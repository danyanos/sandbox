from typing import Any, Dict, List
from pathlib import Path

from data_crane.reader.reader_base import BaseReader
from data_crane.data_container import DataContainer


class CsvReader(BaseReader):

    def __init__(self,
                 header: List[str],
                 delimiter: str):
        self.header = header
        self.delimiter = delimiter

    def load_file(self,
                  path: Path) -> DataContainer:
        data: List[Dict[str, Any]] = []
        with path.open(mode='r') as file_handle:
            for line in file_handle:
                fields = line.split(self.delimiter)
                mapping = {}
                for (index, field) in enumerate(fields):
                    mapping[self.header[index]] = field
                
                data.append(mapping)

            return DataContainer(data=data)

