class Player(): #Clase jugador
    
    def __init__(self, username, password, age, avatar, life = 100):
        
        self.username = username
        self.pasword = password
        self.age = age
        self.avatar = avatar 
        self.life = 100
    
    def life_substraction(self, life_to_substract):
        
        life = player.life - life_to_substract
        print(life)
    
    def show_player_info(self): # Función para mostrar la info del jugador
        
        show_info = f"""
            |--------------------------------------------------------------------------------|
            |                                                                                |
            |                                                                                |
                Nombre de usuario -> {self.username}                                         
                Edad --------------> {self.age}                                              
                Avatar ------------> {self.avatar}                                           
            |                                                                                | 
            |                                                                                |
            |                                                                                |             
            |--------------------------------------------------------------------------------|
                """
        return print(show_info)

