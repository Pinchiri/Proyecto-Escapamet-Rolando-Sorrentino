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

saman = set_saman_game()

#Juego Samán
def saman_game(inventory):
     
    while True:   
        
                
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

quizizz = set_quizizz()   

def quizizz_game(inventory):
        
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
        
#Creando juego de memoria como un objeto

def set_memory():
    
    gamename = response_json[2]["objects"][2]["game"]["name"]
    reward = response_json[2]["objects"][2]["game"]["award"]
    rules = response_json[2]["objects"][2]["game"]["rules"]
    requirement = response_json[2]["objects"][2]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

memory = set_memory()

def memory_game(inventory):

    inventory.add_obj(memory.reward)
    
    print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        EXCELENTE! Has vencido la memoria!
        
        Has obtenido {memory.reward}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)
    

#JUEGOS BIBLIOTECA

#Creando el juego de derivada como un objeto
def set_derivada():
    
    gamename = response_json[1]["objects"][1]["game"]["name"]
    reward = response_json[1]["objects"][1]["game"]["award"]
    rules = response_json[1]["objects"][1]["game"]["rules"]
    requirement = response_json[1]["objects"][1]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

derivada = set_derivada()

#Juego cálculo de derivada
def derivada_game(inventory):
    
    inventory.add_obj(derivada.reward)
    
    print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        EXCELENTE! Respuesta correcta!
        
        Has obtenido {derivada.reward}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)

#Creando criptograma como un objeto    
def set_cryptogram():
    
    gamename = response_json[1]["objects"][2]["game"]["name"]
    reward = response_json[1]["objects"][2]["game"]["award"]
    rules = response_json[1]["objects"][2]["game"]["rules"]
    requirement = response_json[1]["objects"][2]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

cryptogram = set_cryptogram()

def cryptogram_game(inventory):
    
    question = response_json[1]["objects"][2]["game"]["questions"][random.randint(0,2)]
    question_answer = question["question"]
    
    question_1 = response_json[1]["objects"][2]["game"]["questions"][0]["question"]   
    question_2 = response_json[1]["objects"][2]["game"]["questions"][1]["question"]
    question_3 = response_json[1]["objects"][2]["game"]["questions"][2]["question"]
    
    show_question = f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        Juguemos al {cryptogram.gamename}! 
        ({cryptogram.rules}),   
                 
                               
                    
    |  Si quieres una pista ingresa "p"                                              |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    ------> """
    
    inventory.add_obj(saman.requirement[1])
    
#Creando ahorcado como un objeto    
def set_ahorcado():
    
    gamename = response_json[1]["objects"][0]["game"]["name"]
    reward = response_json[1]["objects"][0]["game"]["award"]
    rules = response_json[1]["objects"][0]["game"]["rules"]
    requirement = response_json[1]["objects"][0]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

ahorcado = set_ahorcado()

#Juego Ahorcado
def ahorcado_func(question_answer):
    
    word = []
    hidden = []
    
    for l in question_answer:
        word.append(l)
        hidden.append("_")
    
    while True:
        
        if "_" in hidden:
            
            player_answer = input("""
    |--------------------------------------------------------------------------------|
        Ingresa una letra                                              
    |--------------------------------------------------------------------------------|
    -------> """)
            
            if player_answer in word:
                print("""
    |--------------------------------------------------------------------------------|
        EXCELENTE! letra correcta
    |--------------------------------------------------------------------------------|
    """)
                for i, l in enumerate(word):
                    if player_answer == l:
                        hidden[i] = player_answer
                        print(f"""
    |--------------------------------------------------------------------------------|
        {hidden}
    |--------------------------------------------------------------------------------|
    """)
            else:
                print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        WRONG! letra incorrecta
        
        {ahorcado.rules}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)         
        else:
            print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        EXCELENTE! Has vencido al {ahorcado.gamename}
        
        Has obtenido {ahorcado.reward}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)  
            inventory.add_obj(ahorcado.reward)
            break    
                
    
def ahorcado_game(inventory):
    
    question = response_json[1]["objects"][0]["game"]["questions"][random.randint(0,2)]
    question_displayed = question["question"]
    question_answer = question["answer"]
    question_1 = response_json[1]["objects"][0]["game"]["questions"][0]["question"]   
    question_2 = response_json[1]["objects"][0]["game"]["questions"][1]["question"]
    question_3 = response_json[1]["objects"][0]["game"]["questions"][2]["question"]
        
    show_question = f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        Juguemos al {ahorcado.gamename}! 
        ({ahorcado.rules}),  
        La primera letra de la palabra es en mayúsculas! 
                 
                    {question_displayed}           
                    
    |  Si quieres una pista ingresa "p"                                              |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    ------> """
    
    print(show_question)
    
    ahorcado_func(question_answer)
       

            

#JUEGOS DEL LABORATORIO

#Función para hacer adivinanza como un objeto
def set_adivinanza():
    gamename = response_json[0]["objects"][2]["game"]["name"]
    reward = response_json[0]["objects"][2]["game"]["award"]
    rules = response_json[0]["objects"][2]["game"]["rules"]
    requirement = response_json[0]["objects"][2]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

adivinanza = set_adivinanza()

#Adivinanza
def adivinanza_game(inventory):
    
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

soup = set_alphabet_soup()
   
#Función de la sopa de letras
def alphabet_soup(inventory): 

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
            
            elif answer == "s":
                inventory.add_obj(soup.reward)
                break
            
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
            
            elif answer == "s":
                inventory.add_obj(soup.reward)
                break
            
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
            
            elif answer == "s":
                inventory.add_obj(soup.reward)
                break
            
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
    
    
#Creando el juego preguntas python como objeto
def set_python_game():
        
    gamename = response_json[0]["objects"][1]["game"]["name"]
    reward = response_json[0]["objects"][1]["game"]["award"]
    rules = response_json[0]["objects"][1]["game"]["rules"]
    requirement = response_json[0]["objects"][1]["game"]["requirement"]
        
    return Game(gamename, reward, rules, requirement)

python_g = set_python_game()
    
#Juego preguntas python
def python_game(inventory):
        
    inventory.add_obj(python_g.reward)
    print(f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
        EXCELENTE! Has vencido al {python_g.gamename}
        
        Has obtenido {python_g.reward}               
    |                                                                                |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    """)
        
        
                  

#JUEGO PASILLO LABORATORIO

def set_boolean_logic():
    
    gamename = response_json[3]["objects"][0]["game"]["name"]
    reward = response_json[3]["objects"][0]["game"]["award"]
    rules = response_json[3]["objects"][0]["game"]["rules"]
    requirement = response_json[3]["objects"][0]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

door_hallway = set_boolean_logic()

#Juego Lógica Booleana
def boolean_logic(inventory):
    
    #Preguntas
    question = response_json[3]["objects"][0]["game"]["questions"][random.randint(0,1)]
    question_displayed = question["question"]
  
    #Respuestas
    question_answer = question["answer"].lower()
                 
    show_question = f"""    
    |--------------------------------------------------------------------------------|
    |                                                                                |
       Juguemos a la {door_hallway.gamename}! 
       ({door_hallway.rules}) 
                    
        Responde la siguiente pregunta:

                {question_displayed}
                                
    |  Si quieres una pista ingresa "p"                                              |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    ------> """
    
    while True:
        
        answer = input(show_question).lower()
        
        if answer == question_answer:
            
            inventory.add_obj(door_hallway.reward)
                    
            print(f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            EXCELENTE! Respuesta correcta!
            
            Has obtenido {door_hallway.reward}               
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
            
            {door_hallway.rules}               
        |                                                                                |
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
            continue
        
#JUEGOS SERVIDORES

#Creando juego final un objeto
def set_final_game():
    
    gamename = response_json[4]["objects"][0]["game"]["name"]
    reward = response_json[4]["objects"][0]["game"]["award"]
    rules = response_json[4]["objects"][0]["game"]["rules"]
    requirement = response_json[4]["objects"][0]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

final = set_final_game()

def final_game(inventory):
    
    answers = ["1", "2"]
    answer = random.choice(answers)
    
    while True:
        
        player_answer = input(final_image)
        
        if player_answer == answer:
            
            print(f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            FELICIDADES! HAS COMPLETADO EL DESAFÍO!
            
            Muchas gracias {player.avatar} por salvar a la Universidad 
            una vez más            
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
            Inténtalo de nuevo          
        |                                                                                |
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """) 
           break
        
    

#Creando juego de escoger un numero random como objeto  
def set_choose_num():
    
    gamename = response_json[4]["objects"][2]["game"]["name"]
    reward = response_json[4]["objects"][2]["game"]["award"]
    rules = response_json[4]["objects"][2]["game"]["rules"]
    requirement = response_json[4]["objects"][2]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

choose_num = set_choose_num()

#Juego de escoger un numero random de python
def choose_num_game(inventory):
    
    answer = random.randint(1, 15)
    
    show_question = f"""
    |--------------------------------------------------------------------------------|
    |                                                                                |
       Juguemos a la {choose_num.gamename}! 
       ({choose_num.rules}) 
       
       Ingresa un número del 1 al 15
                                
    |  Si quieres una pista ingresa "p"                                              |
    |                                                                                |
    |--------------------------------------------------------------------------------|
    ------> """
    while True:
        
        player_answer = input(show_question)
        
        if int(player_answer) == answer:

            inventory.add_obj(saman.requirement[0])
        
            print(f"""
        |--------------------------------------------------------------------------------|
        |                                                                                |
            EXCELENTE! Respuesta correcta!
            
            Has obtenido {saman.requirement[0]}               
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
            
            {choose_num.rules}               
        |                                                                                |
        |                                                                                |
        |--------------------------------------------------------------------------------|
        """)
            continue   

#Creando palabraz mezcladas como un objeto
def set_scrabble():
    
    gamename = response_json[4]["objects"][1]["game"]["name"]
    reward = response_json[4]["objects"][1]["game"]["award"]
    rules = response_json[4]["objects"][1]["game"]["rules"]
    requirement = response_json[4]["objects"][1]["game"]["requirement"]
    
    return Game(gamename, reward, rules, requirement)

scrabble = set_scrabble()

def scrabble_game(inventory):
    
    inventory.add_obj(scrabble.reward)
    
    print(f"""
|--------------------------------------------------------------------------------|
|                                                                                |
    EXCELENTE! Respuesta correcta!
    
    Has obtenido {scrabble.reward}               
|                                                                                |
|                                                                                |
|--------------------------------------------------------------------------------|
""")
    