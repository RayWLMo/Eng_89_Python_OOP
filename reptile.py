# Step 2 - Create a reptile class to inherit Animal class
# if not in the same directory, the class needs to be imported with an absolute path
from animal import Animal


class Reptile(Animal):  # Inheriting from Animal class

    def __init__(self):
        super().__init__()  # super() is used to inherit everything from the parent class
        self.cold_blooded = True
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        return "Must sit in the sun for some heat"

    def hunt(self):
        return "Must hunt for food to survive"

    def use_venom(self):
        return "Uses venom on prey and potential threats"


# Creating an object of the Reptile class
smart_reptile = Reptile()
print(smart_reptile.breathe())  # breathe() method is inherited from Animal class
print(smart_reptile.hunt())  # hunt() is available in Reptile class
