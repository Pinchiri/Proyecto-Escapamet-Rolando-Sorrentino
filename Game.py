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
           

    # def libros_game():
        
    #     gamename = response_json[1]["objects"][0]["game"]["name"]
    #     reward = response_json[1]["objects"][0]["game"]["award"]
    #     rules = response_json[2]["objects"][0]["game"]["rules"]
    #     requirement = response_json[2]["objects"][0]["game"]["requirement"]
    
    #     question = response_json[1]["objects"][0]["game"]["questions"][random.randint(0,2)]
    #     question_displayed = question["question"]
    #     question_answer = question["answer"]
    #     question_1 = response_json[1]["objects"][0]["game"]["questions"][0]["question"]   
    #     question_2 = response_json[1]["objects"][0]["game"]["questions"][1]["question"]
    #     question_3 = response_json[1]["objects"][0]["game"]["questions"][2]["question"]
        
    #     show_question = f"""
    # |--------------------------------------------------------------------------------|
    # |                                                                                |
    #    Juguemos al {gamename}! 
    #    ({rules}), 
    
    #    Ingresa tu respuesta letra por letra
                    
    #                 {question_displayed}
       
    #   Aquí aparecerán las letras que aciertes ->           
                    
    # |  Si quieres una pista ingresa "p"                                              |
    # |                                                                                |
    # |--------------------------------------------------------------------------------|
    # ------> """
    
    #     while True:
            
    #         if question_displayed == question_1:
    #             answer = input(show_question)
                
    #             if answer in question_1:

    