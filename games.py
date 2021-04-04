import random
from images import * #Dibujos
import functions #Funciones
from Player import * #Clase Player
from PlayerStats import * #Clase Stats
from Game import * #Clase Game
from Room import * #Clase Room
import requests

response = requests.get('https://api-escapamet.vercel.app/')
response_json = response.json()

#Inventario

def set_inventory():
    
    inventory = Inventory()
    
    return inventory

inventory = Inventory()
#JUEGOS DEL RECTORADO

#Función para hacer el juego del saman un objeto
def set_saman_game():
        
    gamename = response_json[2]["objects"][0]["game"]["name"]
    reward = response_json[2]["objects"][0]["game"]["award"]
    rules = response_json[2]["objects"][0]["game"]["rules"]
    requirement = response_json[2]["objects"][0]["game"]["requirement"]

    return Game(gamename, reward, rules, requirement)

#Juego Samán
def saman_game(inventory):
     
    while True:   
        saman = set_saman_game()
                
        questions = response_json[2]["objects"][0]["game"]["questions"]
            
        print(f"""
        |---------------------------------------------------------------------------------------|
                                                                                        
        Has perdido 20 de vida por pisar el Samán! ---- Te queda 20 de vida               
                                                                                                
        |---------------------------------------------------------------------------------------|
        
        
        
    """)

            
        for question in questions:
            print(question, "\n")
                
        choice = input(f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            {saman.gamename}
            ({saman.rules})
        
            Responde en orden separando los dos resultados con un espacio                
        |                                                                                |           
        |--------------------------------------------------------------------------------|
        ------> """)

        choice = choice.replace(" ", "")

        if choice == "6741":
            
            inventory.add_obj(saman.reward)
            
            print(f"""
        |--------------------------------------------------------------------------------|
                                                                                        
            ¡FELICIDADES! Eres el mejor jugador del mundo y por ello has conseguido un
                                        {saman.reward}      
                                                                                                
        |--------------------------------------------------------------------------------|
        """)
            break
        
        else:
            print("\nHas fallado! ojo pelao con pisar el Samán")
            break
        
        
#Función para hacer quizizz un objeto
def set_quizizz():
    
    gamename = response_json[2]["objects"][1]["game"]["name"]
    reward = response_json[2]["objects"][1]["game"]["award"]
    rules = response_json[2]["objects"][1]["game"]["rules"]
    requirement = response_json[2]["objects"][1]["game"]["requirement"]

    return Game(gamename, reward, rules, requirement)
    
def quizizz(inventory):
        
    quizizz = set_quizizz()

    #Preguntas
    question = response_json[2]["objects"][1]["game"]["questions"][random.randint(0,2)]
    question_displayed = question["question"]      
              
    #Respuestas
    question_answer = question["correct_answer"]
    question_answer2 = question ["answer_2"]
    question_answer3 = question ["answer_3"]
    question_answer4 = question ["answer_4"]
        
    #Interfaz de la pregunta
    show_question_quizizz = f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
       Juguemos al {quizizz.gamename}! 
       ({quizizz.rules}) 
       
       Debes responder a las siguiente pregunta:
                    
            {question_displayed}

              1.  {question_answer}
              2.  {question_answer2}
              3.  {question_answer3}
              4.  {question_answer4}
                  
                    
    |  Si quieres una pista ingresa "p"                                              |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    ------> """

    while True:
            
        #Respuesta del usuario
        answer = input(show_question_quizizz)
        while not answer.isnumeric() or int(answer) not in range(1,5):
            answer = input("\nIngreso Inválido, por favor ingresa una opción válida \n    ------> ")
            
                
        if answer == "1":
                
            inventory.add_obj(quizizz.reward)
                
            print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        EXCELENTE! Respuesta correcta
        
        Has obtenido {quizizz.reward}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)
            break
            
        else:
            print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        WRONG! Respuesta incorrecta
        
        {quizizz.rules}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)
            continue
            

#JUEGOS DEL LABORATORIO

#Función para hacer adivinanza como un objeto
def set_adivinanza():
    gamename = response_json[0]["objects"][2]["game"]["name"]
    reward = response_json[0]["objects"][2]["game"]["award"]
    rules = response_json[0]["objects"][2]["game"]["rules"]
    requirement = response_json[0]["objects"][2]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

#Adivinanza
def adivinanza():
    
    adivinanza = set_adivinanza()
    
    inventory = Inventory()
    
    gamename = response_json[0]["objects"][2]["game"]["name"]
    reward = response_json[0]["objects"][2]["game"]["award"]
    rules = response_json[0]["objects"][2]["game"]["rules"]
    requirement = response_json[0]["objects"][2]["game"]["requirement"]

    #Preguntas
    question = response_json[0]["objects"][2]["game"]["questions"][random.randint(0,2)]
    question_displayed = question["question"]     
              
    #Respuestas
    question_answers = question["answers"]
    
    #Interfaz de la pregunta
    show_question_adivinanza = f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
       Juguemos a las {adivinanza.gamename}! 
       ({adivinanza.rules}) 
       
       Debes responder a la siguiente adivinanza
                    
            {question_displayed}
                                
    |  Si quieres una pista ingresa "p"                                              |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    ------> """
        
    
    while True:
           
        #Respuesta del usuario
        answer = input(show_question_adivinanza)
                 
        if answer in question_answers:
            Inventory.add_obj(inventory, reward)
             
            print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        EXCELENTE! Respuesta correcta
        
        Has obtenido {adivinanza.reward}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)
            
            break 
         
        else:
            
            print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        WRONG! Respuesta incorrecta
        
        {adivinanza.rules}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)
            continue  
          
#Función para hacer la sopa de letras un objeto
def set_alphabet_soup(): 
    
    gamename = response_json[0]["objects"][0]["game"]["name"]
    reward = response_json[0]["objects"][0]["game"]["award"]
    rules = response_json[0]["objects"][0]["game"]["rules"]
    requirement = response_json[0]["objects"][0]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)
    
#Función de la sopa de letras
def alphabet_soup(): 
    
    inventory = Inventory()
    
    soup = set_alphabet_soup()

    #Preguntas
    question = response_json[0]["objects"][0]["game"]["questions"][random.randint(0,2)]
      
       
    question_1 = response_json[0]["objects"][0]["game"]["questions"][0]   
    question_2 = response_json[0]["objects"][0]["game"]["questions"][1]
    question_3 = response_json[0]["objects"][0]["game"]["questions"][2]
                 
    #Respuestas
    question_answers1 = [question_1["answer_1"].lower(), question_1["answer_2"].lower(), question_1["answer_3"].lower()]
    
    question_answers2 = [question_2["answer_1"].lower(), question_2["answer_2"].lower(), question_2["answer_3"].lower()]
    
    question_answers3 = [question_3["answer_1"].lower(), question_3["answer_2"].lower(), question_3["answer_3"].lower()]  
    
    player_answers = []
    
    #Interfaz de la pregunta
    show_question = f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
       Juguemos a la {soup.gamename}! 
       ({soup.rules}) 
                    
       Debes colocar las palabras que encuentres
                                
    |  Si quieres una pista ingresa "p"                                              |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """
        
    
    while True:
        
        if player_answers == question_answers1 or player_answers == question_answers2 or player_answers == question_answers3:
                   
                Inventory.add_obj(inventory, soup.reward)
                
                print(f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            EXCELENTE! Has vencido la sopa de letras!
            
            Has obtenido {soup.reward}               
        |                                                                                |
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
                
                break    
            
        #Si random pickea la pregunta 1
        if question == question_1:
               
            #Respuesta del usuario
            print(show_question)
            answer = input(show_alphabet_soup_q1).lower()
                    
            if answer in question_answers1:
                
                print(space + f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            EXCELENTE! Respuesta correcta               
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
                player_answers.append(answer)
                print(player_answers)
                continue
            
            else:
                
                print(f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            WRONG! Respuesta incorrecta
            
            {soup.rules}               
        |                                                                                |
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
                continue 
               
        # -------------------------------------------------------------------------------------
        #Si random pickea la pregunta 2
        elif question == question_2:
            
            #Respuesta del usuario
            print(show_question)
            answer = input(show_alphabet_soup_q2).lower()
                    
            if answer in question_answers2:
                
                print(space + f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            EXCELENTE! Respuesta correcta               
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
                player_answers.append(answer)
                print(player_answers)
                continue
            else:
                
                print(f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            WRONG! Respuesta incorrecta
            
            {soup.rules}               
        |                                                                                |
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
                continue 
            
        # -------------------------------------------------------------------------------------   
        #Si random pickea la pregunta 3
        elif question == question_3:
            #Respuesta del usuario
            print(show_question)
            answer = input(show_alphabet_soup_q3).lower()
                    
            if answer in question_answers3:
                
                print(space + f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            EXCELENTE! Respuesta correcta               
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
                player_answers.append(answer)
                print(player_answers)
                continue
            else:
                
                print(f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            WRONG! Respuesta incorrecta
            
            {soup.rules}               
        |                                                                                |
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
                continue  
