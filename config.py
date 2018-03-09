import toml
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "package": {
        "name": "HelloWorld",
        "version": "0.1.0",
        "author": ["yourname@email.com"],
        "executable": True
    },
    "dependencies": {}
}


def build_default_config(location: str, name: str=None):
    if name is not None:
        config = DEFAULT_CONFIG.copy()
        config["package"]["name"] = name
    os.chdir(location)
    with open("Carpet.toml", "w+") as file:
        contents = toml.dumps(config)
        file.write(contents)


def load_config(location: str) -> Dict[Any, Any]:
    with open("Carpet.toml", "r") as file:
        contents = file.read()
        config = toml.loads(contents)
    return config


def set_config(location: str, key: str, value: Any):
    with open("Carpet.toml", "w+") as file:
        contents = file.read()
        config = toml.loads(contents)
        config[key] = value
        contents = toml.dumps(config)
        file.write(contents)
