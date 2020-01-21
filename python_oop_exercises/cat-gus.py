class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {}".format(self.name, self.age)


gus = Cat("Gus", 9)
beans = Cat("Beans", 10)
# print(Cat.description())
print(gus.description())
print(beans.description())
