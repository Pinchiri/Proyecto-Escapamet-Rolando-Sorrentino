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
        
        message_middle = response_json[2]["objects"][0]["game"]["message_requirement"]
        
        while True:
            
            has_requirements = False
            
            direction = input(plaza_rectorado_image).lower()
            
            if direction == "l":
                print("\n Estas en el banco de la izquierda")
                
                quizizz_game(inventory)

                
            elif direction == "f":
                Room.biblioteca(self)
                break
            
            elif direction == "m":
                print("\n Estas en el Samán")
                
                if has_requirements:
                    
                    saman_game(inventory)
                
                else:
                    print("\n", message_middle)
                    print(" Necesitas ser el mejor jugador del mundo para vencer al Samán")
                
            elif direction == "r":
                print("\n Estas en el banco de la derecha")

                memory_game(inventory)
            
            elif direction == "i":
                inventory.show_objects()
                
            else:
                continue
            
        
    def biblioteca(self):
        
        message_left = response_json[1]["objects"][1]["game"]["message_requirement"]
        message_right =response_json[1]["objects"][2]["game"]["message_requirement"]
        
        while True:
            
            has_math = False 
            has_key = False
            
            if derivada.requirement in inventory.objects:
                has_math = True
            
            if cryptogram.requirement in inventory.objects:
                has_key = True
            
            direction = input(biblioteca_image).lower()
            
            if direction == "l":
                print("\n Estas en el mueble para sentarse")
                
                if has_math:
                    derivada_game(inventory)
                    
                else:
                    print("\n", message_left)
                    
            elif direction == "m":
                print("\n Estas en el mueble de libros")
                
                ahorcado_game(inventory)
                
                    
            elif direction == "r":
                print("\n Estas en el gabetero")
                
                if has_key:
                    
                    cryptogram_game(inventory)
                
                else:
                    print("\n", message_right)
            
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
        
        message_left =  response_json[0]["objects"][1]["game"]["message_requirement"]
        message_right = response_json[0]["objects"][2]["game"]["message_requirement"]
        
        while True:
            
            has_cable = False
            has_password = False
            
            if python_g.requirement in inventory.objects:  
                has_cable = True
            
            if scrabble.reward in inventory.objects:
                has_password = True
            
                
            direction = input(laboratorio_image).lower()
            
            if direction == "l":
                print("\n Estas en la computadora de la izquierda")
                
                if has_cable:
                    
                    python_g()
                
                else:
                    print("\n", message_left)
            
            elif direction == "m":
                print("\n Estas en la pizarra")
                
                alphabet_soup(inventory)
                
               
                    
                
                    
            elif direction == "r":
                print("\n Estas en la computadora de la derecha")
                
                if has_password:
                    adivinanza_game(inventory)
                    
                else:
                    print("\n", message_right)
                
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
        
        message_middle = requirement = response_json[4]["objects"][0]["game"]["message_requirement"]
        
        while True:
            
            has_final = False   
            
            if final.requirement in inventory.objects:
                has_final = True
            
            direction = input(servidores_image).lower()
            
            if direction == "l":
                print("\n Estas en la estantería")
                
                scrabble_game(inventory)
            
            elif direction == "m":
                print("\n Estas en la puerta final")
                
                if has_final:
                    final_game(inventory)
                    break
                
                else:
                    print("\n", message_middle)
                
                    
            elif direction == "r":
                print("\n Estas en la basura")
                
                choose_num_game(inventory)

            elif direction == "b":
                Room.laboratorio(self)
                break
            
            elif direction == "i":
                inventory.show_objects()
                
            else:
                print("Eso no es una opción")
                continue
        
        
       
        
   
        
    
    
        