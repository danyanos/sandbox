from dataclasses import dataclass

import pandas

# Create a sample dataclass to be used when creating a DataFrame
@dataclass
class Car:
  make: str
  model: str
  year: int
  color: str
  num_passengers: int


if __name__ == '__main__':
  cars_for_sale = [
    Car("Chevrolet", "Malibu", 2014, "grey", 5),
    Car("Volkswagen", "Beatle", 2012, "yellow", 4),
    Car("Pontiac", "Fiero", 1992, "red", 2)
  ]

  cars_dataframe = pandas.DataFrame(cars_for_sale)

  print(cars_dataframe.index)
  print(cars_dataframe.columns)

  sorted_cars = sorted(cars_for_sale, key=lambda car: car.year)
  
  print(sorted_cars)
