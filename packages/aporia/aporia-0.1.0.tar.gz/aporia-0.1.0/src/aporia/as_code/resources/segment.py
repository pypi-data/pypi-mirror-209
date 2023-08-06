from typing import Any

from aporia.as_code.resources.base import BaseResource, CompareStatus
from aporia.sdk.client import Client
from aporia.sdk.segments import Segment as _Segment


class Segment(BaseResource):
    def __init__(
        self,
        resource_name: str,
        /,
        *,
        name: str | None = None,
        field: str | None = None,
        values: list[str] | list[float | int] | None = None,
        # TODO: Support new custom segment API
    ):
        self.name = resource_name
        if name is None:
            name = resource_name

        self._args = {"name": name}
        if field is not None:
            if values is None:
                raise Exception("Must supply values for automatic segment")
            self._args["field_name"] = field
            self._args["values"] = values

    def compare(self, resource_data: dict) -> CompareStatus:
        if all([self._args[k] == resource_data[k] for k in self._args.keys()]):
            return CompareStatus.SAME
        return CompareStatus.UPDATEABLE

    def setarg(self, arg_name: str, arg_value: Any):
        self._args[arg_name] = arg_value

    def create(self, client: Client) -> tuple[str, dict]:
        segment = _Segment.create(client=client, **self._args)
        return segment.id, segment.raw_data

    def read(self, client: Client, id: str) -> dict:
        return _Segment.read(client=client, id=id).raw_data

    def update(self, client: Client, id: str) -> dict:
        segment = _Segment.read(client=client, id=id)
        segment.update(**self._args)
        return segment.raw_data

    @classmethod
    def delete(cls, client: Client, id: str):
        _Segment.delete_by_id(client=client, id=id)
