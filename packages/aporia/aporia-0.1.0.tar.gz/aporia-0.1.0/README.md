# Aporia Monitor as Code
This repository contains 2 parts:
1. aporia - An unofficial SDK for Aporia
1. mac - An IaC-style API for managing Aporia resources
# SDK Usage
```
from aporia.aporia_api import Aporia
aporia = Aporia(
    base_url="https://platform.aporia.com", 
    token="<APORIA_TOKEN>",
    account="<APORIA_ACCOUNT_ID>"
    )

my_model = aporia.create_model(...)
my_version = my_model.create_version(...)
my_monitor = my_model.create_monitor(...)
```
# MaC Usage
```
import mac

my_model = mac.Model("credit-risk", {"name": "Credit Risk", ...})

dataset = mac.Dataset("serving", {"model": my_model}, {"type": "serving", "connection": ...})

mac.export(my_model)
```