import pathlib

import toml

from ..__type import FileProvider


class TOMLProvider(FileProvider):
    def read(self, path: pathlib.Path) -> dict:
        with open(path, 'r') as file: return toml.load(file)

    def write(self, path: pathlib.Path, data: dict) -> None:
        with open(path, 'w') as file: toml.dump(data, file)
