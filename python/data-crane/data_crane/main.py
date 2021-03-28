import sys
from typing import Any, Dict
from pathlib import Path
from dataclasses import dataclass

from data_crane.reader.csv_reader import CsvReader


@dataclass
class Car():
    make: str
    model: str
    year: int


def as_dataclass(data: Dict[str, Any], classname):
    make = data["make"]
    model = data["model"]
    year = data["year"]

    return classname(make, model, year)


if __name__ == "__main__":

    file_name = sys.argv[1]
    header_row = ["year", "model", "make"]

    file_reader = CsvReader(header=header_row,
                            delimiter='|')
    
    container = file_reader.load_file(Path(file_name))
    print(container.get_data())

    dataclass_data = container.as_dataclass(Car)
    print(dataclass_data)