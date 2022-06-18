import json
import yaml
from yaml.loader import SafeLoader
from creational.handson.context import Context


def load_context(file_path: str):
    if file_path.endswith(".json"):
        data = _load_from_json(file_path)
    elif file_path.endswith(".yaml"):
        data = _load_from_yaml(file_path)
    else:
        raise ValueError(f"Invalid file extension for context: {file_path}")
    return Context(**data)


def _load_from_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)


def _load_from_yaml(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return yaml.load(f, Loader=SafeLoader)
