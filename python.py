# Creating a Python class

from snake import Snake


class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True

    def digest_large_prey(self):
        return "Digests large animals so has a wider selection of prey"

    def climb(self):
        return "Able to climb up trees and other various vertical surfaces"

    def constricts_prey(self):
        return "Able to constrict prey to kill them effectively"


fast_python = Python()
print(fast_python.move())  # move() is inherited from Animal class
print(fast_python.hunt())  # hunt() inherited from Reptile class
print(fast_python.use_tongue_to_smell())  # use_tongue_to_smell() is inherited from Snake class
print(fast_python.constricts_prey())  # constricts_prey() is available from Python class
