# contributor: Hakim Mitiche, 2024
# agent 000 is a human player
import random
from agent import Agent

class Agent000(Agent):

    def __init__(self, name, initial_num_pieces):
        Agent.__init__(self, name, initial_num_pieces, "", True)
        self.strategy = "Depends on the person intelligence, experience or chance!"

     # always pickup one candy   
    def getAction(self, state, message=" your turn (1 or 2 candies)?:"):
        #return int(input("your turn (1 or 2 candies)?: "))
        return int(input(message))