#Importación de librerías
from Player import * 
from images import * 
import requests
from Room import *
import random  
from games import *


def register_players(username): # Función de registro
    
    age = input(create_age)
    while not age.isnumeric() or int(age) < 1:
        age = input("Ingreso inválido. Intente de nuevo: \n    ----> ")

    password = input(create_password)
    while not password.isalnum():
        password = input("Ingreso inválido. Intente de nuevo: \n    ----> ")


    avatar = input(create_avatar)
    
    while not avatar.isnumeric() or int(avatar) not in range(1, 5):
        avatar = input("Ingreso inválido. Intente de nuevo: \n    ----> ")
    
    if avatar == "1":
        avatar = "Scharifker"

    elif avatar == "2":
        avatar = "Eugenio Mendoza"

    elif avatar == "3":
        avatar = "Pelusa"

    elif avatar == "4":
        avatar = "Gandhi"
    
    player = Player(username, password, age, avatar)
    
    with open("/home/pinchiri/UNIMET/Algoritmos_y_Programacion/Proyecto/Proyecto-Escapamet-Rolando-Sorrentino/Players_Database.txt","a+") as dbe:
        dbe.write(f"{player.username}//{player.password}//{player.age}//{player.avatar}\n")

    print("\nJugador registrado con éxito.")
    return player
    

def players_verification():  #Función de registro y verificación de usuarios repetidos
    
    username = input(create_user)
    while not username.isalpha():
        username = input("Ingreso Inválido. Intente de nuevo: \n    ----> ")
    

    try:
        with open("/home/pinchiri/UNIMET/Algoritmos_y_Programacion/Proyecto/Proyecto-Escapamet-Rolando-Sorrentino/Players_Database.txt") as dbe:
            datos = dbe.readlines()
        for dato in datos:
            players_l = dato[:-1].split("//")
            if players_l[0] == username:
                print("\nJugador ya registrado.")
                player = Player(players_l[0],players_l[1],players_l[2],players_l[3])
                return player
        else:
            return register_players(username)
    except FileNotFoundError:
        print("\nTodavía no hay ningún jugador registrado.\n")
        return register_players(username)  

def login(): #Función para loggearse como usuario existente
    try:
        username = input(login_user)
        while not username.isalpha():
            username = input("Ingreso Inválido. Intente de nuevo: \n    ----> ")
    
        with open("/home/pinchiri/UNIMET/Algoritmos_y_Programacion/Proyecto/Proyecto-Escapamet-Rolando-Sorrentino/Players_Database.txt") as dbe:
            datos = dbe.readlines()
            for dato in datos:
                players_l = dato[:-1].split("//")
                if players_l[0] == username:
                    
                    password = input(login_password)
                    while not password.isalnum():
                        password = input("Contraseña inválida. Intente de nuevo: \n    ----> ")
                    
                    while True:
                        if password == players_l[1]:
                            print("Ingreso exitoso")
                            player = Player(players_l[0],players_l[1],players_l[2],players_l[3])
                            return player
                            
                        else:
                            while True:
                                invalid_pass = input("""Contraseña inválida, qué desea hacer? 
                                                            
                                1. Crear un nuevo usuario
                                2. Volver a intentar el ingreso
                                                                
                            ------> """)
                                        
                                if invalid_pass == "1":
                                    return players_verification()
                                        
                                elif invalid_pass == "2":
                                    return login()
                                
                                else:
                                    print("Ingreso Inválido")
                            
                else:
                    while True:            
                        invalid = input("""Usuario inválido, qué desea hacer? 
                                                            
                                1. Crear un nuevo usuario
                                2. Volver a intentar el ingreso
                                                                
                            ------> """)
                                        
                        if invalid == "1":
                            return players_verification()
                                        
                        elif invalid == "2":
                            return login()
                                
                        else:
                            print("Ingreso Inválido")
                    
                        
    except FileNotFoundError:
        print("\nTodavía no hay ningún jugador registrado.\n")
        return players_verification()

#Función para elegir la dificultad
def set_difficulty():
    
    while True:
        
        difficulty = input(create_difficulty) #Escoger la dificultad
        player_difficulty = ""     
            
        while not difficulty.isnumeric() or int(difficulty) not in range(1, 4):
            difficulty = input("Ingreso Inválido. Intente de nuevo: \n    ----> ")
                
        if difficulty == "1":
            player_difficulty == "Fácil"
            PlayerStats.difficulty = "Fácil"
            print(f"Has elegido la dificultad {PlayerStats.difficulty}!")
            return player_difficulty
                        
        elif difficulty == "2":
            player_difficulty == "Normal"
            PlayerStats.difficulty = "Normal"
            print(f"Has elegido la dificultad {PlayerStats.difficulty}!")
            return player_difficulty
                
                        
        elif difficulty == "3":
            player_difficulty == "Peluo"
            PlayerStats.difficulty = "Peluo"
            print(f"Has elegido la dificultad {PlayerStats.difficulty}! ojo pelao")
            return player_difficulty
                
                
        elif difficulty == "4":
            player_difficulty == "Sandbox"
            return player_difficulty
                
                
        else:
            print("\nIngreso Inválido\n")
            continue
                
                
def game_start(difficulty, player):
    
    while True:
            
        time = "x"
        clues = 0
        
        if difficulty == "Fácil":
            player.life = 120
            clues = 7
            time = "no se"
        
        elif difficulty == "Normal":
            player.life = 100
            clues = 5
            time = "no se"
        
        elif difficulty == "Peluo":
            player.life = 60
            clues = 3
            time = "no se"
        
        elif difficulty == "Sandbox":
            player.life = 1000
            clues = 1000
            time = "infinito"
        
        initial_narrative = f"""
        |---------------------------------------------------------------------------------------------------|
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                    
                Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena (esto no es novedad),           
            lo que sí es novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes       
                    que tiene toda la información de SAP de estudiantes, pagos y  asignaturas.               
        |                                                                                                   |
        |                                                                                                   |
                Necesitamos que nos ayudes a recuperar el disco, para eso tienes {time} minutos           
                        antes de que el servidor se caiga y no se pueda hacer más nada.                    
                                            ¿Aceptas el reto?                                            
                                                    (S/N)                                                  
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |   
        |                                                                                                   |
        |                                                                                                   |          
        |                                                                                                   |   
        |                                                                                                   |
        |---------------------------------------------------------------------------------------------------|

        ------> """
        
        choice = input(initial_narrative).lower()
        
        if choice == "s":
            
            bienvenue_avatar = space + f"""
        |---------------------------------------------------------------------------------------------------|
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |
        Bienvenido {player.avatar}, gracias por tu disposición a ayudarnos a resolver este inconveniente,   
                        te encuentras actualmente ubicado en la biblioteca                                 
                    Recuerda que el tiempo corre más rápido que un trimestre en este reto.                   
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |
        |                                                                                                   |   
        |                                                                                                   |
        |                                                                                                   |          
        |      Presiona ENTER para continuar                                                                |   
        |                                                                                                   |
        |---------------------------------------------------------------------------------------------------|

        ------> """
            enter = input(bienvenue_avatar)
            
            while len(enter) > 0:
                enter = input(bienvenue_avatar)
            return PlayerStats(difficulty, clues)
  
            
            
        elif choice == "n":
            print("\n  \n             Pa que estas aquí entonces")
            continue
        
        else:
            print("Ingreso Inválido")
            continue
 

#Funciones para hacer los cuartos objetos

def set_biblioteca():
    
    left = response_json[1]["objects"][1]
    middle = response_json[1]["objects"][0]
    right = response_json[1]["objects"][2]
    
    return Room(left, middle, right)

biblioteca = set_biblioteca()

def set_rectorado():
    
    left = response_json[2]["objects"][1]
    middle = response_json[2]["objects"][0]
    right = response_json[2]["objects"][2]

    return Room(left, middle, right)

rectorado = set_rectorado()
   
def set_laboratorio():
    
    left = response_json[0]["objects"][1]
    middle = response_json[0]["objects"][0]
    right = response_json[0]["objects"][2]

    return Room(left, middle, right)  

laboratorio = set_laboratorio()  

def set_servidores():
    
    left = response_json[4]["objects"][1]
    middle = response_json[4]["objects"][0]
    right = response_json[4]["objects"][2]

    return Room(left, middle, right)

servidores = set_servidores()

def set_pasillo_laboratorio():
    
    left = None
    middle = response_json[0]["objects"][0]
    right = None

    return Room(left, middle, right)

pasillo_laboratorio = set_pasillo_laboratorio() 
    