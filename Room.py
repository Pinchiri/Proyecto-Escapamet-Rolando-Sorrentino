from images import *
from Inventory import *
import random
from games import * 

class Room():
    
    def __init__(self, left, middle, right):
        
        self.left = left
        self.middle = middle
        self.right = right
    
    def plaza_rectorado(self):
        
        while True:
            
            direction = input(plaza_rectorado_image).lower()
            
            if direction == "l":
                print("Estas en el banco de la izquierda")
                
                quizizz(inventory)
            
            elif direction == "m":
                print("Estas en el Samán")
                
                saman_game(inventory)
                
            elif direction == "r":
                print("Estas en el banco de la derecha")
            
            elif direction == "b":
                pass
            
            elif direction == "i":
                inventory.show_objects()
                
            else:
                continue
            
        
    def biblioteca(self):
        
        while True:
                
            direction = input(biblioteca_image).lower()
            
            if direction == "l":
                print("Estas en el mueble para sentarse")
                
            
            elif direction == "m":
                print("Estas en el mueble de libros")
                
                
            
            elif direction == "r":
                print("Estas en el gabetero")
            
            elif direction == "f":
                Room.plaza_rectorado(self)
                break
            
            elif direction == "b":
                print("estas en el pasillo")
            
            else:
                print("Eso no es una opción")
                continue
                

        
        
       
        
   
        
    
    
        