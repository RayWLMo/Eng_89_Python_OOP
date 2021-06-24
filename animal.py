# Creating an Animal class

# Step 1

class Animal:  # follow the correct naming convention
    # we need to initialise with built-in method called __init__(self)
    # self refers to current class
    def __init__(self):  # Declaring attributes in the init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "Keep eating to stay alive"

    def move(self):
        return "Move around to stay aware"


# We need to create an object of this class in order to use any methods
cat = Animal()  # Creating an object of Animal class
# For `cat` as a user the functionality inside Animal class and the method breathe is abstracted
print(cat.eat())
print(cat.breath())
