# Candy Grab Game
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

# play many games between two agent
# then print stats without (game details)

initial_num_pieces = 11
num_games = 1000
PLAYER1_PSEUDO = "SweetTooth"
PLAYER2_PSEUDO = "AlphaCandy"
display = False

print(" ******* Candy Grab Game ********** ")
print(" credit: Carnegie-Mellon University ")
print(" contributor: Hakim Mitiche ")
print(" ***********************************")
print(" Number of candies on the table: ", initial_num_pieces)
response = input("Change? (y: yes)")
if response == "y":
    initial_num_pieces = int(input(" Enter a number (>=3): "))
    #print(" Number of candies is now: ", initial_num_pieces)
print(" Number of rounds to play: ", num_games)    
response = input("Change? (y: yes)")
if response == "y":
    num_games = int(input(" Enter a number ([3...100]): "))
    #print(" Number of rounds to play: ", num_games) 
"""
print(" Would you change the number of candies?")
response = input(" ['y': yes, 'n': no]")
if response == "y":
    initial_num_pieces = int(input(" Enter a number (>=3): "))
    print(" Number of candies is now: ", initial_num_pieces)
"""
print(" Agents: ag001, ..., ag008, agRL, Human")
print(" Select two agents (eg. 1,...,8, 9:RL, 0:human)")

player1 = input(" > 1st player: ")
player2 = input(" > 2nd player: ")
if player1 == player2:
    print(" [warning] the 2nd player is a clone of 1st player!\n")
#start = input(" who starts first: 1, 2? (0: pick one at random): ")
#start = int(start) - 1
print(" agent who starts playin is picked up randomly at each game!")
if player1 == "0":
    PLAYER1_NAME = "human"
elif player1 == "9":
    PLAYER1_NAME = "agentRL"
else : PLAYER1_NAME = "ag00" + player1
if player2 == "0":
    PLAYER2_NAME = "human"
elif player2 == "9":
        PLAYER2_NAME = "agentRL"
else : PLAYER2_NAME = "ag00" + player2

match int(player1):
    case 1: bot1 = Agent001(PLAYER1_NAME, initial_num_pieces)
    case 2: bot1 = Agent002(PLAYER1_NAME, initial_num_pieces)
    case 3: bot1 = Agent003(PLAYER1_NAME, initial_num_pieces)
    case 4: bot1 = Agent004(PLAYER1_NAME, initial_num_pieces)
    case 5: bot1 = Agent005(PLAYER1_NAME, initial_num_pieces)
    case 6: bot1 = Agent006(PLAYER1_NAME, initial_num_pieces)
    case 7: bot1 = Agent007(PLAYER1_NAME, initial_num_pieces)
    case 8: bot1 = Agent008(PLAYER1_NAME, initial_num_pieces)
    case 9: bot1 = AgentRL(PLAYER1_NAME, initial_num_pieces)
    case _: bot1 = Agent000(PLAYER1_NAME, initial_num_pieces)

match int(player2):
    case 1: bot2 = Agent001(PLAYER2_NAME, initial_num_pieces)
    case 2: bot2 = Agent002(PLAYER2_NAME, initial_num_pieces)
    case 3: bot2 = Agent003(PLAYER2_NAME, initial_num_pieces)
    case 4: bot2 = Agent004(PLAYER2_NAME, initial_num_pieces)
    case 5: bot2 = Agent005(PLAYER2_NAME, initial_num_pieces)
    case 6: bot2 = Agent006(PLAYER2_NAME, initial_num_pieces)
    case 7: bot2 = Agent007(PLAYER2_NAME, initial_num_pieces)
    case 8: bot2 = Agent008(PLAYER1_NAME, initial_num_pieces)
    case 9: bot2 = AgentRL(PLAYER1_NAME, initial_num_pieces)
    case _: bot2 = Agent000(PLAYER2_NAME, initial_num_pieces)  

bot1.setPseudo(PLAYER1_PSEUDO)
bot2.setPseudo(PLAYER2_PSEUDO) 
print(" {0}({1}) vs. {2}({3}) for {4} rounds!".\
    format(PLAYER1_NAME,PLAYER2_NAME,PLAYER1_PSEUDO,PLAYER2_PSEUDO,num_games))

agents = (bot1, bot2)
if PLAYER1_NAME == "human" or PLAYER2_NAME == "human":
    details = True
else: 
    details = False    
for i in range(num_games):
    game = CandyGrab(agents, initial_num_pieces)
    if details:
        print("  Game #{}\n".format(i))
    game.play(display=details)

print(" >>> Results: ")
for agent in agents:
    agent.print_stats()


