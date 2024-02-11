# edit: Hakim Mitiche, 2024
import random
from agent import Agent

class Agent007(Agent):
    def __init__(self, name, initial_num_pieces):
        Agent.__init__(self, name, initial_num_pieces)
        self.strategy = "Pickup candies such that to try "+\
        " reach 3 candies left before its last move"

    def getAction(self, state):
        if state % 3 == 2 :
            return 2
        else : 
            return 1
        
