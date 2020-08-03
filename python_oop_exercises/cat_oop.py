class Cat:
    species = 'mammal'
    legs = 4
    eyes = 2
    tail = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def eat(self, food):
        self.food = food
        return "{} ate {} pounds of food".format(self.name, self.food)


gus = Cat("Gus", 9)
description = gus.description()
print(gus.eat(1))
# gus.description()
