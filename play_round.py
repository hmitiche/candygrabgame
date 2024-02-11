# Candy Grab Game
# Play many rounds between agents or human vs. machine
# contributor: hakim mitiche, 2023
# update: 8 Feb 2024
# link: https://github.com/hmitiche/candygrabgame
# credit: Carnegy Mellon University
# original: https://www.cs.cmu.edu/~15381/recitations/rec1/candygrab.zip

from agent000 import Agent000
from agent001 import Agent001
from agent002 import Agent002
from agent003 import Agent003
from agent004 import Agent004
from agent005 import Agent005
from agent006 import Agent006
from agent007 import Agent007
from agent008 import Agent008
from agentRL import AgentRL
from candygrab import CandyGrab

initial_num_pieces = 11             # number of candies at the begining
PLAYER1_PSEUDO = "SweetTooth"
PLAYER2_PSEUDO = "CandyThief"

print(" *** Candy Grab Game *** ")
print(" Number of candies on the table: ", initial_num_pieces)
print(" Would you change the number of candies?")
response = input(" ['y': yes, 'n': no] ")
if response == "y":
    initial_num_pieces = int(input(" Enter a number (>=3): "))
    print(" Number of candies is now: ", initial_num_pieces)
print(" Agents: ag001, ..., ag007, ag008, agentRL")
print(" Select player (eg. 1:agent001, ..., 7:agent007, RL:agentRL, \n\
      0: human (for 2nd player only) ")
player1 = input(" > 1st player: ")
player2 = input(" > 2nd player: ")

if int(player1) == 0:
    print(" [error] you need to select a computer agent for 1st player! ")
    exit()
else:
    PLAYER1_NAME = "ag00" + player1
if int(player2) == 0:
   PLAYER2_PSEUDO = input(" What's your name? >")
   PLAYER2_NAME = "human"
else:
   PLAYER2_NAME = "ag00" + player2

if player1 == player2:
    print(" [warning] the same agent plays against its clone!\n")
print(" 0: pick up one at random, 1: 1st player, 2: 2nd player)")    
start = input(" Who starts first? ")
    
start = int(start) - 1          
    # creates the players
match int(player1):
    case 1: bot1 = Agent001(PLAYER1_NAME, initial_num_pieces)
    case 2: bot1 = Agent002(PLAYER1_NAME, initial_num_pieces)
    case 3: bot1 = Agent003(PLAYER1_NAME, initial_num_pieces)
    case 4: bot1 = Agent004(PLAYER1_NAME, initial_num_pieces)
    case 5: bot1 = Agent005(PLAYER1_NAME, initial_num_pieces)
    case 6: bot1 = Agent006(PLAYER1_NAME, initial_num_pieces)
    case 7: bot1 = Agent007(PLAYER1_NAME, initial_num_pieces)
    case 8: bot1 = Agent008(PLAYER1_NAME, initial_num_pieces)
    case -1: bot1 = AgentRL(PLAYER1_NAME, initial_num_pieces)
    case _: bot1 = Agent007(PLAYER1_NAME, initial_num_pieces)

match int(player2):
    case 0: bot2 = Agent000(PLAYER2_NAME, initial_num_pieces)
    case 1: bot2 = Agent001(PLAYER2_NAME, initial_num_pieces)
    case 2: bot2 = Agent002(PLAYER2_NAME, initial_num_pieces)
    case 3: bot2 = Agent003(PLAYER2_NAME, initial_num_pieces)
    case 4: bot2 = Agent004(PLAYER2_NAME, initial_num_pieces)
    case 5: bot2 = Agent005(PLAYER2_NAME, initial_num_pieces)
    case 6: bot2 = Agent006(PLAYER2_NAME, initial_num_pieces)
    case 7: bot2 = Agent007(PLAYER2_NAME, initial_num_pieces)
    case 8: bot1 = Agent008(PLAYER1_NAME, initial_num_pieces)
    case -1: bot2 = AgentRL(PLAYER1_NAME, initial_num_pieces)
    case _: bot2 = Agent007(PLAYER2_NAME, initial_num_pieces)  

bot1.setPseudo(PLAYER1_PSEUDO)
bot2.setPseudo(PLAYER2_PSEUDO)
print(PLAYER1_NAME+"("+PLAYER1_PSEUDO+") vs. "+\
    PLAYER2_NAME+"("+PLAYER2_PSEUDO+")")
agents = (bot1, bot2)
game = CandyGrab(agents, initial_num_pieces)
game.play(start=start, pause=1)

#for agent in agents:
#    agent.print_stats()