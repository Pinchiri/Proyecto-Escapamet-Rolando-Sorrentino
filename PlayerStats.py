from Player import *

class PlayerStats(Player): #Clase hija de Player, estadísticas del jugador
    
    def __init__(self, difficulty, clues):
        
        self.difficulty = difficulty
        self.clues = clues
        
       
