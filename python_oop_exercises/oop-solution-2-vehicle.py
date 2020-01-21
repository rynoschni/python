# Exercise 2
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(f"{self.year} {self.make} {self.model}")

car = Vehicle("Volkswagen", "GTI", "2017")
car.print_info()