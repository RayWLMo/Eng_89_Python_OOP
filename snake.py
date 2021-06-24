# Creating a Snake class

from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.tetrapods = False

    # Adding specific methods/behaviours
    def use_tongue_to_smell(self):
        return "Uses tongue to seek out prey by smelling"

    def slithers_to_move(self):
        return "Slides side to side in a slither motion to move"


# Creating an object of Snake class
smart_snake = Snake()
print(smart_snake.move())  # move() is inherited from Animal class
print(smart_snake.hunt())  # hunt() is inherited from Reptile class
print(smart_snake.use_tongue_to_smell())  # use_tongue_to_smell() is available from Snake class
