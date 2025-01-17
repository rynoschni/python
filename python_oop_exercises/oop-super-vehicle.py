# Exercise 2
class Vehicle:
    def __init__(self, type_of_vehicle, make, model, year):
        self.type_of_vehicle = type_of_vehicle
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return "My %s is a %d %s %s " % (self.type_of_vehicle, self.year, self.make, self.model)


class Hatchback(Vehicle):
    def __init__(self, type_of_vehicle, make, model, year, doors):
        super().__init__(type_of_vehicle, make, model, year)
        self.doors = doors

    def __str__(self):
        return "My %s is a %d %s %s with %d doors" % (self.type_of_vehicle, self.year, self.make, self.model, self.doors)


boaty = Vehicle("boat", "Boat", "Speed", 2001)
print(boaty)

rex = Hatchback("car", "VW", "Golf", 2018, 5)
print(rex)
