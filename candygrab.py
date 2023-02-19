'''
Play game where players (Agents) take turns selecting
one or two of the remaining pieces. The player that
takes the last piece wins.
edit: Hakim Mitiche, credit: Carnegy Mellon Univeristy
prints who start first, enable the selection of 
who starts first
'''
# edited by: Dr. Hakim Mitiche
# update: Feb 2023

import random
from agent import Agent
from agent001 import Agent001
from agent002 import Agent002
from agent003 import Agent003
from agent004 import Agent004
from agent005 import Agent005
from agent006 import Agent006
from agent007 import Agent007
from agent008 import Agent008
from agentRL import AgentRL

RANDOM_START = -1     # pick up the player to start at random

class CandyGrab:
    def __init__(self, agents, init_num_pieces):
        self.agents = agents
        self.num_pieces = init_num_pieces
    
    # randomly pick up who starts first (default)    
    def play(self, display=True, start=RANDOM_START):

         # select randomly who starts first
        if start == RANDOM_START:
            turn = random.randrange(0,2)
        else: 
            turn = start    

        if display:
            print(self.agents[turn].name + "(" +  
                self.agents[turn].pseudo + ") starts!\n")
            print(" Goal: whoever grabs the last candy wins!!\n")
        
        while self.num_pieces > 0:
            
            if display:
                print("{} pieces remaining".format(self.num_pieces))
            
            num_selected = self.agents[turn].getAction(self.num_pieces)

            if num_selected != 1 and num_selected != 2 :
                print("Bogus! Can't select {}".format(num_selected))
                return

            self.num_pieces = self.num_pieces - num_selected
            
            if display:
                print("\t{} picks {}".format(self.agents[turn], num_selected))
            
            turn = (turn+1) % len(self.agents)            

        self.agents[(turn+1) % len(self.agents)].win()
        self.agents[turn].lose()
        
        if display:
            print("\n >>> {} wins!\n".format(self.agents[(turn+1) % len(self.agents)]))

# to run if the game is launched here from terminal
if __name__ == '__main__':
    initial_num_pieces = 11

    hal = Agent001("HAL", initial_num_pieces)
    walle = Agent007("WALL-E", initial_num_pieces)
    # bb8 isn't used?!
    bb8 = AgentRL("BB-8", initial_num_pieces)

    game = CandyGrab((walle, hal), initial_num_pieces)
    game.play()
    
