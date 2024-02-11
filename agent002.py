import random
from agent import Agent

# state: number of remaining candies
class Agent002(Agent):
    
    def __init__(self, name, initial_num_pieces):
        Agent.__init__(self, name, initial_num_pieces)
        self.strategy = "Always pickup two candies!"
        
    def getAction(self, state):
        action = 2
        return min(action, state)  
        # Don't choose more that what is left

