from images import * #Dibujos
from functions import * #Funciones
from Player import * #Clase Player
from PlayerStats import * #Clase Stats
from Game import * #Clase Game
from Room import * #Clase Room
import random

def main(): 
    
    while True:
        
        choice = input(bienvenue)
        
        if choice == "1":
            players_verification() #Función de registro y verificación de usuarios existentes
            continue
        
        elif choice == "2":
            player = login() #Función para loggearse
            
        else:
            print("\nIngreso Inválido\n")
            continue
         
        difficulty = set_difficulty()
            
        player_stats = game_start(difficulty, player) #Función para iniciar el juego y mostrar las narrativas iniciales
        
        print(player_stats.clues)
        print(player_stats.difficulty)
        inventory = set_inventory()
            
        #Primera sala
            
        Room.biblioteca(biblioteca)
         
            
            
            
        
main()

