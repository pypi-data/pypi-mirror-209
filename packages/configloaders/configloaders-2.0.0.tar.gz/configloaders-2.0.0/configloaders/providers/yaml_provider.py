import pathlib

import yaml

from ..__type import FileProvider


class YAMLProvider(FileProvider):
    def read(self, path: pathlib.Path) -> dict:
        with open(path, 'r') as file: return yaml.safe_load(file)

    def write(self, path: pathlib.Path, data: dict) -> None:
        with open(path, 'w') as file: yaml.safe_dump(data, file)
