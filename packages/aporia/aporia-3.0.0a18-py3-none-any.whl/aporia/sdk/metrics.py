from dataclasses import dataclass
import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel

from aporia.sdk.client import Client
from aporia.sdk.datasets import DatasetType


class TimeRange(BaseModel):
    start: datetime.datetime
    end: datetime.datetime  # "2023-05-12T00:00:00.000000+00:00"

    def serialize(self):
        return {
            "start": self.start.isoformat(timespec="microseconds") + "+00:00",
            "end": self.end.isoformat(timespec="microseconds") + "+00:00",
        }


class MetricSegment(BaseModel):
    id: str
    value: str  # TODO: Test with numeric auto segments

    def serialize(self) -> dict:
        return {"id": self.id, "value": self.value}


class MetricDataset(BaseModel):
    dataset_type: DatasetType = DatasetType.SERVING
    time_range: TimeRange | None = None
    model_version: str | None = None
    segment: MetricSegment | None = None

    def serialize(self) -> dict:
        return {
            "dataset_type": self.dataset_type.value,
            "time_range": self.time_range.serialize() if self.time_range is not None else None,
            "model_version": self.model_version,
            "segment": self.segment.serialize() if self.segment is not None else None,
        }


class MetricResponse(BaseModel):
    id: str
    value: Any
    error: dict | list | str | None
    segment: MetricSegment | None


class QueryResponse(BaseModel):
    metrics: list[MetricResponse]
    time_range: TimeRange


class MetricParameters(BaseModel):
    dataset: MetricDataset
    # Metric identifier
    name: str
    # Parameters
    column: str | None = None
    k: int | None = None
    threshold: float | None = None
    custom_metric_id: str | None = None
    baseline: MetricDataset | None = None


class MetricError(Exception):
    def __init__(self, error, parameters: MetricParameters):
        super().__init__(error)
        self.parameters = parameters


class AporiaMetrics:
    def __init__(
        self,
        token: str,
        account_name: str,
        base_url: str = "https://platform.aporia.com",
        workspace_name: str = "default-workspace",
    ) -> dict:
        self.client = Client(
            base_url=f"{base_url}/api/v1/{account_name}/{workspace_name}", token=token
        )

    def query(
        self,
        # Dataset identifiers
        model_id: str,
        dataset: MetricDataset,
        # Metric identifier
        metric_name: str,
        baseline: MetricDataset | None = None,
        # Parameters
        column: str | None = None,
        k: int | None = None,
        threshold: float | None = None,
        custom_metric_id: str | None = None,
    ):
        metric_parameters = {}
        if column is not None:
            metric_parameters["column"] = column
        if k is not None:
            metric_parameters["k"] = k
        if threshold is not None:
            metric_parameters["threshold"] = threshold
        if custom_metric_id is not None:
            metric_parameters["id"] = custom_metric_id

        metric_datasets = {"data": dataset.serialize()}
        if baseline is not None:
            metric_datasets["baseline"] = baseline.serialize()

        response = self.client.send_request(
            "/query",
            method="POST",
            data={
                "model_id": model_id,
                "metrics": [
                    {
                        "id": "0",
                        "metric": metric_name,
                        "parameters": metric_parameters,
                        "datasets": metric_datasets,
                    }
                ],
            },
            url_search_replace=("/api/v1/", "/v1/metrics-reducer/"),
        )
        self.client.assert_response(response)

        result = [QueryResponse(**entry) for entry in response.json()]

        if result[0].metrics[0].error is not None:
            raise Exception(f"Error occured: {result[0].metrics[0].error}")
        return result[0].metrics[0].value

    def query_batch(self, model_id: str, metrics: list[MetricParameters]):
        metric_requests = []
        for i, metric in enumerate(metrics):
            metric_parameters = {}
            if metric.column is not None:
                metric_parameters["column"] = metric.column
            if metric.k is not None:
                metric_parameters["k"] = metric.k
            if metric.threshold is not None:
                metric_parameters["threshold"] = metric.threshold
            if metric.custom_metric_id is not None:
                metric_parameters["id"] = metric.custom_metric_id

            metric_datasets = {"data": metric.dataset.serialize()}
            if metric.baseline is not None:
                metric_datasets["baseline"] = metric.baseline.serialize()
            metric_requests.append(
                {
                    "id": str(i),
                    "metric": metric.name,
                    "parameters": metric_parameters,
                    "datasets": metric_datasets,
                }
            )

        response = self.client.send_request(
            "/query",
            method="POST",
            data={
                "model_id": model_id,
                "metrics": metric_requests,
            },
            url_search_replace=("/api/v1/", "/v1/metrics-reducer/"),
        )
        self.client.assert_response(response)

        result = [QueryResponse(**entry) for entry in response.json()]

        # Restore order, because different timeframes may change order
        metric_results = {}
        for entry in result:
            for metric in entry.metrics:
                metric_index = int(metric.id)
                if metric.error is not None:
                    metric_results[metric_index] = MetricError(
                        error=metric.error, parameters=metrics[metric_index]
                    )
                else:
                    metric_results[metric_index] = metric.value

        return [metric_results[i] for i in range(len(metric_results))]
