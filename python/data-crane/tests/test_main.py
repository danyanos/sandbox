from dataclasses import dataclass

from data_crane.main import as_dataclass


@dataclass
class Car():
    make: str
    model: str
    year: int


def test_as_dataclass():
    dict_data = {
        "make": "chevrolet",
        "model": "malibu",
        "year": 2014
    }

    result = as_dataclass(dict_data, Car)
    print(result)

    assert False
