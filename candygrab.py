'''
Candy Grab Game
where two players (Agents) take turns to 
one or two of the remaining candies. 
The player thattakes the last piece wins.
edit: Hakim Mitiche, 
credit: Carnegy Mellon Univeristy
contributionq: user-friendly display, election of 
who starts the gamme, arbitrary selection, enable 
a human to play the agents
'''
# edited by: Dr. Hakim Mitiche, 2023
# update: 10 Feb 2024

import random
from time import sleep
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

RANDOM_START = -1     # pick up the player which starts at random

class CandyGrab:
    def __init__(self, agents, init_num_pieces):
        self.agents = agents
        self.num_pieces = init_num_pieces
    
    # randomly pick up who starts first, by default
    # pause: waiting time between two turns
    def play(self, display=True, start=RANDOM_START, pause=0):

         # select randomly who starts first
        if start == RANDOM_START:
            turn = random.randrange(0,2)
        else: 
            turn = start    
        # should I display the game details?
        if display:
            print(self.agents[turn].name + "(" +  
                self.agents[turn].pseudo + ") starts!\n")
            print(" Rules: pickup 1 or 2 candies!")
            print(" Goal: whoever grabs the last candy wins!!\n")
            print("\t     turn | candies | move ")
            print("\t     ---- | ------- | ---- ")
        
        while self.num_pieces > 0:     
            if display:
                #print("{} pieces remaining".format(self.num_pieces))
                #playerName = self.agents[turn].pseudo
                playingNow = "p"+str(turn+1)           # p1 or p2 (player 2)
                if not self.agents[turn].isHuman:
                    num_selected = self.agents[turn].getAction(self.num_pieces)
                    lineToPrint = "\t     {0}     {1}         {2}".\
                    format(playingNow, self.num_pieces, num_selected)
                    print(lineToPrint)
                else:
                    lineToPrint = "play!        {0}     {1}          ".\
                    format(playingNow, self.num_pieces)
                    num_selected = self.agents[turn].getAction(self.num_pieces,\
                        lineToPrint)
            else: 
                num_selected = self.agents[turn].getAction(self.num_pieces)

            if num_selected != 1 and num_selected != 2 :
                print("Bogus! Can't select {}".format(num_selected))
                #return
                continue

            self.num_pieces = self.num_pieces - num_selected
            
            #if display:
            #    print("\t{} picks {}".format(self.agents[turn], num_selected))
            
            turn = (turn+1) % len(self.agents)
            if (pause != 0):
                sleep(pause) 
        # print the last line that shows the loser can't play
        if display:      
            print("\t     p{0}     {1}         {2}".format(turn+1, self.num_pieces, ":("))       
        self.agents[turn].lose()
        self.agents[(turn+1) % len(self.agents)].win()
        
        if display:
            winner = (turn+1) % len(self.agents)
            print("\n >>> {0} ({1} :)) wins!\n".format(self.agents[winner],
                self.agents[winner].pseudo))
            for a in self.agents:
                print("\t", a.name, "strategy: ", a.strategy)

# to run if the game is launched here from terminal
if __name__ == '__main__':
    initial_num_pieces = 11

    hal = Agent001("HAL", initial_num_pieces)
    walle = Agent007("WALL-E", initial_num_pieces)
    # bb8 isn't used?!
    bb8 = AgentRL("BB-8", initial_num_pieces)

    game = CandyGrab((walle, hal), initial_num_pieces)
    game.play()