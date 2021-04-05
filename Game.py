import random
from functions import *
from Inventory import *
from Player import *
from images import *
from PlayerStats import PlayerStats

class Game(): #Clase Juego
    
    def __init__(self, gamename, reward, rules, requirement):
        
        self.gamename = gamename
        self.reward = reward
        self.rules = rules 
        self.requirement = requirement
           
        
        
    
       

    