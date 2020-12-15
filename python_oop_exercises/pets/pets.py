class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        Hunger: %d
        Mopiness: %d
        """ % (self.name, self.fullness, self.happiness, self.hunger, self.mopiness)

    def be_alive(self):
        print("Be Alive Method For Pet Class for %s" % (self.name))
        print("THIS APPLIES TO ALL PET CLASSES AND SUBCLASSES")

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5, cuddle_level="Cuddly"):
        super().__init__(name, fullness, happiness, hunger, mopiness)
        self.cuddle_level = cuddle_level

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        Cuddle Level: %s
        """ % (self.name, self.fullness, self.happiness, self.cuddle_level)

    def be_alive(self):
        super().be_alive()

guster = Pet("Guster", 10, 100, 200, 0)
beans = CuddlyPet("Beans", 10, 100, 200, 0, "Extra Cuddly")

guster.be_alive()
beans.be_alive()
