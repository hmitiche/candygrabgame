import random
from agent import Agent

class Agent001(Agent):
    def __init__(self, name, initial_num_pieces):
        Agent.__init__(self, name, initial_num_pieces)
        self.strategy = "Always pickup one candy!"
        
    def getAction(self, state):
        return 1

