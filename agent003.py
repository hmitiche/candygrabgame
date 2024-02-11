import random
from agent import Agent
# prev_state: number of pieces left after the agent last move 
# prev_move: number of candies pickup in its last turn
# strategy: initialy (1st to play),it pickups a number at random,
# then, it repeats the opponent move

class Agent003(Agent):
    def __init__(self, name, initial_num_pieces):
        Agent.__init__(self, name, initial_num_pieces)
        self.prev_state = self.initial_num_pieces
        self.strategy = "chooses the same move as the opponent!"
        
    def getAction(self, state):
        # If at the start of the game           
        if state == self.initial_num_pieces :
            action = random.randrange(1,3)    # pickup randomly 1 or 2
            self.prev_state = state-action;
            return action
        else :
            # number of pieces picked up by the opponent, last turn
            prev_move = self.prev_state-state   
            action = prev_move; # Same
            action = min(action, state)
            # Don't choose more that what is left
            self.prev_state = state-action;
            return action

    def win(self):
        super().win()
        self.prev_state = self.initial_num_pieces

    def lose(self):
        super().lose()
        self.prev_state = self.initial_num_pieces
