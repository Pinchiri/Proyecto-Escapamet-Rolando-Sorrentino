space = "\n" * 3

bienvenue = """
    |--------------------------  Bienvenido a Escapamet -----------------------------|
    |                                                                                |
    |                                                                                |
    |                           1. CREAR NUEVO USUARIO                               |
    |                           2. USUARIO EXISTENTE                                 |           
    |                           3. SALIR                                             |
    |                                                                                |
    |                                                                                |   
    |                                                                                |   
    |                                                                                |  
    |                   Escriba el número de la opción que desee                     |           
    |--------------------------------------------------------------------------------|
        
    ------> """

login_user = space + """
    |--------------------------------------------------------------------------------|
    |                                                                                |
    |   Usuario                                                                      |
    |                                                                                |           
    |--------------------------------------------------------------------------------|
    ------> """

login_password = space + """
    |--------------------------------------------------------------------------------|
    |                                                                                |
    |   Contraseña                                                                   |
    |                                                                                |           
    |--------------------------------------------------------------------------------|
    ------> """
    
create_user = """
    |--------------------------------------------------------------------------------|
    |                                                                                |
    |   Escriba su Usuario (Solo letras)                                             |
    |                                                                                |           
    |--------------------------------------------------------------------------------|
    ------> """

create_password = space + """
    |--------------------------------------------------------------------------------|
    |                                                                                |
    |   Escriba su Contraseña (sin caracteres especiales)                            |
    |                                                                                |           
    |--------------------------------------------------------------------------------|
    ------> """

create_age = space + """
    |--------------------------------------------------------------------------------|
    |                                                                                |
    |   Escriba su Edad                                                              |
    |                                                                                |           
    |--------------------------------------------------------------------------------|
    ------> """

create_avatar = space + """
    |--------------------------------------------------------------------------------|
    |                                                                                |
    |   Ingrese el número del avatar que desea                                       |
    |                                                                                |
    |            1. Scharifker                                                       |
    |            2. Eugenio Mendoza                                                  |
    |            3. Pelusa                                                           |
    |            4. Gandhi                                                           |
    |                                                                                |             
    |--------------------------------------------------------------------------------|
    ------> """

create_difficulty = space + """
    |--------------------------------------------------------------------------------|
    |                                                                                |
    |   Ingrese el número de la dificultad en que desea jugar                        |
    |                                                                                |
    |            1. Fácil (120 de vida y 7 pistas)                                   |
    |            2. Normal (100 de vida y 5 pistas)                                  |
    |            3. Peluo  (60 de vida y 3 pistas)                                   |
    |                                                                                |
    |                                                                                |             
    |--------------------------------------------------------------------------------|
    ------> """




plaza_rectorado_image = space + """
    |---------------------------------------------------------------------------------------------------|
    |                    |_      \       __           |    __     |___     _|                           |
    |                      |      \       _\  __/      \_/       _/       |                             |
    |                       \      |      \  /        _|   _____/        /                              |
    |                        |_     \      \/        /    \    __/     _|                               |
    |                          |____/       \___    /____/    /   ____|                                 |
    |                               \______     |  |       ______/                                      |
    |                                      \____|_/_______/                                             |
    |                                          \      /                                                 |
    |                                           |    |                                                  |
    |                                           |    |                                                  |
    |                                           |    |                                                  |
    |                                           |    |                                                  |
    |                                           |    |                                                  |
    |       ____________                        |    |                         ____________             |
    |       | |------| |                      _/      \_                       | |------| |             |
    |_______|_|______|_|_____________________/__________\______________________|_|______|_|_____________|
    |                                                                                                   |          
    |                                                                                                   |   
    |                                    Plaza del Rectorado                                            |
    |---------------------------------------------------------------------------------------------------|
    
    Ingresa
        "l" para ir al banco de la izquierda
        "m" para ir al Samán
        "r" al banco de la derecha
        "f" para moverte a la Biblioteca
        "i" para ver el inventario
    
-------> """
    
biblioteca_image = space + """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                              _______________________________                                      |
    |                              | ___________________________ |                                      |
    |                              ||_|_|\__|_|_|_|_|_|_|_|_|_|_||                                      |
    |                              ||_|_|_|_|_|\__|_|_|_|_|_|_|_||                                      |
    |                              ||_|_|_|_|_|_|_|_|_|_|_|_|_|_||                                      |
    |                              ||_|_|_|_|_|_|_|\__|_|_|_|_|_||                                      |
    |                              ||_|_|_|_|_|_|_|_|_|_|_|_|_|_||                                      |
    |                              ||_|_|_|_|_|_|_|_|_|_|__/|_|_||                                      |
    |                              ||_|_|_|_|_|_|\|_|_|_|_|_|_|_||                                      |
    |                              ||_|_|_|_|_|_|_|_|_|_|_|_|_|_||                                      |
    |       __________             ||_|_|_|_|_|_|_|_|_|_|_|_|_|_||            _________________         |
    |     _| .      . |_           ||_|__/|_|_|_|_|_|_|\__|_|_|_||           |____.___|___.____|        |
    |    |_|_.______._|_|          ||_|_|_|_|_|__/|_|_|_|_|_|_|_||           |____.___|___.____|        |
    |    ||------------||          ||_|_|_|_|_|_|_|_|_|_|_|_|_|_||           |____.___|___.____|        |   
    |____||____________||__________||___________________________||___________|_________________|________|
    |                                                                                                   |          
    |                                                                                                   |   
    |                                        Biblioteca                                                 |
    |---------------------------------------------------------------------------------------------------|
    
    Ingresa
        "l" para ir al mueble de la izquierda
        "m" para ir al estante de libros
        "r" al gabetero de la derecha
        "f" para ir a la Plaza del Rectorado
        "b" para ir a la puerta de los Laboratorios
        "i" para ver el inventario
        
-------> """

pasillo_laboratorio_closed_image = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |         Presiona ENTER para abrir la puerta                                                       |
    |                                                                                                   |
    |                                      ____________________                                         |
    |                                     |         |          |                                        |
    |                                     |         |          |                                        |
    |                                     |         |          |                                        |
    |                                     |         |          |                                        |
    |                                     |         |          |                                        |
    |                                     |         |          |                                        |
    |                                     |    o    |     o    |                                        |
    |                                     |         |          |                                        |
    |                                     |         |          |                                        |
    |                                     |         |          |                                        |
    |                                     |         |          |                                        |   
    |_____________________________________|_________|__________|________________________________________|
    |                                                                                                   |          
    |                                                                                                   |   
    |                                   Puerta de los Laboratorios                                      |
    |---------------------------------------------------------------------------------------------------|
    
    Ingresa
        "b" para ir a la Biblioteca
        "i" para ver el inventario
        
-------> """

pasillo_laboratorio_opened_image = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                          ___________ ____________________ ___________                             |
    |                         |           |                    |           |                            |
    |                         |           |                    |           |                            |
    |                         |           |                    |           |                            |
    |                         |           |                    |           |                            |
    |                         |           |                    |           |                            |
    |                        _|           |                    |           |_                           |
    |                       |_|           |                    |           |_|                          |
    |                         |           |                    |           |                            |
    |                         |           |                    |           |                            |
    |                         |           |                    |           |                            |
    |                         |           |                    |           |                            |   
    |_________________________|___________|____________________|___________|____________________________|
    |                                                                                                   |          
    |                                                                                                   |   
    |                                   Puerta de los Laboratorios                                      |
    |---------------------------------------------------------------------------------------------------|
    
    Ingresa
        "f" para ir al Laboratorio
        "b" para ir a la Biblioteca
        "i" para ver el inventario
        
-------> """

laboratorio_image = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                               __________________________________                                  |
    |                               ||------------------------------||                                  |
    |                               ||                              ||                                  |
    |                               ||         A X E M N E          ||                                  |
    |                               ||         G H J I S A          ||                                  |
    |        ________               ||         A D F G E G          ||              ________            |
    |       |        |              ||______________________________||             |        |           |
    |       |________|              ----------------------------------             |________|           |
    |      _____||_____                                                           _____||_____          |
    |      |__________|                                                           |__________|          |
    |      ||        ||                                                           ||        ||          |   
    |_____ ||________||___________________________________________________________||________||__________|
    |                                                                                                   |          
    |                                                                                                   |   
    |                                         Laboratorio                                               |
    |---------------------------------------------------------------------------------------------------|
    
    Ingresa
        "l" para ir a la computadora de la izquierda
        "m" para ir a la pizarra
        "r" para ir a la computadora de la derecha
        "f" para ir al Cuarto de Servidores
        "b" para ir a la Puerta de Laboratorios
        "i" para ver el inventario
        
-------> """

servidores_image = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |       _______________               ____________________                                          |
    |      |      ||       |             |         |          |                                         |
    |      |______||_______|             |         |          |                                         |
    |      |      ||       |             |         |          |                                         |
    |      |______||_______|             |         |          |                                         |
    |      |      ||       |             |         |          |                  ______                 |
    |      |______||_______|             |         |          |                 | \__/ |                |
    |      |      ||       |             |    o    |     o    |                 |------|                |
    |      |______||_______|             |         |          |                 |      |                |
    |      |      ||       |             |         |          |                 |      |                |
    |      |______||_______|             |         |          |                 |      |                |
    |      ||             ||             |         |          |                 |      |                |   
    |______||_____________||_____________|_________|__________|_________________|______|________________|
    |                                                                                                   |          
    |                                                                                                   |   
    |                                     Cuarto de Servidores                                          |
    |---------------------------------------------------------------------------------------------------|
    
    Ingresa
        "l" para ir a la estantería
        "m" para ir a la puerta final
        "r" para ir al pote de basura 
        "b" para ir al Laboratorio
        "i" para ver el inventario
        
-------> """

template = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |   
    |___________________________________________________________________________________________________|
    |                                                                                                   |          
    |                                                                                                   |   
    |                             Estas en                                        |
    |---------------------------------------------------------------------------------------------------|
    """

show_alphabet_soup_q1 = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                                                                                                   |
    |                                 A V X S C H A R I F K E R M X                                     |
    |                                 T A O H P X K Ñ Q A Y H M A L                                     |
    |                                 D E S S K W G H J A E B L X Z                                     |
    |                                 H O E S M H A F R W R K S D E                                     |
    |                                 F L C B A G H Y U K K E R M X                                     |
    |                                 Z Ñ J G F L A K F Z W R M N O                                     |
    |                                 A Z L S L Z B R I F J E N O Ñ                                     |
    |                                 B Q O K I X A J D K O P B P L                                     |
    |                                 Y S P Ñ U C S R K I Z I V Q K                                     |
    |                                 E Y Q A Y V D O D Y L L C R J                                     |
    |                                 K M R W T B F P J Z S A X S H                                     |
    |                                 Q N S Q E N G Q H X B R Z I G                                     |
    |                                 A Z T Z Q M H S G F S E R G F                                     |   
    |                                                                                                   |
    |                                                                                                   |          
    |                                                                                                   |   
    |                                                                                                   |
    |---------------------------------------------------------------------------------------------------|
    
   -------> """

    
show_alphabet_soup_q2 = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                                                                                                   |
    |                                 A V X S C A D X R Q K E R M X                                     |
    |                                 T A S H P X K Ñ Q A Y H M A L                                     |
    |                                 D E O S K W G H J A E B L X Z                                     |
    |                                 H O N S M H A F R W R K S D E                                     |
    |                                 F L A B A G H Y U K K E R M X                                     |
    |                                 Z Ñ C G F L A K F Z W R O N O                                     |
    |                                 A Z R S L Z B R I F J L N O Ñ                                     |
    |                                 B Q A K I X A J D K L X B P L                                     |
    |                                 Y S M Ñ U C S R K E Z S V Q K                                     |
    |                                 E Y Q A Y V D O B Y K A C R J                                     |
    |                                 K M R W T B F P J Z S C X S H                                     |
    |                                 Q N S Q E N G Q H X B R Z I G                                     |
    |                                 A Z T Z Q M H S D A G A M A F                                     |   
    |                                                                                                   |
    |                                                                                                   |          
    |                                                                                                   |   
    |                                                                                                   |
    |---------------------------------------------------------------------------------------------------|
    
   -------> """  

show_alphabet_soup_q3 = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                                                                                                   |
    |                                 A V X S C H X A K F J Q R M X                                     |
    |                                 T A O H P X K Ñ Q A Y H M A L                                     |
    |                                 D E S S K W B H J A E B L X Z                                     |
    |                                 H O E S M H A O R W R K S D X                                     |
    |                                 F L C B A G H Y A K K E R M E                                     |
    |                                 Z Ñ J G F L X K F D W R M N T                                     |
    |                                 A Z L S L Z B J I F A E N O N                                     |
    |                                 B Q O K I X A J D K O Y B P A                                     |
    |                                 Y S P Ñ U C S R K I Z Z V Q R                                     |
    |                                 E Y Q S Y V D O D Y K X C R O                                     |
    |                                 K M D A G A M A J Z S B X S L                                     |
    |                                 Q N S Q E N G Q H X B R Z I L                                     |
    |                                 A Z T Z Q M H S G F S E R G F                                     |   
    |                                                                                                   |
    |                                                                                                   |          
    |                                                                                                   |   
    |                                                                                                   |
    |---------------------------------------------------------------------------------------------------|
    
   -------> """

criptograma_1 = """
    |--------------------------------------------------------------------------------|
    |    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z                         |
    |                           ||
    |    Y Z A B C D E F G H I J K L M N O P Q R S T U V W X                         |           
    |--------------------------------------------------------------------------------|
    """

criptograma_2 = """
    |--------------------------------------------------------------------------------|
    |    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z                         |
    |                           ||
    |    W X Y Z A B C D E F G H I J K L M N O P Q R S T U V                         |           
    |--------------------------------------------------------------------------------|
    """
    
criptograma_3 = """
    |--------------------------------------------------------------------------------|
    |    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z                         |
    |                           ||
    |    V W X Y Z A B C D E F G H I J K L M N O P Q R S T U                         |           
    |--------------------------------------------------------------------------------|
    """

final_image = """
    |---------------------------------------------------------------------------------------------------|
    |                                                                                                   |
    |                                                                                                   |
    |                                                                                                   |
    |                       1. ROJO                                2. AZUL                              |
    |                   ___________________                    ___________________                      |
    |                  |                   |                  |                   |                     |
    |                  |       ____        |                  |       ____        |                     | 
    |                  |      /    \       |                  |      /    \       |                     |
    |                  |     |      |      |                  |     |      |      |                     |
    |                  |     |      |      |                  |     |      |      |                     |
    |                  |      \____/       |                  |      \____/       |                     |
    |                  |                   |                  |                   |                     |
    |                  |___________________|                  |___________________|                     |
    |                                                                                                   |
    |                                                                                                   |   
    |                                                                                                   |
    |                                                                                                   |          
    |                                                                                                   |   
    |                                                                                                   |
    |---------------------------------------------------------------------------------------------------|
    
    ------> """