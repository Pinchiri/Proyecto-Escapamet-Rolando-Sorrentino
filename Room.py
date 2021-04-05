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
                print("\n Estas en el banco de la izquierda")
                
                quizizz(inventory)
                continue
                
            elif direction == "f":
                Room.biblioteca(self)
                break
            
            elif direction == "m":
                print("\n Estas en el Samán")
                
                saman_game(inventory)
                
            elif direction == "r":
                print("\n Estas en el banco de la derecha")

                memory_game(inventory)
            
            elif direction == "i":
                inventory.show_objects()
                
            else:
                continue
            
        
    def biblioteca(self):
        
        while True:
                
            direction = input(biblioteca_image).lower()
            
            if direction == "l":
                print("\n Estas en el mueble para sentarse")
                continue
            
            elif direction == "m":
                print("\n Estas en el mueble de libros")
                
                ahorcado_game(inventory)
                
                    
            elif direction == "r":
                print("\n Estas en el gabetero")
                continue
            
            elif direction == "f":
                Room.plaza_rectorado(self)
                break
            
            elif direction == "b":
                Room.pasillo_laboratorio(self)
                break
            
            elif direction == "i":
                inventory.show_objects()
                
            else:
                print("Eso no es una opción")
                continue
            
    def pasillo_laboratorio(self):
        
        while True:
            message_requirement = response_json[3]["objects"][0]["game"]["message_requirement"]
            
            has_requirement = False
            door_opened = False
            
            if door_hallway.reward in inventory.objects:
                door_opened = True
            
            if door_hallway.requirement in inventory.objects:   
                has_requirement = True
                
            else:
                has_requirement = False
            
            if not door_opened:
                    
                direction = input(pasillo_laboratorio_closed_image).lower()
                
                if len(direction) == 0:
                    
                    if has_requirement:
                        
                        boolean_logic(inventory)
                        continue
                             
                    else:
                        print("\n", message_requirement) 
                        continue    
                
                elif direction == "b":
                    
                    Room.biblioteca(self)
                
                elif direction == "i":
                    inventory.show_objects()
                    
                else:
                    print("Eso no es una opción")
                    continue
                
            elif door_opened:
                
                direction = input(pasillo_laboratorio_opened_image).lower()
                    
                if direction == "f":
                        
                    Room.laboratorio(self)  
                    break  
                    
                elif direction == "b":
                        
                    Room.biblioteca(self)
                    break
                    
                elif direction == "i":
                    inventory.show_objects()
                        
                else:
                    print("Eso no es una opción")
                    continue   
        
    def laboratorio(self):
        
        while True:
                
            direction = input(laboratorio_image).lower()
            
            if direction == "l":
                print("\n Estas en la computadora de la izquierda")
                pass
            
            elif direction == "m":
                print("\n Estas en la pizarra")
                
                alphabet_soup(inventory)
                
                    
            elif direction == "r":
                print("\n Estas en la computadora de la derecha")
                
                adivinanza_game(inventory)
                
            elif direction == "f":
                Room.servidores(self)
            
            elif direction == "b":
                Room.pasillo_laboratorio(self)
                break
            
            elif direction == "i":
                inventory.show_objects()
                
            else:
                print("Eso no es una opción")
                continue
    
    def servidores(self):
        
        while True:
                
            direction = input(servidores_image).lower()
            
            if direction == "l":
                print("\n Estas en la estantería")
                continue
            
            elif direction == "m":
                print("\n Estas en la puerta final")
                
                ahorcado_game(inventory)
                
                    
            elif direction == "r":
                print("\n Estas en la basura")
                continue

            elif direction == "b":
                Room.laboratorio(self)
                break
            
            elif direction == "i":
                inventory.show_objects()
                
            else:
                print("Eso no es una opción")
                continue
        
        
       
        
   
        
    
    
        