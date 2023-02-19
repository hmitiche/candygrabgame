# edit: Dr. Hakim Mitiche
# addition: agent pseudo name with default value
import random

class Agent:
    """
    Parent class for all agent implementations.
    Inherit from this Agent class and implement the getAction method.
    """
    def __init__(self, name, initial_num_pieces, pseudo="candyGrabber"):
        self.name = name
        self.pseudo = pseudo
        self.initial_num_pieces = initial_num_pieces
        self.num_wins = 0
        self.num_games = 0

    def setPseudo(self, pseudo):
        self.pseudo = pseudo    
    
    def __str__(self):
        return self.name    
    
    def getAction(self, state):
        raise NotImplementedError
    
    def win(self):
        self.num_games += 1
        self.num_wins += 1

    def lose(self):
        self.num_games += 1

    def print_stats(self):
        if self.num_games == 0:
            win_percent = 0;
        else:
            win_percent = 100 * self.num_wins / self.num_games

        print("{} won {}/{} ({:0.1f}%)".format(self.name, self.num_wins, self.num_games, win_percent))

