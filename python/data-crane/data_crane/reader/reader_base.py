from abc import ABC
from pathlib import Path

from data_crane.data_container import DataContainer


class BaseReader(ABC):

    def load_file(self, file_path: Path) -> DataContainer:
        pass
