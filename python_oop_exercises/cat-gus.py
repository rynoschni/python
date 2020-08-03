class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s is %d" % (self.name, self.age)


gus = Cat("Gus", 9)
beans = Cat("Beans", 10)

print(gus)
