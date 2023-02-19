# edit: hakim mitiche, 
# update: Feb 2023
# link: https://drive.google.com/file/d/1lzDM1O4eRpomf6fC2RHS_O5jwQ1Dy0Ah/view
# credit: Carnegy Mellon University
# original: https://www.cs.cmu.edu/~15381/recitations/rec1/candygrab.zip
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

initial_num_pieces = 11
PLAYER1_PSEUDO = "SweetTooth"
PLAYER2_PSEUDO = "AlphaCandy"

print(" *** Candy Grab Game *** ")
print(" number of candies on the table: ", initial_num_pieces)
print(" Agents: ag001, ..., ag007")
print(" Select the agents (eg. type: 1 for agent001)")
player1 = input(" > 1st player: ")
player2 = input(" > 2nd player: ")
if player1 == player2:
    print(" [warning] the same agent plays against its clone!\n")
start = input(" who starts first: 1, 2? (0: pick one at random): ")
start = int(start) - 1
PLAYER1_NAME = "ag00"+player1 
PLAYER2_NAME = "ag00"+player2
match int(player1):
    case 1: bot1 = Agent001(PLAYER1_NAME, initial_num_pieces)
    case 2: bot1 = Agent002(PLAYER1_NAME, initial_num_pieces)
    case 3: bot1 = Agent003(PLAYER1_NAME, initial_num_pieces)
    case 4: bot1 = Agent004(PLAYER1_NAME, initial_num_pieces)
    case 5: bot1 = Agent005(PLAYER1_NAME, initial_num_pieces)
    case 6: bot1 = Agent006(PLAYER1_NAME, initial_num_pieces)
    case 7: bot1 = Agent007(PLAYER1_NAME, initial_num_pieces)
    case _: bot1 = Agent007(PLAYER1_NAME, initial_num_pieces)

match int(player2):
    case 1: bot2 = Agent001(PLAYER2_NAME, initial_num_pieces)
    case 2: bot2 = Agent002(PLAYER2_NAME, initial_num_pieces)
    case 3: bot2 = Agent003(PLAYER2_NAME, initial_num_pieces)
    case 4: bot2 = Agent004(PLAYER2_NAME, initial_num_pieces)
    case 5: bot2 = Agent005(PLAYER2_NAME, initial_num_pieces)
    case 6: bot2 = Agent006(PLAYER2_NAME, initial_num_pieces)
    case 7: bot2 = Agent007(PLAYER2_NAME, initial_num_pieces)
    case _: bot2 = Agent007(PLAYER2_NAME, initial_num_pieces)  

#walle = Agent007("WALL-E", initial_num_pieces)
#bb8 = AgentRL("BB-8", initial_num_pieces)

#agents = (walle, bb8)
bot1.setPseudo(PLAYER1_PSEUDO)
bot2.setPseudo(PLAYER2_PSEUDO)
agents = (bot1, bot2)

game = CandyGrab(agents, initial_num_pieces)
print(" ag00"+player1+"("+PLAYER1_PSEUDO+") vs. ag00"+\
    player2+"("+PLAYER2_PSEUDO+")")
game.play(start=start)

for agent in agents:
    agent.print_stats()

