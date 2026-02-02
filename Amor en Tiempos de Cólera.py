import random
import time

def enter():
    while True:
        try:
            tecla = input("Presione ENTER para continuar...")
            if tecla != '':
                print("Debes presionar solamente ENTER.")
                continue
            return
        except ValueError:
            print("Ocurrió un error inesperado.")

inventario = [["Pescado podrido", 2], ["Huevo", 1]]
talentos = [["Fuerza", 0], ["Ingenio", 0], ["Inteligencia", 0], ["Detallismo", 0], ["Rebeldía", 0],
            ["Sentido del humor", 0], ["Empatía", 0], ["Confianza", 0], ["Sarcasmo", 0], ["Ego", 0],
            ["Sensibilidad", 0], ["Controlador/a", 0]]

def ensenartalentos(talentos):
    print(f"\n--- HABILIDADES ACTUALES ---")
    if not talentos:
        print("No hay habilidades registradas.")
    else:
        for nombre, valor in talentos:
            print(f"{nombre}: {valor}")
    print("----------------------------")

def introduccion():
    nombrejugador = input("Introduzca su nombre :) : ")
    print(f"\n Bienvenido {nombrejugador}. Lamento contarte que has vivido un accidente de avión.\n")
    enter()
    print("\n Aún recuerdas los gritos de las personas al estar cayéndose el avión, el temblor de los asientos y el instante en que  solo se veía un profundo destello de luz y un irritante pitido.\n")
    enter()
    print("\n Cuando te despertaste, ya estabas en la orilla de una isla desierta, herido, confundido… pero vivo.\n")
    enter()
    print("\n Junto a ti, cuatro personas más habían logrado sobrevivir.\n")
    enter()
    print("""                                                                                                                   
                                                    #%%%        
             *%%%          %%%:        =.           *%%%        
             *%%#          %%%%       %%%+           #%%        
             -%%          -%%%%%     *%%%#         +%%%%%+      
          .*%%%%%*      -*%%%%%%%    %%%%%       #%%%%%%%%%%    
         %%%%%%%%%%%    %%%%%%%%%   %%%%%%%%    *%%%%%%%%%%%    
         %%%%%%%%%%%-  :%%%%%%%%%% @%%%%%%%%:   %%%%%%%%%%%%    
         %%%%%%%%%%%+  +%%%%%%%%%% %%%%%%%%%=   %%%%%%%%%%%%:   
        +%*%%%%%%%:%+  +%%%%%%%*#%:=%%%%%%%%%   %%%%%%%%%##%%   
        =%=%%%%%%%+%*   %%%%%%%%*%  %%%%%%%+*=  %%%%%%%%%= %%   
         +*%%%%%%%##+   *%%%%%%%%-  #%%%%%%# %  =%%%%%%%%% +%   
         %%%%%%%%%# +   %%%%%%%%%%  :%%%%%%* #   #%%%%%%%%**#   
         +:%%%%%%%%=*    %%%%%%%%   -%%%%%%% #    %%%%%%%%#     
            %%%%%%*      %%%%%%%%   :%%%=%%*      .%%% %%%#     
            #%%%%%        :%%%%*     %%% %%        %%. =%%*     
            #%%%%%         %%%%=     %%+ %%        %%   %%#     
             %%%%#         %%%%*     %%  %%       +%%   =%%     
             #%%%%         =%%%*     %%  #%-      #%%    %%-    
             :%%%%          %-%=      %. *%       +%+    %%#    
              %%%#          % #:      %% #%       =%:    .%%    
             #%%%%          %%#=      %% *%       +%      %%    
                %%                                        %%%   
          """)
    enter()
    print("\n Han pasado dos meses desde el accidente.\n")
    enter()
    print("\n Dos meses de calor, hambre y miedo, que hacia que cada día fuese interminable.\n")
    enter()
    print("\n Y ahora, sin darte cuenta, empiezas a mirarlos de otra manera: con una mirada que busca algo más que una simple amistad.\n")
    enter()
    print("\n Quizá cariño… quizá amor… quizá algo que vaya más allá de sobrevivir.\n")
    enter()
    print("\n Porque en esta isla, dejas tu pasado atrás, y tus sentimientos han comenzado a florecer.\n")
    enter()
    return nombrejugador
nombrejugador = introduccion()
equipo=[]
def enseñarequipo(equipo):
    print(f"\nEste es el Equipo que actualmente tienes.\n")
    for i in equipo:
        print(f"{i[0]}: {i[1]}")
    return equipo


def introahabilidades(talentos):
    print(f"\nPara comenzar es importante saber que tienes que tener caracteristicas para sobrevivir en esta isla desierta.\n")
    print(f"Estas son tus habilidades actuales:")
    for i in talentos:
        print(f"{i[0]}: {i[1]}")
    print(f"\nEmpiezas sin ninguna porque tu vida no era muy interesante antes del choque.\n")
    print(f"\nA cada uno de tus compañeros de isla le agradan tres de estas habilidades.\n")
    enter()
    print(f"\nPara lograr conseguir una cita con quien desees debes tener un alto nivel en las tres habilidades que le gustan a tu paramor.\n")
    enter()
    print(f"\nPara conseguir subir tus habilidades debes de elegir las opciones que se alineen con la habilidad que deseas subir.\n")
introahabilidades(talentos)

def abreinventario(inventario):
    input("Presiona ENTER para abrir tu inventario...")
    for i in inventario:
        print(f"{i[0]}: {i[1]}")
#abreinventario(inventario)

def tirardado():
    print("\n🎲 Tirando el dado...")
    enter()
    print("""
                            .%@@@%.                          
                        .%@@@@@@@@@@@@#.                     
                    %@@@@@@@@@@@@@@@@@@@@@@@#                
                *@@@@@@@@@@@         %@@@@@@@@@@@=           
            :%   -%@@@@@@@@@@@@*+*%@@@@@@@@@@@#   %@@%       
            @@@@@%-   .%@@@@@@@@@@@@@@@@@%   .*@@@@@@@       
            @@@@@@@@@@%.   +%@@@@@@@@*   .@@@@@@%%@@@@       
            @@@@@@@@@@@@@@@+    :    =%@@@@@@@%    @@@       
            @@@@@@@@@@@@@@@@@@@+  @@@@@@@@@@@@.    @@@       
            @@@@@@@@+  %@@@@@@@@ +@@@@*#@@@@@@-   @@@@       
            @@@@@@@@    %@@@@@@@ +@@-    @@@@@@@@@@@@@       
            @@@@@@@@:   *@@@@@@@ +@@    .@@@@@@@@@@@@@       
            @@@@@@@@@- :@@@@@@@@ +@@=  -@@@@@@@@@@@@@@       
            @@@@@@@@@@@@@@@@@@@@ +@@@@@@@@@@@@@@@@@@@@       
            @@@@@@@@   .@@@@@@@@ +@@@@@@@@@@@@#   =@@@       
            @@@@@@@@    #@@@@@@@ +@@@@@@@@@@@@    .@@@       
            @@@@@@@@+   #@@@@@@@ =@@@@%@@@@@@@.   @@@@       
            #@@@@@@@@@@@@@@@@@@@ =@@+    @@@@@@@@@@@@%       
               +@@@@@@@@@@@@@@@@ =@@     @@@@@@@@@@=         
                   -@@@@@@@@@@@@ =@@.  .@@@@@@@*             
                       +@@@@@@@@ =@@@@@@@@@@=                
                           -%@@@ =@@@@@@*                    
                               + =@@@+                       
    """)
    time.sleep(1)
    dado = random.randint(1, 10)
    print(f"Resultado: [{dado}]")
    return dado

def tirardado1al20():
    print("\n🎲 Tirando el dado...")
    enter()
    print("""
                            .%@@@%.                          
                        .%@@@@@@@@@@@@#.                     
                    %@@@@@@@@@@@@@@@@@@@@@@@#                
                *@@@@@@@@@@@         %@@@@@@@@@@@=           
            :%   -%@@@@@@@@@@@@*+*%@@@@@@@@@@@#   %@@%       
            @@@@@%-   .%@@@@@@@@@@@@@@@@@%   .*@@@@@@@       
            @@@@@@@@@@%.   +%@@@@@@@@*   .@@@@@@%%@@@@       
            @@@@@@@@@@@@@@@+    :    =%@@@@@@@%    @@@       
            @@@@@@@@@@@@@@@@@@@+  @@@@@@@@@@@@.    @@@       
            @@@@@@@@+  %@@@@@@@@ +@@@@*#@@@@@@-   @@@@       
            @@@@@@@@    %@@@@@@@ +@@-    @@@@@@@@@@@@@       
            @@@@@@@@:   *@@@@@@@ +@@    .@@@@@@@@@@@@@       
            @@@@@@@@@- :@@@@@@@@ +@@=  -@@@@@@@@@@@@@@       
            @@@@@@@@@@@@@@@@@@@@ +@@@@@@@@@@@@@@@@@@@@       
            @@@@@@@@   .@@@@@@@@ +@@@@@@@@@@@@#   =@@@       
            @@@@@@@@    #@@@@@@@ +@@@@@@@@@@@@    .@@@       
            @@@@@@@@+   #@@@@@@@ =@@@@%@@@@@@@.   @@@@       
            #@@@@@@@@@@@@@@@@@@@ =@@+    @@@@@@@@@@@@%       
               +@@@@@@@@@@@@@@@@ =@@     @@@@@@@@@@=         
                   -@@@@@@@@@@@@ =@@.  .@@@@@@@*             
                       +@@@@@@@@ =@@@@@@@@@@=                
                           -%@@@ =@@@@@@*                    
                               + =@@@+                       
    """)
    time.sleep(1)
    dado = random.randint(1, 20)
    print(f"Resultado: [{dado}]")
    return dado

def minijuegoparoimpar(recompensa_elegida):
    print("\n🌀 DESAFÍO DE PROFUNDIDAD (Par o Impar) 🌀")
    print("El remolino va a liberar un número aleatorio de burbujas (entre 1 y 10). Adivina si el número será Par o Impar.")

    while True:
        eleccion = input("Elige 'P' (Par) o 'I' (Impar): ").upper()
        if eleccion in ['P', 'I']:
            break
        else:
            print("Opción no válida. Por favor, elige 'P' o 'I'.")

    numero_mar = random.randint(1, 10)
    es_par = (numero_mar % 2 == 0)
    resultado_mar = 'P' if es_par else 'I'

    print(f"\nEl remolino arroja {numero_mar} burbujas.")

    if eleccion == resultado_mar:
        print(f"\n🎉 ¡ÉXITO! 🎉")
        print(f"¡El número {numero_mar} es {'Par' if es_par else 'Impar'}! El mar te recompensa con el/la {recompensa_elegida[0]}.")
        return True
    else:
        print(f"\n💔 FRACASO 💔")
        print(f"El número {numero_mar} es {'Par' if es_par else 'Impar'}, y tú elegiste el opuesto. Tu ofrenda se pierde.")
        return False

def piedra_papel_tijera(mov: str) -> str:
    c = random.randint(1,3)
    if c == 1:
        c = "piedra"
        print("Contrincante escogió piedra")
    elif c == 2:
        c = "papel"
        print("Contrincante escogió papel")
    elif c == 3:
        c = "tijera"
        print("Contrincante escogió tijera")


    if mov == c:
        return "Empate"
    elif mov == "papel" and c == "tijera":
            return "Perdiste"
    elif mov == "piedra" and c == "papel":
            return "Perdiste"
    elif mov == "tijera" and c == "piedra":
            return "Perdiste"
    else:
        return "Ganaste"

def jugar_ppt_escena():
    while True:
        n = input("\nEscoge tu movimiento (piedra/papel/tijera): ")
        enter()
        print("""
        ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        :::::::::::::::::::::::::::::::::::::::::::-=@@@@--:::::::::::::::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::::::::-@@@@%--@@@@#-:::::::::::::::::-----::::::::::::::::::::::
        :::::::::::::::::::::::::::::::::::::::-@@--#+::%+-+@@-:::::::::::::::#@@@@@@%+--:::::::::::::::::
        :::::::::-==-*@@*+#*=-:::::::::::::::::=@@::-=::#:::@@@@*-:::::::::::=@@-:::=%@@@@%+======--::::::
        :::::::-@@@@@@**@@#%@@@@#::::::::::::::=@@::-=::#:::@--*@%:::::::::::-@@#-::::::-=#@@@@@@@@@%:::::
        :::::=%@@#::*=::+=::%#-*@@-::::::::::::=@@::-=::#:::@::-@@::::::::::::=%@@@@@*-:::=#-:::::-%@*::::
        :::-@@%+@*::--::--::--::@@-::::::::%@@@@@@::-=::#:::@::-@@:::::::::-@@@@@@@@@@@@+:%-:::::::#@#::::
        :::=@@::=*::::::::::::::@@-::::::-@@+--*@@:::::::::::::-@@:::::::::@@=::::::::::::%-:-+::::#@#::::
        :::=@@::=*:::::::::::::-@@-::::::-@@#:::-%:::::::::::::-@@:::::::::+@@*========%#-%-:-+::::#@#::::
        :::-@@=::::::::::::::::%@#:::::::::#@@-::::::::::::::::+@#::::::::::-+@@@@@@@-::::-%@@*::::#@#::::
        :::::%@@=:::::::::::::-@@:::::::::::-@@=-:::::::::::::-@@=::::::::::::::::-@@--=@*::::=#:::#@#::::
        ::::::-%@@+:::::::::::*@%:::::::::::::%@@-::::::::::::=@@::::::::::::::::::-@@@:::--+%+:--=@@=::::
        ::::::::-@@+:::::::::-@@+::::::::::::::=@@+----------=%@*:::::::::::::::::::-@@%*@%*#@@@@@@%-:::::
        :::::::::-@@@@@@@@@@@@@#::::::::::::::::-#@@@@@@@@@@@@@=::::::::::::::::::::::=#%%%%#+-:::::::::::
        ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        """)
        n = n.lower()
        if n in ["papel", "tijera", "piedra"]:
            return piedra_papel_tijera(n)
        else:
            print("El movimiento no existe. Elige piedra, papel o tijera.")


def mar(inventario, talentos, nombrejugador):
    print("\n--- ENCUENTRO EN EL MAR ---\n")
    enter()
    print("""
    ==================================================================================================
    ==================================================================================================
    ==================================================================================================
    ==================================================================================================
    ======================================================----:----===================================
    ===============================================-----=============-----============================
    ===========================================---==========---===========----========================
    ====================#====================--======-------------------======--======================
    ==================#@@*================---====---------------------------====---===================
    =================@@@@%===============--====-----------::::::::::----------====--==================
    ===============+@@@@%@=============--====--------::::::::::::::::::::-------====--================
    ==============*@@@@@#@+===========--===-------:::::::::::::::::::::::::-------====-===============
    ==============@@@@@@#@@==========-===-------:::::::::::::::::::::::::::::----++*#%#+%#***=========
    =============@@@@@@@#@@#========-====-----:::::::::::::::::::::::::::::::::------===-=============
    ============%@@@@@@@#@@@=======--==------:::::::::::::::::::::::::::::::::::------===-============
    ===========+@@@@@@@@#@@@@*====--===-----:::::::::::::::::::::::::::::::::::::-----===--===========
    ===========@@@@@@@@@%@@@@@%===-===-----:::::::::::::::::::::::::::::::::::::::-----===-===========
    ==========#%+====+@@%@@@@@@@@+-===-----:::::::::::::::::::::::::::::::::::::::-----===--==========
    =======*@@@@@%%%###%@@@@%%%####*==----:::::::::::::::::::::::::::::::::::::::::-----==--==========
    =========+@@@@@@@@@@@@@@@@@@@@===-----:::::::::::::::::::::::::::::::::::::::::-----===-==========
    @@%%%%%%@@@@@%%%%%%%%%%%%%%%@@@@@@@@@@@@%%%%@@@@@@@@@@@@@@%*+++*%@@@@%%%%%%%%%%%@@@@@@@@@@@@@@@@@@
    ####%%%%@%%%%%%%%%%##%%#######%%@@@@%%%#####%%%@@@@@@@@#---------*@@%%%%%%%#########%%%%%%@@@@@@@@
    %%%%@@@@@@@%@@@@@@@@%%%@@@@@@@@@@@@@@%%%%%%%%%%%%%%@@@@@@@@@@@@@@%%%%#+=++#@%%%%%%%%%%%%%%%%%%%%%%
    %%%%%@@@@@@@%%%%%%%%%%%%%%%@@@@@@%%%%%%%%@@@@@@@%###+=============+*#####%%%%%%%%%%%%%%%%%%%%@@@@@
    @@@@@@@@@%%%%%%%%@@@%%%%%%%@@@@@@@@@@%%%%%%%%%%#*============+*#%@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%
    %%@@@@@@%%%%%%%%@@@%%%%%@@@@@@%%%%%%%%%%%**+***######****++++++++++**#%@@@@@@@@%%%%%%%%%%%%%%%%%%%
    @@@@@@@%%%%%%%@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*++++++++++++++++++++++++++#@@@@@@@@@@@@@@@@@@@
    @@@@@@@%%%%%%%%@@@%@@@@@@@@@@@%%%%%%%%%%%%%%@@@#+++++++++++++++**#%%@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%######%%%%%%%%%%%%%#######*###%%@@@@@@@@@@@@@@@@@@@@@@
    """)
    print(f"\nDecides ir a buscar comida en el mar.\n")
    enter()
    print(f"\nA lo lejos puedes ver una silueta en la orilla del mar 🌊.\n")
    enter()
    print(f"\nMientras más te acercas te das cuenta que es una silueta que conoces.\n")
    enter()
    print(f"\n{nombrejugador}:¡Paco!")
    print(f"{nombrejugador}:¿Qué haces aquí?\n")
    enter()
    print(f"\nPaco: ¨Hola guapi, nada mas estaba admirando la belleza del mar¨")
    print(f"Paco: ¨¿Tú? Usualmente no te veo por aquí¨\n")
    enter()
    print(f"\n{nombrejugador}:Ah, pues estaba buscando nuestro desayuno")
    print(f"{nombrejugador}:¿Quieres ayudarme?\n")
    enter()

    while True:
        print(f"\nPaco: ¨Claro, iré solo para protegerte de los tiburones 🦈.¨\n")
        print("1. Jaja, aquí no hay tiburones. Tontito.")
        print("2. No creo que le puedas ganar a un tiburon, amigo. ")

        opcion = input("Elige el numero que deseas decir (1 o 2): ")
        if opcion == "1":
            print(f"\nPaco: ¨Bueno entonces te puedo proteger de los terrorificos cangrejos 🦀 ;). ¨\n")
            enter()
            print(f"\nJuntos caminan por un tiempo en un silencio comodo.\n")
            enter()
            break
        if opcion == "2":
            print(f"\nPaco: ¨Te sorprenderia lo que pueden hacer estos brazos.¨\n")
            enter()
            print(f"\nJuntos caminan por un tiempo en un silencio un poco incomodo.\n")
            enter()
            break
        else:
            print("Opción no válida")
    print("\nDe pronto, un cangrejo gigante sale detrás de una roca 🪨.\n")
    enter()
    print("""

                                     .                ..                 
                                      +               :.                 
                                      -.              @                  
                                       *-            %.                  
                                        -+          @                    
                                         :%        @                     
                                          .#     .@                      
                                           ==    @                       
                                            @   @.                       
                                            @: :#                        
                                            @  -#                        
                                         .-@*:  @:  ..                   
                                       @#******@*@#***#@-                
                                      @*%%%%%%%%*@%%%%%%@#               
                                    +@*@@%%%%%%%%%@%%@@:.@               
                                  *@#@....@@%@@%%%@#@@+.:@               
                                :@###%:.........:@###*#@@                
            +@%@@         @%   +@#####@#.......:@%#####*#@=  =@@         
           -@####@        @#%@@@@@######%@@#%@@##########**@@%@#         
           @#####@:       -@###############################*%@@          
           @#####%*         #@@%%%###########################*@          
           @######@         +@#######%########################*@         
           @######@         @########@########################*@.        
          +@######@@@@+    .@#########%########################@         
       *@##############@:  +@#########%@#####################@*          
      @#################@  *@###########@@################@@=            
     =@#################@+ *%##############%@@@@@@@@@@@@=.               
     +%#################%+ *%#######################%%@                  
     =@#################%*=@@@########################@.                 
     :@#################%@**#**@%#####################@@@:               
      @#################%@######%#####################%@##@              
      *@################@@######%#####################%@##@-             
      .@%%############%%@@#############################@##@.             
       #@%%%%%%%%%%%%%%%@@@@@@@########################@#@%              
       .@%%%%%%%%%%%%%%%@@@   @@%###################%@@@@%@              
        *@%%%%%%%%%%%%%%@      @%@@@@@@@@@@@@@@@@@%**+@-@@@%%@@@         
         @%%%%%%%%%%%%%@:      @######*+++++++++++++++%%########%@.      
          +@%%%%%%%%%@@.       @######*+++++++++++++++#@##########@+     
            .+#%%*=:           @%#####*+++++++++++++++#@###########%%    
                               =@%%%%#%*+++++++*+*****%%############%@   
                               +@@%%%%@**************%@##############%#  
         +@@@-                .@##@@@@@##******##%@@@@################@- 
        @#####@-             .#@%#####@*********+++++@#################@ 
      @@@@%%%##%*      .:=+@%##@@%%%##*+++++++++++++*@#################@=
     #@%%%%@%%%#@. @@@###@%###%%%@@%%%#**+++++++++++%@%%###############@@
     +@%%%%%%%%%%@#%%%%%%@#%%%%%%%%@@@@************#@@%%%%%##########%%%@
    #@%@@%%%%%%%%%%%%%%%%@%%%%%%%%%%%%##@@@%##**##@+ @%%%%%%%%%%%%%%%%%%@
    @%%%%%@%%%%%%%%%%%%%%@@%%%%%%%%%@#*******####@   -@%%%%%%%%%%%%%%%%%@
    -@%%%%%%%%%%%%@@@@@@@@@@@@@@@%#************#@.    %@%%%@. #@%%%%%%%%@
      =@@%%%%%%@@@#*******@@****************#@@:       %@%%@   @%%%%%%%@#
         .=**+.    :+%@@@@@@@@@@@@@@@@@@@@*:             +#.   @%%%%%%%@.
                                -@@# -@@:                      @%%%%%%@- 
                                +@@   @%*                      @%%%%%@:  
                                @%@   @%@                      @%%@@-    
                                @%@   @%@                      .-:       
                               .@%@   @%@:                               
                               -@%@   @%@:                               
                  :%@@@@@@@@@@==@%@   @%@-=@@@@@@@@@@%:                  
                @@%%%%%%%%%%%%%%@%@   @%@%%%%%%%%%%%%%%@@                
               @%%%%%%%%%%%%%%%%%%@.  @%%%%%%%%%%%%%%%%%%@               
               @@@%%%%%%%%%%%%%%%@@=.:@@%%%%%%%%%%%%%%%@@@          
    """)
    enter()


    while True:
        print("\nPaco se pone delante de ti, levantando los brazos como si realmente pudiera pelear.")
        print("Paco: ¨¡Atrás! Yo me encargo de esto… creo.¨")
        print("1. Reírte y animarlo.")
        print("2. Dar un paso adelante para ayudarlo.")
        print("3. Agarrarlo de la mano y jalarlo para esconderse detras de una roca.")
        opcion = input("Elige el numero que deseas decir: ")

        if opcion == "1":
            talentos[5][1] += 1
            print("\n¡Felicidades 🎉! Has ganado un punto de Sentido del Humor gracias a esta decisión.\n")
            print("\nPaco se siente animado por tus risas y te devuelve una sonrisa 😁.\n")
            enter()
            print("\nSin embargo eso es todo lo que necesita el cangrejo gigante para atacar.\n")
            enter()
            print("\nPara que Paco logre esquivar al cangrejo debes de tirar un dado, si sacas de 5 en adelante el habra pasado la prueba.\n")
            enter()
            dado = tirardado()
            if dado >= 5:
                print("Paco esquivo al cangrejo con facilidad.\n")
                enter()
                print("\nEn lo que estaba distraido el cangrejo ambos salieron corriendo.\n")
                enter()
                print("\nNo sabes como pero tu mano termino entrelazada con la de el.\n")
                enter()
                print(f"\nPaco te sonrie")
                print(f"Paco: ¨Buff {nombrejugador}, no sabía que eras así de interesante¨\n")
                enter()
                print(f"\nLe devuelves la sonrisa y no puedes evitar notar que sus ojos son del mismo color que el mar.\n")
                enter()
            if dado < 5:
                print("¡El cangrejo golpeo a Paco!\n")
                enter()
                print("\n¡El golpe fue tan duro que se cayó algo de tu inventario!\n")
                enter()
                print(f"-1 {inventario[1][0]}")
                print(f"-1 {inventario[0][0]}")
                inventario[1][1] = max(0, inventario[1][1] - 1)
                inventario[0][1] = max(0, inventario[0][1] - 1)
                abreinventario(inventario)
            break

        elif opcion == "2":
            talentos[6][1] += 1
            print("\n¡Felicidades! Has ganado un punto de Empatía gracias a esta decisión.\n")
            print("\nTe pones al lado de Paco y miras al cangrejo a los ojos. \n")
            enter()
            print("\nCangrejo Gigante: ¨¡Oye! ¡Dos contra uno no es justo 😢!¨\n")
            enter()
            print("\nPaco parece dudar sobre lo que van a hacer.")
            print("Ahora que son dos, necesitas una tirada de dado de 4 o más para asustar al cangrejo y hacerlo huir.\n")

            dado =tirardado()

            if dado >= 4:
                print("\n¡El cangrejo gigante se intimida por su valentía combinada y se retira rápidamente !\n")
                enter()
                print("\n¡Recompensa! Encuentras una Concha brillante 🐚 donde estaba escondido el cangrejo.\n")
                inventario.append(["Concha brillante", 1])
                abreinventario(inventario)
            else:
                print("\nEl cangrejo se enfurece. ¡Ambos son golpeados por un ataque de pinza simultáneo!\n")
                enter()
                print("\nPierdes 1 unidad de cada objeto, ¡y Paco pierde el único Pescado podrido que tenía escondido!\n")
                enter()
                inventario[1][1] = max(0, inventario[1][1] - 1)
                inventario[0][1] = max(0, inventario[0][1] - 2)
                abreinventario(inventario)
            break

        elif opcion == "3":
            talentos[11][1] += 1
            print("\n¡Felicidades! Haz ganado un punto de Controlador/a.\n")
            print("\nJalas a Paco detrás de una roca, sin darle tiempo de reaccionar. Paco se ve un poco molesto.\n")
            enter()
            print("\nPaco: ¨Oye, ¡yo iba a pelear! ¿Por qué hicimos eso?¨\n")
            enter()
            print("\nEl cangrejo no los ve detrás de la roca, pero está bloqueando el camino. Necesitas una tirada de dado 🎲 de 6 o más para esconderse y pasar desapercibido.\n")
            enter()
            dado = tirardado()
            if dado >= 6:
                print("\nLogran pasar de puntillas por el borde de la roca mientras el cangrejo mira al horizonte. ¡Están a salvo!\n")
                enter()
                print("\nTu acción preventiva le demostró a Paco que sabes lo que haces.")
                talentos[7][1] += 1
                print("¡Ganas un punto de Confianza gracias a la seguridad que le diste a Paco!\n")
            else:
                print("\nEl cangrejo escucha el crujido de la arena bajo sus pies 👣. ¡Se voltea y los ve!\n")
                enter()
                print("\nAmbos tienen que correr, dejando una **huella de pánico** por el lugar.\n")
                enter()
                print("\nPaco te mira con decepción. Él siente que tu falta de fe lo arriesgó a él y a tu misión.\n")
                talentos[7][1] = - 1
                print("¡Pierdes un punto de Confianza gracias al enojo de Paco 😤!")
            break

        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

        enter()
    print(f"Paco se sienta pesadamente en la arena, viendo cómo la marea rompe. No tiene fuerzas ni para limpiar el barro de su camiseta 👚.\n")
    enter()
    print("""                              
                                             .%--#-                                   
                                          .+#:::::-#                                  
                                          %-::::::::*                                 
                                          ::#::::::-=.                                
                                           *+:+-::-+=                                 
                                            @ .#=-*:                                  
                                       .:--=   ..+                                    
                                    *                -*                               
                                   :.                   .                             
                                   :                    :                             
                                                         .                            
                                   :  .+            -    -                            
                                   :   #            --    :                           
                        ::        #   -=            -+:    :                          
                       +-.:      =   ..             -  %   .:                         
                       .  :    ==    **             @   #    :                        
                       =  :*:  .-   +=+             @    :    =                       
                        :.=    +   ===+             #     +   .-                      
                          ..  :   %===+=           =+      %.  .:                     
                              +  @======++-     =*++-       .*  .:                    
                       ..:.  -  @   =*++=========+*.          +. .- ..::              
                ..... *. .=:.=.*           ...                  # + -++.+****+++                                                                                                                                         
    """)
    enter()
    print(f"\n{nombrejugador}: ¿Te duele algo? Deberíamos ponerle algo de hielo, si tuviéramos.\n")
    enter()
    print(f"Paco se ríe sin humor, un sonido áspero.\n")
    enter()
    print(f"\nPaco: ¨No es el cangrejo, {nombrejugador}. Estoy cansado de la isla 🏝️. De la sal, de la arena en todos lados, del coco. Estoy harto de no tener control. ¨\n")
    enter()
    print(f"Paco levanta una mano y la deja caer con frustración. Su mirada es de profunda derrota.\n")
    enter()
    print(f"\nPaco: ¨Llevamos dos meses aquí. Dos meses fingiendo que una piña colada y una fogata son vacaciones. No lo son. ¨\n")
    enter()
    print(f"Su voz se suaviza, volviéndose melancólica.\n")
    enter()
    print(
        f"\nPaco: ¨Extraño tanto las cosas pequeñas. ¿Sabes? Extraño un maldito cigarro 🚬 después de un mal día. Extraño quedarme despierto hasta las 4 AM jugando un videojuego sin tener que preocuparme por si un cangrejo gigante nos come. Extraño a mi familia. ¨\n")
    enter()
    while True:
        print("\nEs momento de apoyar a Paco, lo último que quieres es bajar los ánimos.")
        print("Así es como empieza el canibalismo 🍖.")
        print("1. 'Cállate y hablemos de la final de la Champions 🏐. Eres un crack, ya te salvaste de la vergüenza.'")
        print("2. 'Tu familia estaría orgullosa del esfuerzo que estás haciendo'.")
        print("3. Agarrarlo de la mano y sonreírle 😀.")
        opcion = input("Elige el numero que deseas decir: ")
        if opcion == "1":
            print(f"\n{nombrejugador}: Cállate y hablemos de la final de la Champions que perdiste. Eres un crack, ya te salvaste de esa vergüenza.\n")
            enter()
            print(f"Le das un golpe amistoso en el hombro, desviando completamente la conversación. Paco parpadea, la sorpresa borra su melancolía.\n")
            enter()
            print(f"\nPaco: (Su ego se enciende de nuevo, con tono desafiante) ¨¡Oye! No saques trapos viejos, {nombrejugador}. ¡Ganamos la anterior! ¡Y qué te crees, aquí soy el mejor! ¨\n")
            enter()
            print(f"\n{nombrejugador}: Claro que lo eres, campeón. Por eso sobrevivimos. Pero si te quedas llorando 😭 por un cigarro, ¿quién va a hacer el ridículo mañana? ¡Arriba esos ánimos! \n")
            enter()
            print(f"\nPaco: (Sonriendo de verdad, con su energía de vuelta) ¨Esa sí es mi {nombrejugador}. Okey, ¡a dormir! Mañana vamos a inventar la Coca-Cola con piñas 🍍. ¿Vienes al campamento 🏕️?¨\n")
            enter()
            print(f"\n{nombrejugador}: Nah, aún tengo algo de energía. Nos vemos en un rato.\n")
            enter()
            print("\nMiras a Paco regresar al centro de la isla con una sonrisa 😀 y un paso mucho más firme.\n")
            enter()
            break
        if opcion == "2":
            print(f"\n{nombrejugador}: Tu familia estaría orgullosa del esfuerzo que estás haciendo\n")
            enter()
            print(f"\n{nombrejugador}: Y no miento, tu 'no es ego, es confianza' es la única razón por la que a veces nos atrevemos a ir a explorar. Nos inyectas vida, Paco.\n")
            enter()
            print(f"Paco te da un codazo suave. El brillo en sus ojos 👁️ regresa, un poco más humilde que antes.\n")
            enter()
            print(f"\nPaco: (Sonriendo) ¨No es ego, es que realmente soy muy bueno. Pero gracias, {nombrejugador}. A veces necesito escuchar que mi espectáculo sirve de algo más que para mí. ¨\n")
            enter()
            print("\nPaco: ¨Bueno, no sé tú pero yo daría todo por una siesta. ¿Vienes al campamento 🏕️?¨\n")
            enter()
            print(f"\n{nombrejugador}: Nah, aún tengo algo de energía.\n")
            enter()
            print("\nMiras a Paco regresar al centro de la isla con una sonrisa y una ligera subida de ego.\n")
            enter()
            break
        if opcion == "3":
            print(f"\n{nombrejugador}: Yo también extraño a mi familia 👨‍👩‍👧‍👦.\n")
            enter()
            print(f"\n{nombrejugador}:Pero no todo es tan malo, al menos hay gente dispuesta a pelear con tiburones por mi en esta isla.\n")
            enter()
            print(f"Paco te mira y aunque no dice nada puedes ver en su cara que tus palabras le hicieron sentir mejor.\n")
            enter()
            print("\nPaco: ¨Bueno, no se tu pero yo daría todo por una siesta¨\n")
            enter()
            print("\nPaco: ¨Voy al campamento, ¿vienes?¨\n")
            enter()
            print(f"\n{nombrejugador}:Nah, aún tengo algo de energía 🪫.\n")
            enter()
            print("\nMiras a Paco regresar al centro de la isla con una sonrisa.\n")
            enter()
            break
        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

    print(f"Has terminado tu momento con Paco, debes buscar comida en otros lugares de la isla 🏝️.")

    return talentos, inventario

def cueva(inventario, talentos, nombrejugador):
    print("\n--- AVENTURA EN LA CUEVA ---\n")
    enter()
    print("""                                                            
                                                 .#.                                                           
                                                *%==*                                                          
                                               +.=* .=#                                                        
                                             *.:  #   :%#%+                                                    
                                           .@.   += -  :.* @-                                                  
                                          *+=+  #*+    #=#:#+@:   *#+@-                                        
                                        =@-+      *=    @:  -#=#@-#*  .@@@-                                    
                                       #% .    :    =@.  -    :.    *  -% *@                                   
                               -%=.  -@:.@      =:  +-  .. .*     .#   %-@* %#      .##.                       
                              %%= .+@*+-  #    *. -@+  .++        .  :# :*#+ -@-  #*-@:+@:                     
                            *%*=*  *+     .-        +%  @ :+-        .   %=-   #**@...   =*#                   
                          -%#.+.  -=        #  -%  =@@-*@@ #:      *.     -:#%*  *-#@   .% @@*                 
                        =%*- +. +#..++       *+@  @@@@@@@@@#*:=-:.         .@=%=  .@-%# @-  #+%                
                 #@=. +=   .%. *:=   .@.    =%*# @@@@@@@@@@@= +.=-#       *-   :@@: .:-@..   *#-@=             
               #*+:=.=+@=     . :  -+   -.   =++@@@@@@@@@@@@%  +-  -*:   -     % +%#  -.:..    .= +*           
             +# -%      .*  -+.   -+     =*..:*=@@@@@@@@@@@@@ + .:*: *%#.         =+*-   ==        -#%=.       
          =*.  +# -+   -*  *=+   @-   .@-  *   +@@@@@@@@@@@@@@@ .:   .@*            .@@   **  --       .      
        .*.  -+   :      - :   :   :=  .*= += =:%@@@@@@@@@@@@@@@-:.++    :+*-    -++-   .=  ..                
                             ..       +:=@- .-  @@@@@@@@@@@@@@@@@+   @@@-     :=*.                            
          .   .+*+.=%%+=::        =%#@*- =*.:  :#@@@@@@@@@@@* #@@*+:    :#@@%#=      :#*+                      
                           .-=#@+.    .+@@+  ..   *: =@@@@@-   +@*=-:   .=%@++-##@%@@@#                        
                                  :::  +@@@@#-       =%.              . ..                                                                                                                      
    """)
    print(f"\nBuscas refugio o quizás algo de mineral ⛏️ útil y te adentras en una cueva oscura.\n")
    enter()
    print(f"\nAl iluminar con tu antorcha 🔥, ves a Blanca, sentada y concentrada.\n")
    enter()
    print(f"\n{nombrejugador}: ¡Blanca! ¿Qué haces tan adentro? Pareces absorta.\n")
    enter()
    print(f"\nBlanca: ¨Ah, {nombrejugador}. Aquí no es oscuro. Es una paleta de grises muy díficil de encontrar.¨")
    print(f"Blanca: ¨Mira, ¿te has dado cuenta de lo que acaba de pasar?\n")
    enter()
    print(f"\n{nombrejugador}: ¿Qué cosa? ¿Que acabo de esquivar una telaraña 🕸️ gigante?\n")
    enter()

    while True:
        print(f"\nBlanca: ¨No, tontit@. Justo en esa telaraña, había un patrón que replica la Torre Eiffel 🗼.\n")
        print("1. Jaja, Blanca, tienes una imaginación de otro nivel.")
        print("2. Tienes razón, el detalle cambia todo. ¿Ves algo más raro?")

        opcion = input("Elige el número que deseas decir (1 o 2): ")
        if opcion == "1":
            print(f"\nBlanca: ¨No es imaginación. Es sensibilidad. Y el humor es para defenderse, ya sabes ;). ¨\n")
            enter()
            print(f"\nAmbos se adentran un poco más, compartiendo un silencio lleno de complicidad.\n")
            enter()
            break
        if opcion == "2":
            print(
                f"\nBlanca: ¨Sí. Hay un olor a sopa de tomate 🍅, pero estamos en el trópico. No es nada... pero sí es algo.¨\n")
            enter()
            print(f"\nSiguen avanzando, con un ligero aire de misterio en el ambiente.\n")
            enter()
            break
        else:
            print("Opción no válida")
    print("\nDe pronto, encuentran un brillo deslumbrante en una recámara oculta. ¡Es una bola de discoteca gigante 🪩!\n")
    enter()
    print("\nMientras Blanca está a punto de señalar que 'la luz de esta bola es demasiado saturada', escuchan un '¡SHH!'.\n")
    enter()
    print("\nUna red de pesca hecha de hojas de palmera con brillantina cae sobre ustedes. Son capturados por...\n")
    enter()
    print("\n¡La Tribu de Los Caníbales 🍖 Un Poco Ofendidos!\n")
    enter()
    print("""
    ....................................................:++=............................................................@*%%..................:..*..........................................................................................
    ....................................................++++=..........................................................:%@#.........=:........%%*%..........................................................................................
    ..............:......................................:*:............................................................@-..........=+.........%@%.....................................+.=:.................................................
    ............-@@@@:....................................#:.............=*:...........................................:..............=#+.......%%.................................=%@=+%+==-...............................................
    ...........*@@@@@@:...................................*=...........-*@@%+..........................................-.............===+#.......%................................##%@%@%%*==-.............................-%@+.............
    ...........##@@@@*.......................-=:..........-*...........@@@@@@-.......................=@%%%%@*.........+..............%@@@@.......:..............:=::...............#%%%%%@%#=:............................#@@@@@-...........
    .........*%..=*#*......................:@@@%#.........:%...........+@@@@@.......................@@%====%%@-......@@.............:.@@@+:.......%............+*%%#-...............=%%%%%@@#=............................%@@@@@:...........
    .......+@+..-@@@@#.....................+@@@@*..........%............*@@%.......................*%*=+%@#==%#......%#@...........:-@@@::=....................=@@@@=..................:%#*%@@+...........................+@@@@:............
    ......+@-...:@@@@*....................--@@@#::.........%............*@@%::......................@=*@@@@#=#=.....-..%@......=@@@@%@@@@@-.......-@............@@@#......................@@@@@............................*@@*.............
    .......%@#...:%@=........................@@+:.........+@@*....+%###*##*#*#**#*-..+@@@............++@@@@*=:......#...@@..=@@@+:%@@@@@@%@@.....:@@............-@@=:......................**@%......................------++---#*:.........
    ........*@@=-=##+=................-+%%%%@%%@#@%%%=:....*@@@-..=@%%#*##***##**-.@@@@@@@.............#@@*:.......-.....@@@@=....+@@@=#@%+@@-..-@..:........=**#@@%-#=.........-........=@#####...................--------*---##---........
    .........:@@##%%##*%@..............#%%#%%%%%@#%%%=.....-#:@@@=@@@#%###****#@@@@@@@@@@@.............-@@#.......................-@@@@@@:-.@@:=@%..%......+@@@#%%%@#%@@*.......@+......=@@%%@@@#:...............=------------%#-----.......
    ...........%%%%%%%%@@@+..........#@@+-%%%@%%@%@@........%.:@@@@@=.@%*#**#%@@@@@#@@@@@@.........=+%*%%%##%#+-...................@@@@@-....%@@%........##+=.==%%%%%%-*@@=.....=#@=...---@@%%%%@=.............*@@@=--==--==+@+-------......
    ............**%#%%%..-@@-......#@#....+#######@@........@...:%#...#%%%###@:%@@@@@@@#@@.......=@#==%++@=+#=+#+..................=@@@@+.....:........#@#....==@##@%%...-@@:....@.=@@@+:.=@@@%@+@=.............#@@@@@%*=--#%---------:.....
    ............-=*==+.....-@*......*@#...-******+-@........#.........:@##%#@@:@@@@@@@@@@@.....#@@=..=##**#*#:@@%..................:@@@@@@:.............#@*...-=*%%%%#....%@#....@:........*@@@@-@-..................-=%@#*+%@@@@@@@@@@.....
    ............#@@@@%...-@@*.........:#+.+******=:@........*.........:@@%@@@@@@@@@@@@@@@.....%@=.....@#*##%-..+@#.................%@@@@@@@@-.............-@+.-@@@@@@:.=@%:......*=.........%%%*%=..................=*==+==-------:.........
    ...........=#*+++*#@*:...............=********:@-.......==.......-%%%%%%%%@#@#@@@@@@-.......=@%...@@##%@-:%@@#.................@@%@@@@@@@@=..............=@=-%%%@@#+=.........#........@@%@@*...................=*%*=+*#*-----:.........
    ..........-#%%@@@@#+.................**********@:.......-#......:%%%%%%%%%@@@@@@@@@=...........-%@=+**@@+-....................:@@@@@@%@@@@@@+............====%%%%%*...........@.......#@@@@@@-.................-@#++***@@*----:.........
    ..........#%%@@@@%@@.................***********.........@......#%%%%%%%%%@@@@@@@@:............+%*%#==*@*@-...................-@@@@%-....@@@@@#..........==-*%%%%%%...........%-.....:@@@@@@@#.................+@@@@@*%#*+-----.........
    .........:%@@@@@@@@%+................**********@.........@.....:#%%%#%%%%%@@@@@@+.............:@%#=%**%=#@@...................*@@@+........=@@@%.........==:#%%%%%%...........-*.....-@@@%@@@@-................=%%%%@@@@+------:........
    .........*@@@@@@@@@@@................********#@@.........#.....+#%%#%%%@%%%@@%................%@%%##@%#*%@@+..................@@@@....:=.:+#@%#%.........==:%%%%%%%............@.....#@@@%@@@@*................:%%@#+*+=--------........
    .........%+%+#****#+%................*****#@@@%..........+.....*#%%#%%%@%%%%%+................@@#==*%%*==#@@..................@@@....=.=.-@@@%-:.........==:%%%%%%#............%:....@@@@@@@@%@:...............====+====--------........
    .........:@@@+..-@@@-................*%@@@%%%%%..........==....##%%##%%#%%#%%#...............+@#*%%+**=%%#@@..................@@@......=-%@@%:=..........==:%%%%%%*............++...-@@@@%@@@@@+................=======---------:.......
    .........+@@%....@@@-................*%@%%%%%%%..........:#...:%%%%##%#*%%#%%%:..............%@@@@@@@@@@@@@@=.................%*%=.....-+@@:%#=..........==:%%%%%%*.............%...=@@@@%@@%@@%................+======---------:.......
    .........%@@:....-@@+................#%%%%%%%%%...........@...=#%%%*#%%*@%##%%:..............-*@@@@@@@@@@@%=:................:*@%#==...-@@.*=:*.........:===%%%%%%*.............@...@@@@@%@@%@%@-..............=+======-----=+*+........
    .........@@#......@@@................-*%%%%%%%%...........@...:**%###%#+%%*#-..................*@@......@@@.................:%.@@@#-+..@*...-#..........:===%%%%%%*.............*+.:@@@%@%%@@@%@*.............:++++*:......**+++........
    .........@@#......@@@................-========:...........%.....%@@@:...*@@@:..................+++......++*:................-=+*@@=:+#@*.....-..........:===%%%%%%+.............-%.-@@@%@%@@@@@@@.............=+++++......:*++*-........
    ........+@@-......+@@:...............-======**............+.....%@@%....:@@@:..................##*......*##=................-.#.@@@+.+#*................:=====+%@@-..............@.*@@@%@%@%@%@%@+............=++**.......:**++.........
    ........@@*........@@:...............====-.@@.............-=....%@@-.....#@@:..................%*-.......*#+.................::=#@%=.:.@.................@%%%@@%%%:..............*-@@@@@@%@@@%@%@#............****........=*+++.........
    ........@@.........#@:...............=%#...@@.............:#....%@*.......@@-..................@%........#@+...................=.#@......................@%%%%%%%@:..............=%@@@@@@@@%@%@%%@...........+++*-........*++++.........
    .......:@-..........@:...............-@-...#%..............@....%@........:@-.................:@+.........@+......................@=.....................%@.....@=................@.@%::=++==:.#%...........:+++*.........++++=.........
    ......-@+...........@#...............#@....*%..............@..:#@%.........@@+................=@..........%#......................@:....................:@*.....@+................%-@=..........@*..........+#*++.........*#%%+.........
    ......:...............:......................................................................---..........:--:....................................................................-:::::........::::........:::.............::::........
    """)
    enter()
    print("\nSu líder, con un sombrero de fiesta y un traje de baño 🩱, dice:\n")
    print("\nLíder: ¨¡Nadie toca la bola de discoteca sin pagar el cover de la fiesta! ¡Ahora a la Olla de las Decisiones Difíciles!¨\n")
    enter()
    print("\nSon arrojados a una jaula hecha de cañas de bambú y sujetada con cordones de zapato. Los caníbales se sientan a discutir el menú.\n")
    enter()
    while True:
        print("\nBlanca está absorta mirando la etiqueta de precio del traje de baño del Líder, sin entender el tipo de cambio.\n")
        print("Tienes que concentrarte y usar uno de tus talentos para escapar.")
        print("1. Intentar entender su dinámica y apelar a sus emociones.")
        print("2. Buscar algún un fallo en la jaula o en el entorno.")
        print("3. Idear un plan de distracción demasiado elaborado.")

        opcion = input("Elige el número para intentar escapar: ")

        if opcion == "1":
            talentos[8][1] += 1
            print("\n¡Felicidades 🎉! Has ganado un punto de Sensibilidad.\n")
            print("\nObservas que los caníbales se ven profundamente aburridos y tristes, como si hubieran perdido el control remoto.\n")
            enter()
            print("\nPara conmoverlos y lograr que los liberen por 'lástima social', necesitas sacar 5 o más en un dado.\n")
            enter()
            dado = tirardado()

            if dado >= 5:
                print("\n¡Éxito! Les gritas: '¡Su tristeza 😢 es palpable! ¡Se nota que extrañan la televisión por cable! ¡Liberennos por un sentido de comunidad global!'.\n")
                enter()
                print("El líder caníbal derrama una lágrima: '¡Es cierto! ¡El internet 🛜 está fallando! ¡Lárguense, antes de que el sentimiento pase!'.\n")
                enter()
                print("\nBlanca te sonríe con admiración. ¨Sabía que no todo era lo que parecía. El detalle cambia todo. Y tu sensibilidad es... genuina.¨\n")
                enter()
            else:
                print("\n¡Fallo! Les gritas: '¡La falta de armonía de este grupo me lastima!'.\n")
                print("\n¡No puede ser! Por su fallo has perdido un punto de Sensibilidad.\n")
                enter()
                print("El líder caníbal grita: '¡No vinimos a hablar de sentimientos! ¡A la olla!'.\n")
                enter()
                print("Blanca pone los ojos en blanco, saca un lápiz ✏️ y dibuja una nota rápida en un trozo de corteza.\n")
                print("Blanca: 'Oye, Líder. El cuello de tu traje de baño está al revés. Lo noté. Detalle mata caníbal.'\n")
                enter()
                print("El líder caníbal, avergonzado por la falta de estilo, corre a esconderse. ¡Los demás se dispersan por el caos!\n")
                inventario.append(["Lápiz de Blanca", 1])
                print("\n¡Blanca los ha salvado! Encuentras un Lápiz de Blanca en la jaula.\n")
                abreinventario(inventario)
            break

        elif opcion == "2":
            talentos[9][1] += 1
            print("\n¡Felicidades 🎊! Has ganado un punto de Detallismo.\n")
            print("\nTe concentras en los nudos de los cordones de zapato 👞 que sujetan el bambú.\n")
            enter()
            print("\nPara encontrar el nudo de zapato que el Líder hizo en un momento de distracción (es el más flojo), necesitas sacar 7 o más en un dado.\n")
            enter()

            dado = tirardado()

            if dado >= 7:
                print("\n¡Éxito! Encuentras el nudo flojo: ¡es una lazada doble y no triple! Lo deshaces en segundos.\n")
                enter()
                print("\nEscapan mientras los caníbales discuten si la bola de discoteca es 'vintage' o 'simplemente vieja'.\n")
                enter()
                print("\nBlanca asiente: ¨El detalle cambia todo. Yo estaba por dibujar un croquis del nudo, pero tú fuiste más rápido. Me atrae ese detalle.¨\n")
                enter()
                inventario.append(["Cordón de zapato (cuerda)", 1])
                print("¡Recompensa! Toman un Cordón de Zapato resistente de la jaula desarmada.\n")
                abreinventario(inventario)
            else:
                print("\n¡Fallo! El nudo que elegiste es una obra de ingeniería naval. Pierdes tiempo y un caníbal te ve.\n")
                print("\n¡No puede ser! Por su fallo has perdido un punto de Detallismo.\n")
                enter()
                print("\nCaníbal: '¡Oigan! ¡Miren al prisionero! ¡Está oliendo mis zapatos! ¡Qué raro!'.\n")
                enter()
                print("Blanca, con su humor 🤣 inteligente, interviene: '¡No! ¡Está haciendo una reseña! ¡Dice que la textura visual de tu dedo gordo es muy expresiva!'.\n")
                enter()
                print("El caníbal se distrae con el halago artístico. Blanca aprovecha y patea un pequeño coco rodante que golpea la pierna del Líder, desequilibrándolo y haciendo que caiga la llave (un tenedor oxidado).\n")
                print("\n¡Blanca los ha salvado! Ella usa el tenedor para pinchar la jaula y salen.\n")
                inventario.append(["Tenedor Oxidado (Llave)", 1])
                print("¡Recuperan el Tenedor Oxidado 🍴(Llave)!.\n")
                abreinventario(inventario)
            break

        elif opcion == "3":
            talentos[10][1] += 1
            print("\n¡Felicidades! Has ganado un punto de Inteligencia.\n")
            print("\nTe pones a idear un complejo sistema de escape: usar un palo, una roca, y la bola de discoteca 🪩 para crear un efecto dominó.\n")
            enter()
            print("\nPara que tu plan de 'caos controlado' funcione, necesitas sacar 6 o más en un dado.\n")
            enter()
            dado = tirardado()

            if dado >= 6:
                print("\n¡Éxito! El sistema funciona: la bola de discoteca rueda, refleja el sol en la cara del Líder, y la roca golpea un tronco, que abre la jaula. ¡Es un escape digno de película!\n")
                enter()
                print("\nBlanca está impresionada: ¨Wow, qué ingenioso 😏. Me encanta que no uses el camino obvio. La complicidad es clave.¨\n")
                enter()
                print("¡Ganas un punto de Complicidad con Blanca!\n")
            else:
                print("\n¡Fallo! El palo se rompe y solo logras que la bola de discoteca gire muy lento. Los caníbales se ríen de tu intento.\n")
                print("\n¡No puede ser! Por su fallo has perdido un punto de Inteligencia.\n")
                enter()
                print("\nLíder: '¡Jaja! ¡El prisionero hizo un show de luces de baja calidad!'.\n")
                enter()
                print("Blanca se adelanta y dice con sarcasmo: '¡Qué vergüenza! ¡Pensé que como tribu al menos tendrían un criterio estético! ¡Esa bola de discoteca tiene un filtro cromático horrible!'.\n")
                enter()
                print("Los caníbales se quedan en silencio, ofendidos. Blanca aprovecha la distracción 'artística' para patear la cerradura de cañas con un movimiento inesperado. ¡Escapan!\n")
                inventario.append(["Critica Estética", 1])
                print("¡Blanca los ha salvado! Ganan un punto de Critica Estética (un concepto valioso).\n")
            break

        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

    print(f"\nBlanca se sienta pesadamente en una roca, mirando un pequeño charco de agua con decepción. No es tristeza, es vacío.\n")
    enter()
    print(f"\n{nombrejugador}: ¿Te duele algo? ¿Fue la paleta de colores de esa jaula?\n")
    enter()
    print(f"\nBlanca se ríe, pero es un sonido apagado, sin su brillo habitual.\n")
    enter()
    print(f"\nBlanca: ¨No es la jaula, {nombrejugador}. Estoy exhausta de la superficialidad. De sobrevivir, de la falta de capas. Estoy harta de que todo sea 'peligro' o 'comida'. ¨\n")
    enter()
    print(f"\nBlanca señala el charco. Su mirada es de profunda melancolía.\n")
    enter()
    print(f"\nBlanca: ¨Llevamos dos meses aquí. Dos meses donde la única 'expresión' es un coco 🥥 con una cara dibujada. Extraño el arte que te rompe el alma. Extraño una conversación que no sea: '¿Hay un tigre 🐅?' o '¿Comemos esto?'. Extraño sentir que hay algo invisible, pero real, en lo que hacemos. ¨\n")
    enter()
    print(f"\nSu voz se vuelve un susurro, genuinamente vulnerable.\n")
    enter()

    while True:
        print("\nBlanca necesita complicidad mental y emocional. No puedes permitir que se ahogue en la melancolía.")
        print("1. 'Cállate, tienes razón. Pero al menos nos salvamos. ¿De qué color es la tristeza, por cierto?'")
        print("2. 'Tu capacidad para ver el 'algo' en el 'nada' es lo único que mantiene nuestra alma viva aquí'.")
        print("3. Tocarle la mano y sonreírle con comprensión, sin decir nada.")

        opcion = input("Elige el número para apoyarla: ")

        if opcion == "1":
            print(f"\n{nombrejugador}: Cállate, tienes razón. Es la falta de profundidad. Pero al menos nos salvamos. ¿De qué color es la tristeza, por cierto? ¿Un pastel ahumado?\n")
            enter()
            print(f"\nLe das un empujón amistoso en el hombro, usando el humor rápido para desviar la intensidad. Blanca parpadea, su ironía se enciende.\n")
            enter()
            print(f"\nBlanca: (Su humor se recupera, con tono sarcástico) ¨¡Oye! No saques mi paleta de colores emocionales. Es un gris saturado. Y sí, tienes razón. Si seguimos vivos, es gracias a mi ojo de águila para el detalle... y tu capacidad para meterte en problemas.¨\n")
            enter()
            print(f"\n{nombrejugador}: Claro que sí. Ahora vamos, campeona. ¿Vienes al campamento 🏕️ para dibujar el mapa de los caníbales?\n")
            enter()
            print(f"\nBlanca: (Sonriendo de verdad) ¨Solo si me ayudas a encontrar un pigmento más vivo. Vamos.¨\n")
            enter()
            print("\nBlanca se dirige al centro de la isla 🏝️ con una sonrisa 😁, lista para encontrar lo invisible en el mapa.\n")
            enter()
            break

        if opcion == "2":
            print(f"\n{nombrejugador}: Tu capacidad para ver el 'algo' en el 'nada' es lo único que mantiene nuestra alma viva aquí. No eres superficial, eres el ancla ⚓ de la profundidad.\n")
            enter()
            print(f"\nBlanca te mira fijamente, y una lágrima de genuina sensibilidad se asoma. Se siente validada.\n")
            enter()
            print(f"\nBlanca: (Con suavidad) ¨Gracias, {nombrejugador}. A veces necesito que alguien note el detalle invisible de mi esfuerzo. Gracias por escucharme de verdad.¨\n")
            enter()
            print("\nBlanca: ¨Bueno, voy a dibujar el escape. ¿Vienes al campamento?¨\n")
            enter()
            print(f"\n{nombrejugador}: Te alcanzo en un rato. Necesito algo de 'paleta de colores 🎨' también.\n")
            enter()
            print("\nBlanca regresa al campamento con el alma más ligera, apreciando la conexión emocional.\n")
            enter()
            break

        if opcion == "3":
            print(f"\nLe agarras suavemente la mano, el gesto dice 'Yo te entiendo'.\n")
            enter()
            print(f"\n{nombrejugador}: Yo también. Pero la belleza del mar, la del coco, y la de un amigo que no se rinde... tampoco es un mal arte.\n")
            enter()
            print(f"Blanca aprieta tu mano 🤚. Aunque no dice nada, sientes la complicidad. Sus ojos reflejan gratitud.\n")
            enter()
            print("\nBlanca: ¨Bueno, no sé tú pero yo daría todo por dibujar un rato. Voy al campamento 🏕️, ¿vienes?¨\n")
            enter()
            print(f"\n{nombrejugador}: Nah, aún tengo algo de energía. Nos vemos en un rato.\n")
            enter()
            print("\nMiras a Blanca alejarse, la sensibilidad de tu gesto ha reconfortado su espíritu.\n")
            enter()
            break

        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

    print(f"Has terminado tu momento con Blanca, debes buscar comida en otros lugares de la isla 🏝️.")

    return talentos, inventario

def playa(inventario, talentos, nombrejugador):
    print("\n--- ENCUENTRO EN LA PLAYA ---\n")
    enter()
    print("""                   
                                                     *#.+#*=+#*: ..                              
                                                   =# #+     :%:-#                                    
                                                   =# @:     .#-:%.                                   
                                     ::              -@:   .#+.*:                                    
                                     .%@=              =.-*##=.                                     
                                      .%%#:                                         
                            .:-====:.  :#+%-     .:::    ...   ..-*#***##+:                           
                         .+@@%*-:::-=**-+++*..+#+=---+#+       :#=.      :+#=                         
                             :-+**+-. .+%@+###-:=*******=     .#-          -%#***+:                   
                                  .+#*-.-@%@*+%%+=--:.        :%:          .:.   =*:                  
                                     .+#=#@@@@#=:..:=##=. .:::=%+                .*=                  
                                   .-+##@@@@#+-:..     -@=.=:#%         :*%=     =*:                  
                                .+%*: *@@@@@@::*@@%@%+:  *#                .--.  -##+-.               
                              :*#%+ .*#: -*+@@=  :@=  :+@%@=                         ++.              
                            .+%=  =%%-   :#:*+#*.  #=    .:.  ----::::::.........::-*%-               
                           :*==#+:*+.    .#:++.+#. .@         :::::----------------::                 
                          -*-  .=%+.     .%:#=. +#. @:                                                
                         -#=   .*+.      :#+#:   +#:@                                                 
                        :*##=:.=*:       -%%:     +@+                                                 
                        =*. :+%@=        :-.       :                                                  
                       :#+    -*:                                                                     
                       -#*%@%#%*.                                                                     
                       -*.    +*.       .=+*###%%%@@@@@@@@@@%%%%%%%%%%%%%%%%%%@@@@@@-                 
                      :+*++****#**####@#-......                                                       
                                 -###%%-  :=+=-        +###=    :#+         -#+:                      
                                    :+@%=.                 ..::.        ...  ..                       
                                     ..:=***++=-:.         =++=-       :++=.                          
                                              .-=*##*=.                                               
                                         ...         :@     .=====:      .=++-   .=+.                 
                                         :=-      .:=%*                                               
                                           :.   .@+.                                                  
                                           .    -%:             .=++++-     .-=-:                     
                                                 .-=+**#%%#*=.   ......      .::.                     
                                                          ..:=#.                                      
                                                             .#-     :----.      :=+:                 
                                                            =#=      :---:.      ...                  
                                                           -%                                         
                                                           .%+..                 -#+.                 
                                                             .=*%@@%*=-.                              
                                                                       .:=*%@@*:                      
                                                                              .-#=                    
                                                                                :-.                   
    """)
    print(f"\nDecides ir a buscar comida a la playa 🏖️.\n")
    enter()
    print("\nHace mucha calor, el sol apunta directamente hacia ti.\n")
    enter()
    print("\nA unos metros escuchas unos sigilosos pasos sobre la arena.\n")
    enter()
    print("\nAl girarte, ves a Verónica acercándose a ti con una sonrisa.\n")
    enter()
    print(f"\nVerónica: ¨Hola {nombrejugador}. Estaba intentando coger cocos, pero todos están muy altos.¨")
    print("Verónica: ¨Con un poco de suerte, lo único a lo que nos enfrentaremos hoy serán estos cocos.¨\n")
    enter()

    while True:
        print("\n1. JAJAJAJA, tranqui, el único peligro que corremos aquí es quemarnos, porque con el sol que hace puede venir Andalucía Directo a hacer un huevo para inaugurar el verano.")
        print("2. Espero que no… sinceramente no estoy de humor como para morir hoy.")

        opcion = input("Elige el numero que quieres decir (1 o 2): ")

        if opcion == "1":
            talentos[5][1] += 1
            print("\n¡Muy bien! ¡Sigue así! Has ganado un punto de Sentido del Humor.\n")
            print("\nVerónica se esta partiendo de risa.\n")
            enter()
            print("Verónica: ¨Tienes razón. A veces olvido relajarme un poco.¨\n")
            enter()
            break
        elif opcion == "2":
            talentos[10][1] += 1
            print("\n¡Felicidades! ¡Sigue así! Has ganado un punto de Sensibilidad.\n")
            print("\nVerónica se muerde el labio 🫦, haciendo contacto visual.\n")
            enter()
            print("Verónica: ¨Literal no estoy preparada para morir, tengo miedo.¨\n")
            enter()
            break
        else:
            print("Opción no válida")

    print("\nEn ese mismo instante, cuando se acercan a la palmera 🌴, escuchan un chillido.\n")
    enter()
    print("\n¡Aparecen unos monos 🐒 trepando las ramas! Parece que están enfadados, ya que están protegiendo los cocos.\n")
    enter()
    print("""                                              
                                              -#%@@%%%@@@#+.                                          
                                           +%@%#++++++++++*#@#:        =#%%%%%*-                      
                                         *@%###############+++%@-.=+=*#*######**##.                   
                                       :@%##################**++%@=:-+%@%#%%%####*%=                  
                                   ..:+@#####+++######=......:*#+#@@#=.=@+   #%####%+                 
                                .%%*++@%##=.......=##:.........=#*%%==-:=@    %%####@.                
                               +@::=*@%##-..........:.....:.....*#*@*==-=@.   *@%###%%                
                              .@:.#=*@%#*.....:.........-%@#....*##%@=-=@=    :@%%%%%@                
                              .@-:==#@###....-@@@*=...=@@@@*...=####%%%@%@.    #%%%%%+                
                               #%--=#@###+....%@@@*.....**:......:+*#%@%#%#     *@@%-                 
                                #@+-#@####+:......:%+:#..............-@@@#%@                          
                                  .%@##=.........:-=#%**#%#=:.........@=+%%%+                         
                                   +@+........:*:  .  .-++::.#.......-@: %%%@:                        
                                   :@.........+:+ .:*%%##%%+%+.....:+@:  :@%%#                        
                                   :@%:.......*@%...............:-+@@#@@. %%%#                        
                                .%@##%@#-:..:::............::--*@@%#####%@@%%#                        
                               *@####%##@@@=+..-=---#.. %+=@@@@@####%%####@@%#                        
                              @%#######@@+-+==+-#@@@--..#::::*#..=@%######%@@.                        
                              @%%####%@@@@#-===@@:::%*::*::-=*@@@@@@%####%%%*                         
                              :@%%%%@#:...:=@*%:.......@===*@-.....:%%#%%%%@:                         
                               :@%%@=....:#:=@:..........::*%+*......%%%%@#                           
                                 :@@....*=:%@*..............-@#@:.-..*@@+                             
                                  .@-.-%:%@%%=.....-%%:......#%@%@:.-@                                
                                   .@#+%@@%%%%........:......%%%%@#%#.                                
                                     ..:@%##%%+--::....::---+%%###@=                                  
                                       =%######=-----------+%%####%%                                  
                                       @######%%%@@@@@@@@@%%%%#####@:                                 
                                      .@######%%%@-     :@%%%%#####@-                                 
                                      .@######%%@+       :@%%%#####@-                                 
                                    -*@@#####%%%@%%@@@@@@@@%%%#####@@#=.                              
                               .=*%@@%*=@%%%%%%%@@@@@@@@@@@%%%%%%%@*+#@@@@@@%+=.                      
                           :#@@@@@@@#::..:*#%@%#*@@@@@@@@@##%@%#*-..::*@@@@@@@@@@@*.                  
                          #@@@@@@@@@@@%:.::...:=:@@@@@@@@@=--...:-.:#@@@@@@@@@@@@@@@*                 
                          =@@@@@@@@@@@#%@@-.:#@@@@@@@@@@@@@@@%-.:@@%#@@@@@@@@@@@@@@@=                 
                            :*%@@@@@@@@@@@#%@@@@@@@@@@@@@@@@@@@@#@@@@@@@@@@@@@@@%*.                   
    """)
    enter()


    while True:
        print("\nEl lider de la tribu de monos apunta el coco para lanzárselo a Verónica.")
        print("Verónica: ¨¡Cuidado! es el lider de la tribu, tiene unos niveles de agilidad y punteria increibles.¨")
        print("1. Gritar más alto que el lider de la tribu y tirar una piedra para asustarlos.")
        print("2. Sacar una fruta de tu inventario para conseguir un intercambio humano-monos pacífico.")
        print("3. Proteger a Verónica y esperar a que se cansen.")

        opcion = input("Elige el numero que quieres elegir: ")

        if opcion == "1":
            talentos[0][1] += 1
            print("\n¡Congratulations :)! Has ganado un punto de Fuerza.\n")
            print("\nAgarras una piedra maciza y dura, y gritas con todas tus fuerzas. En ese instante los monos se quedan paralizados.\n")
            enter()
            print("\nNecesitas tirar un dado y que salga 4 o más para que los monos salgan pitando de allí.\n")
            dado = tirardado()

            if dado >= 4:
                print("\n¡Los monos te tienen miedo y salen corriendo hacia la selva!\n")
                enter()
                print("\nAl salir corriendo, los monos se dejaron varios cocos 🥥 con muy buena pinta 😋.\n")
                inventario.append(["Coco", 2])
                abreinventario(inventario)
                print("\nVerónica te mira con una mirada de admiración 💕.")
                print(f"Verónica: ¨Vayaaa {nombrejugador}, recuérdame no hacerte enfadar en mi vida.¨\n")
            else:
                print("\nA pesar de que los monos se asustan, el lider de la tribu se enfada y pega un chillido extremadamente fuerte!\n")
                enter()
                print("\nEmpiezan a lanzar cocos y bolas de arena. ¡Te estan haciendo!\n")
                print("\nPierdes la concentración durante unos segundos\n")
                print("\nTe levantas y se te cae un objeto del inventario huyendo de los monos.\n")
                if len(inventario) > 0:
                    item_perdido = inventario[0]
                    print(f"-1 {item_perdido[0]}")
                    inventario[0][1] = max(0, inventario[0][1] - 1)
                abreinventario(inventario)
            break

        elif opcion == "2":
            talentos[1][1] += 1
            print("\n¡Congratulations :)! Has ganado un punto de Ingenio.\n")
            enter()
            print("\nIntentas razonar con la naturaleza. Sacas algo atractivo o comida de tu bolsillo.\n")
            enter()
            print("\nLos monos bajan como buenos cotillas. Necesitas lanzar el dado y sacar 5 o más para que acepten el trato.\n")
            dado = tirardado()
            if dado >= 5:
                print("\n¡El mono lider acepta tu ofrenda! A cambio, te lanza un coco dorado 🥥🪙.\n")
                enter()
                print("\n¡Intercambio completado ✅!\n")
                inventario.append(["Coco Dorado", 1])
                abreinventario(inventario)
            else:
                print("\nEl mono 🙊 te roba lo que tenías en la mano y te muerde el cuello.\n")
                enter()
                print("\n NOOOOO, no solo no conseguiste el coco, sino que te pego la rabia 🩸 y perdiste el objeto.\n")
                if len(inventario) > 0:
                    inventario[0][1] = max(0, inventario[0][1] - 1)
                    print(f"Has perdido 1 {inventario[0][0]}")
            break

        elif opcion == "3":
            talentos[7][1] += 1
            print("\n¡Congratulations :)! Has ganado un punto de Confianza.\n")
            print(f"\nTe pones un paso por delante de Verónica, protegiendola por si hubiese un ataque de parte de los monos. Ella se sorprende por tu gesto.\n")
            enter()
            print("\nVerónica: ¨¿Qué haces? Te harán daño.¨\n")
            enter()
            print("\nNecesitas una tirada de 6 o más para resistir el ataque sin moverte.\n")
            dado = tirardado()

            if dado >= 6:
                print("\nLos monos lanzan un par de cocos, pero al ver que no reaccionas, se aburren y se van.\n")
                enter()
                print("\nVerónica te acaricia la cara, emocionada por ese increible gesto.\n")
                print("Verónica: ¨Nadie había hecho algo así por mí 💘... Gracias.¨\n")
                talentos[6][1] += 1
                print("¡Ganas un punto extra de Empatía por la relación entre tu y Verónica!\n")
                inventario.append(["Coco", 1])
            else:
                print("\nUn coco te da justo en la el hombro, y este se te sale. ¡Duele muchísimo 😭😭!\n")
                enter()
                print("\nDe la reacción dolorosa te caes al suelo y los monos aprovechan para robarte mientras estás inmovil.\n")
                if len(inventario) > 1:
                    inventario[1][1] = max(0, inventario[1][1] - 1)
                    print(f"Te robaron 1 {inventario[1][0]}")
                else:
                    print("Por suerte no tenías mucho que robar JAJAJAJA.")
            break

        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

    print("\nCuando el caos termina, ambos os sentáis en la arena, reflexionando lo vivido.\n")
    enter()
    print(f"\nVerónica mira el mar desconcertadamente.\n")
    enter()
    print(f"\n{nombrejugador}: Oye, ¿estás bien? Fue intenso, pero ya termino todo, estamos bien.\n")
    enter()
    print("\nVerónica cierra los ojos y suspira.\n")
    enter()
    print("\nVerónica: ¨No son los monos, ni las ganas de comer ... es la isla, es el ruido 😢.¨\n")
    enter()
    print("\nVerónica: ¨En mi vida de antes, siempre había ruido. Que sí el tráfico de Madrid, sus barrios llenos de música látina, los exhibicionistas de la Gran Vía, teléfonos... Y yo solo sabía quejarme.¨\n")
    print("\nVerónica: ¨Y ahora... este silencio, esta calma que se respira en la isla me está matando. Me hace pensar demasiado en todo lo que he perdido estos años.¨\n")
    enter()

    while True:
        print("\nVerónica esta triste y reflexiva.")
        print("1. 'El silencio es bueno. Quiere decir que no hay más aviones cayéndose ni gente gritando.'")
        print("2. 'Yo puedo cantarte algo si quieres. ¿Te sabes alguna canción?'")

        opcion = input("Elige el numero que deseas decir (1 o 2): ")

        if opcion == "1":
            print(
                f"\n{nombrejugador}: El silencio es bueno, Vero. Significa que estamos vivos.\n")
            enter()
            print("\nVerónica te mira y saca una falsa sonrisa.\n")
            enter()
            print("\nVerónica se levanta, se sacude la arena con una nueva energía, una energía limpia .\n")
            enter()
            print("\nVerónica: ¨Vale, basta de lloros!. Vamos a abrir esos cocos antes de que vuelvan los monos 😊.¨\n")
            break

        if opcion == "2":
            print(f"\n{nombrejugador}: ¡Yo soy el Julio Iglesias del siglo XXI! *Empiezas a tararear una horrible canción y a tocar las palmas desigualmente*\n")
            enter()
            print("\nVerónica estalla en carcajadas. Es una risa genuina que espanta el silencio pesado.\n")
            enter()
            print(f"\nVerónica: ¨¡Por favor, para 🤣!¨ (Se ríe) ¨Vale, vale, prefiero el silencio a que cantes.¨\n")
            enter()
            print(f"\nVerónica: ¨Gracias, {nombrejugador}. Me has hecho olvidarme de todo estoo.¨\n")
            print("Sus ojos brillan, ya no de lágrimas, sino de tranquilidad y felicidad.\n")
            break

        else:
            print("Opción no válida. Por favor, ingresa 1 o 2.")

    print("\nYa esta atardeciendo, por lo que deciden volver al campamento antes de que caiga la noche, debes buscar comida en otros lugares de la isla 🏝️.\n")

    return talentos, inventario

def montana(talentos, inventario, nombrejugador):

    indice_ego = 9
    indice_rebeldia = 4
    indice_sarcasmo = 8

    print("\n--- ESCENA: ENCUENTRO EN LA MONTAÑA ---\n")
    enter()
    print("""
    ====================================================================================================
    ================================================+*.#++==============================================
    ===============================================+#  .*+==============================================
    ====================**:=#+===================+*:   .:-*=================+*+*++======================
    ===================*     :+:++===============*      :::*+++============*.    #+*+===================
    ================+-            *+===========+-       .:::=+=========++#.-         :+=================
    ==============+:-: :---------:. *++=======#         .:::::#=======*=-   .::..---- .-*===============
    ==============+%*+****+++++++++*#++=====+#           ::::::*+=====*=----------------#===============
    ================+++++++++++++**=+++====*=  +==   *%  .-%:@#-=*=====+++=+++++++++++++================
    ==========+===============++# .#+++===#-+#====-.++##=.%#*%%%%#%++====+-.#+==============+=:#+=======
    =======+*   *+++==========+-   :++++++-=======++=*######%=%%%%%@++++*   :++===========*+      =+++==
    =====+*-        *========*     ::-##-============######%+#*%%%%%%#+*    .:-#===#*+==#:. :-------+++=
    ===+#:. -------  .*====+#-=-.*##%%#-============+%########*%@%%%%%=      :::%+* :#==+***********+===
    ====*#############+===+===--+##%@==+=========*+%##########%%%%%%@: =.  +  -*:#. .:+++===============
    ====================+#-+++*#####-=+=======+=*%###########%%%%%%%=+*=+ #*#.*#%%%- :::*=+=============
    ===================+*=*+**####+=====++=+++*##########+##%%%%%%+=+====*=*###*#%%%@*##*%+=============
    ============++====*=*######%@**#**#-##*#############**#%%%%%%==++======**####%%%%@%#%%@++===========
    ===========*=*++=#**#####%%=:+++=*###########%*-:::::=#%%%%*=+=++=+*==#-=%##%%%%%%%%#%%%*===========
    ==========+*-+**%-=%##%=%% *====##########@+:::==::++++++%+=+=*#=*-+*==**#%#--%%%%=+@%%@@#==========
    ======+#++%+*=%#++*+@@-+#:+====%#######%*+=++++++++++++++++#*+-=%***%%****#+=**%%=*+@%%%=@@+*+======
    ======*-#***+++@*#***%***#====%##%@%=----:::::::::---+%%*++++**+##*######*%+***%**#+#@%*++%%-*======
    ====+#+++*=+#*##****+##*#%*##=-----------------------::::::=#*##*%%@#+=*#*+##***%+%#%%#+**%++**=====
    ====+#**=%+##+-=#@@==-*@---+#=--------------*#*%=----======--=+#+=*#-::*%-+*%@*@+=*#+*#*##*+++%=====
    =====%@@@%#%#==--%%===============----+#@#--*%@@@====++==========++***+=====%%------#%++#%@@@@%=====
    ====###*+++++++*###**+=======##======*%+%++%%%@*@*===++=================**=++++++--+#++**#%###%#+===
    =+@**###########*******************%@%*==+**#%##@@%%=================************#+++*@##########@+=
    ===========++++++++++++++*%%%%%%%%@##@*###%%%%@##%%%%%%%%%%%%%%%%%%%%%%%%%#+++++++++++++++++++=+++==
    =============================================================================+======================
    ====================================================================================================
    """)
    enter()

    print("El aire frío de la montaña 🏔️ te corta un poco la respiración mientras avanzas entre los arbustos húmedos.\n")
    enter()
    print("\nLlevas horas buscando algo que pueda servir de comida: frutas silvestres, raíces, lo que sea. La isla no da muchas opciones, y Paco, Verónica y Blanca se están quedando sin fuerzas.\n")
    enter()
    print("\nSuspiras, frustrado/a.\n")
    enter()
    print("\nJusto entonces escuchas un crujido entre las rocas.\n")
    enter()
    print("\n—¿Quién anda ahí? —preguntas, tensando los hombros.\n")
    enter()
    print("\nUna figura sale de entre los árboles, tranquila como si hubiera estado paseando por un parque y no sobreviviendo a un naufragio.\n")
    enter()
    print("\n¡Es Eliel!\n")
    enter()
    print("\nLa luz se cuela entre las hojas 🌿 y le ilumina el rostro: sereno, con esa mirada cálida que siempre te hace sentir que las cosas van a estar bien. Lleva una pequeña bolsa tejida con hojas, ligeramente abultada.\n")
    enter()
    print("\nEliel: ¨Vaya… no esperaba encontrar a nadie por aquí. Pensé que estabas buscando cerca del río.¨")
    print("\nTe observa con atención, evaluando si estás bien.\n")
    enter()
    print("\nEliel: ¨Encontré algunas frutas 🍇🍈🍌¨ —alza la bolsa—. ¨No son muchas, pero servirán para hoy. ¿Y tú? ¿Has encontrado algo?¨\n")
    enter()
    print("\nTe quedas mirándolo. Ese tono suave, esa calma… Te desespera y te tranquiliza al mismo tiempo.\n")
    enter()
    print("\nEliel inclina un poco la cabeza 🙂‍↕️, esperando tu respuesta.\n")
    while True:
        print(f"1.\n   —Obvio que encontré cosas. Yo siempre puedo con esto… no como algunos.")
        print("2.\n   —No mucho… pero al menos ya sé dónde no buscar.")
        print("3.\n   —¿Tú estás bien? Pareces cansado. No esperaba verte tan lejos.")

        opcion = input("\nElige el número de la opción que deseas responder: ")

        if opcion == "1":
            talentos[indice_ego][1] += 1
            print("\nHas ganado un punto de EGO gracias a esta decisión.\n")
            enter()
            print(f"\n{nombrejugador}:Obvio que encontré cosas. Yo siempre puedo con esto… no como algunos.\n")
            enter()
            print("\nEliel te mira por un instante, con una pizca de tristeza en su calma habitual.\n")
            enter()
            print("\nEliel: ¨Me alegra 😀 que seas tan autosuficiente, pero recuerda que un grupo sobrevive mejor que uno solo. Nos vemos en el campamento 🏕️.¨\n")
            break

        elif opcion == "2":
            print(f"\n{nombrejugador}:No mucho… pero al menos ya sé dónde no buscar.\n")
            enter()
            print("\nEliel asiente con comprensión.\n")
            enter()
            print("Eliel: ¨Es una buena actitud. No pierdas la esperanza, siempre hay algo más allá de la siguiente roca. Ven, te acompaño un poco y te muestro dónde encontré esto.¨\n")
            enter()
            print("Sientes un pequeño alivio al tener a Eliel a tu lado. La montaña 🏔️ se siente menos hostil.\n")
            break

        elif opcion == "3":
            print(f"\n{nombrejugador}:¿Tú estás bien? Pareces cansado. No esperaba verte tan lejos.\n")
            enter()
            print("\nEliel sonríe ligeramente, y por un momento, su mirada parece cansada.\n")
            enter()
            print("\nEliel: ¨Estaré bien. Es solo que la responsabilidad pesa. No te preocupes por mí. Concentrémonos en volver con comida 🥖🥕.¨\n")
            enter()
            print("\nSu respuesta no te convence del todo, pero decides no insistir.\n")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    print("\nLuego de tu respuesta en el encuentro, Eliel sonríe ligeramente y ajusta la bolsa de frutas sobre su hombro.\n")
    enter()
    print("\nEliel: ¨Ven, vamos de vuelta. No está lejos, pero es mejor ir con cuidado. El camino a veces engaña.¨\n")
    enter()
    print("\nCamináis juntos, el silencio solo roto por el crujido de las hojas secas 🍂 bajo vuestros pies.\n")
    enter()
    print("\nDespués de unos minutos, Eliel se detiene y señala una zona de matorrales cerca de un gran tronco caído.\n")
    enter()
    print("\nEliel: ¨Aquí encontré estas bayas 🫐, pero tuve que tener mucho cuidado. Algunas plantas de este lado de la montaña pueden ser venenosas si te equivocas. ¿Ves la diferencia entre estas y aquellas?¨\n")
    enter()
    print("\nTe muestra dos tipos de bayas muy parecidas, que solo se distinguen por un sutil patrón de puntos en la piel.\n")
    enter()
    print("\nEliel: ¨Creo que sería bueno que todos aprendiéramos a diferenciarlas, por si alguien más tiene que buscar comida solo.¨\n")
    enter()
    print("\nTe está invitando a tomarte el tiempo para aprender, pero sabes que el campamento 🏕️ los espera y que Blanca no está bien.\n")
    enter()
    print("\nMientras miras las bayas y a Eliel, notas que en el tronco 🪵 caído hay un pequeño cuchillo 🔪 artesanal, probablemente dejado allí por Eliel en un descuido. Podría ser muy útil, pero él no lo ha notado.\n")
    enter()
    print("\nEliel espera pacientemente tu respuesta, sin dejar de mirar la diferencia entre las bayas.\n")

    while True:
        print("\n--- Decisión en el Sendero ---\n")
        print(
            f"1.\n   —No tenemos tiempo para clases de botánica, Eliel. Necesito ese cuchillo para cortar leña. ¡Date prisa! (Tomas el cuchillo sin que te vea).")
        print(
            "2.\n   —¿Esperas que recordemos un patrón de puntos en bayas cuando apenas recordamos nuestros nombres? Eres un idealista.")
        print(
            "3.\n   —Sí, entiendo la diferencia. Es buena idea enseñarlo a todos, pero ahora volvamos. Blanca necesita esta comida ya.")

        opcion2 = input("\nElige el número de la opción que deseas responder: ")

        if opcion2 == "1":
            talentos[indice_rebeldia][1] += 1
            equipo.append(["Cuchillo artesanal", 1])
            print("\nHas ganado un punto de REBELDÍA y has añadido 'Cuchillo artesanal' a tu equipo\n.")
            enter()
            print(f"\n{nombrejugador}:—No tenemos tiempo para clases de botánica 🪴, Eliel. Necesito ese cuchillo para cortar leña. ¡Date prisa!\n")
            enter()
            print("\nEliel se sobresalta por tu tono, pero asiente, guardando las bayas 🫐 rápidamente. Parece preocupado por tu repentina impaciencia.\n")
            break

        elif opcion2 == "2":
            talentos[indice_sarcasmo][1] += 1
            print("\nHas ganado un punto de SARCASMO gracias a esta decisión.\n")
            enter()
            print(f"\n{nombrejugador}:—¿Esperas que recordemos un patrón de puntos en bayas cuando apenas recordamos nuestros nombres? Eres un idealista.\n")
            enter()
            print("\nEliel sonríe con resignación, sin ofenderse, pero un poco decepcionado. Toma las bayas 🫐 y se pone en marcha.\n")
            break

        elif opcion2 == "3":
            print(f"\n{nombrejugador}:—Sí, entiendo la diferencia. Es buena idea enseñarlo a todos, pero ahora volvamos. Blanca necesita esta comida ya.\n")
            enter()
            print("\nEliel te dedica una mirada agradecida por tu preocupación. Asiente y retoma el camino 🚶‍♂️ rápidamente.\n")
            break

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    enter()
    print("\nRetomáis el camino de vuelta, acelerando el paso. La esperanza de llevar comida al campamento 🏕️ hace el descenso más ligero.\n")
    enter()
    print("\nCamináis juntos, el silencio solo roto por el crujido de las hojas secas bajo vuestros pies.\n")
    enter()
    print("\nEl camino se hace más fácil a medida que descendéis, pero una sensación de tensión os envuelve.\n")
    enter()
    print("\nA pocos metros de la entrada al campamento, una niebla extraña 🌫️ os envuelve. De la niebla emerge la figura translúcida de una mujer con adornos de la isla, flotando sobre el sendero.\n")
    enter()
    print("\nEspíritu: ¨¡Tú, superviviente! Me atrae lo que llevas. Dame lo que más valoras de tu inventario o haz un trato conmigo.¨\n")
    enter()
    print("\nEl espíritu te está pidiendo un duelo directo por tus pertenencias. Te señala y exige un juego de 'Piedra, Papel o Tijera'.\n")
    enter()
    print("\nEliel (con temor): ¨Es el Espíritu de la Cosecha. Juega limpio. Si ganas, te dará un regalo. Si pierdes, tendrás que entregarle algo. ¡No la ofendas!¨\n")
    enter()

    while True:
        print("\n--- Decisión frente al Espíritu ---")
        print(f"1.\n   —¿Un juego de niños? Bien, juguemos por todo.")
        print("2.\n   —¿Estás segura? No quiero ganarle a una aparición. No sería justo.")
        print("3.\n   —Acepto el desafío. Pero que sea rápido.")

        opcion3 = input("\nElige el número de la opción que deseas responder: ")

        if opcion3 == "1":
            talentos[indice_rebeldia][1] += 1
            print("\nHas ganado un punto de REBELDÍA.")
            break
        elif opcion3 == "2":
            talentos[indice_sarcasmo][1] += 1
            print("\nHas ganado un punto de SARCASMO.")
            break
        elif opcion3 == "3":
            print("\nAceptas el desafío con seriedad.")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

    enter()
    print("\n--- ¡Desafío de la Cosecha! Una ronda de Piedra, Papel o Tijera. ---\n")
    enter()

    resultado_espiritu = jugar_ppt_escena()

    if resultado_espiritu == "Ganaste":
        print("\n¡Ganaste al Espíritu de la Cosecha! Su figura se disuelve en un resplandor verde.\n")
        enter()
        print("\nEspíritu: ¨Eres digno. Toma esto y que te sirva.¨")
        enter()
        equipo.append(["Hacha primitiva", 1])
        print("\n[Has añadido 'Hacha primitiva' a tu inventario (Equipo).] ¡Un valioso premio!\n")
        enter()

    elif resultado_espiritu == "Perdiste":
        print("\n¡Perdiste contra el Espíritu de la Cosecha! La figura se ríe con un sonido hueco.\n")
        enter()

        print("\nEl espíritu te exige tu objeto más antiguo, el que ha absorbido más energía de la isla 🏝️.\n")

        if inventario:
            objeto_perdido = inventario.pop(0)
            print(f"\n[Has perdido {objeto_perdido[0]} (x{objeto_perdido[1]}) de tu inventario.]\n")
        else:
            print("\nTu inventario está vacío. El espíritu te quita un poco de tu energía vital.\n")

        enter()

    else:
        print("\nEl Espíritu acepta el empate. Su figura se disuelve lentamente. Te mira con desinterés.\n")
        enter()
        print("\nEspíritu: ¨Vete. No pierdas más mi tiempo.¨\n")
        enter()

    print("\nFinalmente, Eliel y tú entráis a la zona del campamento. El sol ☀️ está a punto de ocultarse. El día ha sido largo y peligroso.\n")
    enter()

    ensenartalentos(talentos)
    print("\nEste es tu equipo:\n")
    enseñarequipo(equipo)
    print(f"\nHas terminado tu momento con Eliel, debes buscar comida en otros lugares de la isla 🏝️.\n")
    return talentos, inventario, equipo

def noche(inventario, talentos, nombrejugador):
    print("\n--- NOCHE ---\n")
    print(f"\nAl regresar al campamento despues de todas estas aventuras te sientes cansado.\n")
    enter()
    print("\nTe sientas en la arena junto a Paco y Veronica ⛱️.\n")
    enter()
    print("\nBlanca y Eliel te sonríen desde la fogata 🔥 que están haciendo.\n")
    enter()
    print("\nAunque conseguiste un par de cosas de comer sabes que no será suficiente para llenar el estómago de ninguno.\n")
    enter()
    print(f"\nPaco mira lo poco que le queda para comer, con una mirada reflexiva 😒.\n")
    print(f"\nPaco: ¨¿Es en serio? Mi gato 🐈‍⬛ come mejor que esto, y eso que es callejero.¨\n")
    enter()
    print(f"\nVerónica, por otro lado, se ve pálida. Intenta sonreír, pero le tiemblan las manos al sostener su parte.\n")
    print(f"\nVerónica: ¨Está bien, Paco. Al menos tenemos algo... aunque me siento un poco mareada.¨\n")
    enter()
    print(f"\nEliel y Blanca observan al grupo, esperando ver cómo reaccionas ante la escasez.\n")
    enter()
    while True:
        print("\nLa tensión por el hambre es palpable. ¿Qué haces?")
        print("1. Cederle tu parte de la comida a Verónica.")
        print("2. Hacer un chiste sobre la 'cocina de autor' minimalista para animar a Paco.")
        print("3. Proponer a Eliel un sistema de racionamiento estricto para que dure más.")

        opcion = input("Elige el número de tu acción (1, 2 o 3): ")

        if opcion == "1":
            talentos[6][1] += 1
            print(f"\n¡Has ganado un punto de Empatía!\n")
            print(f"\n{nombrejugador}: Verónica, toma lo mío. Yo aguantaré hasta mañana. Tú lo necesitas más.\n")
            enter()
            print(f"\nVerónica te mira con los ojos llorosos 🥹 y acepta la comida agradecida.\n")
            print(f"\nVerónica: ¨Gracias, {nombrejugador}. De verdad... no sé qué haría sin ti.¨\n")
            enter()
            print(f"\nBlanca asiente desde la fogata 🔥, aprobando el gesto silenciosamente. El hambre aprieta tu estómago, pero tu conciencia está llena.\n")
            enter()
            break

        elif opcion == "2":
            talentos[5][1] += 1
            print(f"\n¡Has ganado un punto de Sentido del Humor 🤣!\n")
            print(f"\n{nombrejugador}: Vamos, Paco. En un restaurante de lujo en París 🥐 te cobrarían 200 euros por una porción así de 'exclusiva'. Es una experiencia gourmet 🧑‍🍳.\n")
            enter()
            print(f"\nPaco suelta una carcajada, casi atragantándose con un trozo de fruta.\n")
            print(f"\nPaco: ¨¡Tienes razón! Somos unos incomprendidos culinarios. Gracias por hacerme reír, guapi.¨\n")
            enter()
            print(f"\nEl ambiente se relaja notablemente. Incluso Eliel sonríe. El hambre sigue ahí, pero el ánimo ha subido.\n")
            enter()
            break

        elif opcion == "3":
            talentos[11][1] += 1
            print(f"\n¡Has ganado un punto de Controlador/a!\n")
            print(f"\n{nombrejugador}: Eliel, esto no puede seguir así. Necesitamos cronometrar las comidas y dividir las calorías equitativamente.\n")
            enter()
            print(f"\nEliel te mira con seriedad y asiente, sacando una pequeña libreta 📓 (quién sabe de dónde).\n")
            print(f"\nEliel: ¨Estoy de acuerdo. Me gusta cómo piensas, {nombrejugador}. Necesitamos orden en el caos.¨\n")
            enter()
            print(f"\nPaco rueda los ojos murmurando 'qué aburridos', pero nadie discute tu lógica. Te sientes en control de la situación.\n")
            enter()
            break

        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

    print("\nLa noche cae sobre la isla 🌕. El fuego se consume lentamente mientras todos intentan dormir.\n")
    return talentos, inventario
def cantomisterioso(inventario, talentos, nombrejugador):
    enter()
    print("\nEs tarde. La fogata se ha reducido a unas pocas brasas rojas que palpitan como un corazón cansado.\n")
    enter()
    print("\nEstán todos recostados, intentando dormir, cuando de repente el viento cambia de dirección.\n")
    enter()
    print("\nDesde el mar 🌊, llega una voz. No es el viento 🍃. Es una melodía... humana, pero extraña. Triste y hermosa a la vez.\n")
    enter()

    print(f"\nBlanca se incorpora de inmediato, con los ojos muy abiertos.\n")
    print(f"\nBlanca: ¨¿Lo escuchan? Es un sol menor... pero vibra como si estuviera bajo el agua. Es... azul oscuro.¨\n")
    enter()

    print(f"\nVerónica se pone de pie de un salto, agarrando un palo afilado que usa de lanza.\n")
    print(f"\nVerónica: ¨¿Quién anda ahí? ¡Si es una broma, no tiene gracia!¨ —su voz es un rugido defensivo.\n")
    enter()

    print(f"\nPaco se esconde ligeramente detrás de Eliel, aunque intenta que parezca una pose relajada.\n")
    print(f"\nPaco: ¨Tranquilos, tranquilos... Seguro es una sirena 🧜 que ha olido mi colonia. No es ego, es que huelo genial.¨\n")
    enter()

    print(f"\nEliel levanta una mano pidiendo silencio.\n")
    print(f"\nEliel: ¨No tiene sentido. No hemos visto barcos ⛵ en semanas. Esa voz... no debería estar ahí. Debemos tener cuidado.¨\n")
    enter()

    while True:
        print("\nTodos te miran a ti, esperando el voto decisivo sobre cómo actuar.")
        print("1. 'Blanca tiene razón, la melodía es hipnótica. Hay que ir a ver, podría ser alguien que necesita ayuda.'")
        print("2. 'Verónica, baja el palo. Si es hostil, ya nos habría atacado. Vamos a investigar con cabeza.'")
        print("3. 'Paco, si es una sirena, te usaremos de cebo. ¡Vamos a ver qué demonios es eso!'")

        opcion = input("Elige el número de tu reacción: ")

        if opcion == "1":
            talentos[10][1] += 1
            talentos[6][1] += 1
            print("\n¡Has ganado puntos de Sensibilidad y Empatía 😀!\n")
            print(f"\nBlanca te sonríe, agradecida de que valides su intuición.\n")
            print(f"\nBlanca: ¨Sabía que tú también sentías ese 'algo'. No es peligro, es... soledad.¨\n")
            enter()
            print(f"\nVerónica respira, pero baja el arma ligeramente. ¨Vale, pero si intenta morderte, le rompo la cabeza.¨\n")
            break

        elif opcion == "2":
            talentos[2][1] += 1
            talentos[11][1] += 1
            print("\n¡Has ganado puntos de Inteligencia y Controlador!\n")
            print(f"\nEliel asiente, satisfecho con tu prudencia.\n")
            print(f"\nEliel: ¨Exacto. Movernos sin evaluar la situación es un error. Vamos en formación cerrada.¨\n")
            enter()
            print(f"\nVerónica asiente con respeto. ¨Bien. Tú mandas, pero yo voy delante.¨\n")
            break

        elif opcion == "3":
            talentos[5][1] += 1
            talentos[4][1] += 1
            print("\n¡Has ganado puntos de Sentido del Humor y Rebeldía!\n")
            print(f"\nPaco suelta una carcajada nerviosa.\n")
            print(f"\nPaco: ¨¡Jaja! ¡Claro! Sacrifiquemos al más guapo. Clásico. Pero voy... solo para que no se pierdan.¨\n")
            enter()
            print(f"\nBlanca se ríe 🤣 por lo bajo. ¨El sarcasmo te queda bien, {nombrejugador}. Aligera el miedo.¨\n")
            break
        else:
            print("Opción no válida.")

    print("\nEl grupo decide adentrarse en la oscuridad hacia la playa 🏖️. La luna 🌕 está oculta tras nubes densas.\n")
    enter()
    print("\nCaminan entre la maleza. Eliel va marcando el paso, Verónica vigila los flancos, Blanca mira las sombras fascinada y Paco va tropezando con todo.\n")
    enter()

    print("\nLa voz se hace más fuerte. Es un canto melancólico 🎶🎵, sin letra inteligible, pero que eriza la piel.\n")
    enter()
    while True:
        print(f"\nEstán cerca de la línea de árboles 🌴 que da a la arena. Deben decidir cómo asomarse.\n")
        print(f"\nEliel susurra: ¨Si salimos todos a la vez, seremos un blanco fácil.¨\n")
        print("1. Intentar acercarse reptando en silencio absoluto para ver sin ser vistos.")
        print("2. Salir caminando con confianza y gritando '¡HOLA!'. Que sepan que no tenemos miedo.")
        print("3. Analizar el entorno: buscar huellas 👣 o señales antes de salir a la arena.")

        opcion = input("Elige tu estrategia (1, 2 o 3): ")

        if opcion == "1":
            print("\nDeciden usar el sigilo. Eliel y Blanca son buenos en esto, pero Paco es torpe.\n")
            enter()
            print("Necesitas sacar 5 o más en el dado para que Paco no pise una rama seca.")
            tirardado()
            dado = random.randint(1, 10)
            print(f"\n¡Sacaste {dado} 🎲!")

            if dado >= 5:
                print("\n¡Éxito! Logran llegar hasta unos matorrales al borde de la playa 🏖️ sin hacer ruido.\n")
                talentos[11][1] += 1
                print("\nGanas un punto de Controlador por la buena gestión del grupo.\n")
            else:
                print("\n¡CRACK! Paco pisa una hoja de palma seca que suena como un disparo 🔫.\n")
                print("\nPaco: ¨¡Ups! Fue... ¿el viento?¨\n")
                print("\nEl canto se detiene de golpe.\n")

                talentos[7][1] -= 1
                print("\n¡Oops! Perdiste un punto de Confianza\n")
            break

        elif opcion == "2":
            talentos[4][1] += 1
            print("\n¡Ganas un punto de Rebeldía!\n")
            print(f"\n{nombrejugador}: ¡A la mierda el sigilo! ¡Somos los dueños de esta isla!\n")
            print("\nVerónica sonríe 😁 con fiereza: ¨¡Así se habla!¨\n")
            enter()
            print("\nSalen a la playa 🏖️ pisando fuerte. El canto se corta abruptamente.\n")
            break

        elif opcion == "3":
            talentos[3][1] += 1
            print("\n¡Ganas un punto de Detallismo!\n")
            print(f"\nTe detienes a mirar la arena antes de salir. Blanca se agacha a tu lado.\n")
            enter()
            print("\nBlanca: ¨Mira... la arena está removida aquí. Y hay... ¿brillantina? No, son escamas fosforescentes.¨\n")
            enter()
            print("Inventario actualizado: Recoges unas Escamas Raras del suelo.")
            inventario.append(["Escamas Raras", 3])
            abreinventario(inventario)
            print("\nCon esta pista, avanzan con cuidado.\n")
            break
        else:
            print("Opción no válida.")
    return inventario, talentos
def intercambiomar(inventario, talentos, nombrejugador, equipo):
    print(f"\nTodos caminan lentamente, buscando averiguar qué es lo que está pasando. \n")
    enter()
    print(f"\nMientras más se acercan a la orilla del mar, más frío ❄️ se siente. \n")
    enter()
    print(f"\nSientes un escalofrío recorrer tu cuerpo. \n")
    enter()
    print("\nAl llegar a la orilla, la voz se ha silenciado. Hay un silencio espeso, solo roto por el sonido de las olas lamiendo la arena.\n")
    enter()
    print("\nBlanca se arrodilla junto al agua y señala un punto donde las olas crean un remolino inusual, como si algo estuviera succionando el agua.\n")
    print(f"\nBlanca: ¨Miren. El agua se ve diferente ahí. Es más oscura, casi tinta. Siento... que pide algo. Es como un hueco hambriento en el mar 🌊.¨\n")
    enter()
    print(f"\nEliel se acerca y ve unas conchas dispuestas en un patrón circular.\n")
    print(f"\nEliel: ¨Es un arreglo artificial. Un ritual. Se ha dejado algo aquí... y se ha tomado algo a cambio. Es una ofrenda.¨\n")
    enter()
    print(f"\nVerónica: ¨¿Una ofrenda? ¿Y si le ofrezco mi lanza? Capaz me da un misil balístico.¨ (Se ríe 🤣, pero está seria.)\n")
    enter()
    print(f"\nTodos te miran. Es obvio que este remolino es el origen del canto, y es un lugar de poder.\n")
    while True:
        print("\n🌊 La Tienda del Mar 🌊")
        print("El remolino parece dispuesto a tomar un objeto de tu Inventario y, a cambio, ofrecerte una recompensa, si superas el desafío de suerte.")
        print("1. Hacer una Ofrenda: Abrir tu inventario y elegir un objeto para dar al mar.")
        print("2. No arriesgarse: Dejar el lugar y volver al campamento.")

        opcion_ritual = input("¿Qué decides? (1 o 2): ")

        if opcion_ritual == "2":
            print("\nDecides que el riesgo es demasiado grande. El grupo se aleja del remolino, sintiendo un escalofrío en la espalda.\n")
            print("\nEl canto, muy débil, parece lamentar su partida. Vuelven a dormir, más cautelosos que antes.\n")
            break

        elif opcion_ritual == "1":
            if not inventario:
                print("\n🚫 Tu inventario está vacío. No tienes nada que ofrecerle al mar.")
                enter()
                continue

            print("\n--- Tu Inventario Actual ---")
            abreinventario(inventario)
            print("----------------------------\n")

            while True:
                try:
                    opciones_validas = {str(i + 1): item[0] for i, item in enumerate(inventario)}

                    eleccion_ofrenda = input("Elige el número del objeto que quieres ofrendar según su orden (o 'c' para cancelar): ")

                    if eleccion_ofrenda.lower() == 'c':
                        print("\nDecides no hacer una ofrenda por ahora.\n")
                        break

                    if eleccion_ofrenda in opciones_validas:
                        nombre_objeto_ofrenda = opciones_validas[eleccion_ofrenda]

                        indice_a_remover = -1
                        for i, item in enumerate(inventario):
                            if item[0] == nombre_objeto_ofrenda:
                                indice_a_remover = i
                                break

                        if indice_a_remover != -1:
                            objeto_ofrenda = inventario.pop(indice_a_remover)
                            print(f"\nOfreces {objeto_ofrenda[0]} al remolino. El objeto cae y es tragado por el agua oscura sin un solo chapoteo.\n")
                            enter()
                            recompensas = [
                                ["Arco de Hueso de Kraken (Arma)", 1],
                                ["Lanza Imbuida (Arma)", 1],
                                ["Piedra de la Claridad (Objeto Mágico)", 1],
                                ["Poción de Vitalidad (Consumible)", 1],
                                ["Anillo de Coral (Protección)", 1]
                            ]

                            print("\nEl remolino comienza a brillar con una luz azul intenso. De las profundidades se escuchan susurros, y el mar te ofrece una elección:\n")

                            print("--- Recompensas del Mar 🌊 (Elige lo que quieres intentar ganar) ---")
                            for i, item in enumerate(recompensas):
                                print(f"{i + 1}. {item[0]}")
                            print("------------------------------------------------------------------\n")

                            while True:
                                try:
                                    eleccion_recompensa = int(input("Elige el número de la recompensa que deseas obtener: "))
                                    if 1 <= eleccion_recompensa <= len(recompensas):
                                        recompensa_elegida = recompensas[eleccion_recompensa - 1]
                                        print(f"\nHas elegido intentar ganar: {recompensa_elegida[0]}.")
                                        enter()

                                        minijuegoparoimpar(recompensa_elegida)

                                        break_inner_loop = False
                                        while True:
                                            print("\n¿Quieres intentar hacer OTRA ofrenda al remolino (y conseguir otra recompensa)?")
                                            print("1. Sí, tengo más objetos que ofrecer.")
                                            print("2. No, volvamos al campamento.")
                                            opcion_repetir = input("Elige (1 o 2): ")

                                            if opcion_repetir == "2":
                                                print("\nLa 'Tienda del Mar' cierra por esta noche. El grupo se retira.\n")
                                                enseñarequipo(equipo)
                                                return
                                            elif opcion_repetir == "1":
                                                if not inventario:
                                                    print("\n🚫 Tu inventario está vacío. No tienes más objetos que ofrecer. Es hora de volver.\n")
                                                    return
                                                print("\n¡Muy bien! Busca tu próxima ofrenda.")
                                                break_inner_loop = True
                                                break
                                            else:
                                                print("Opción no válida. Por favor, elige 1 o 2.")
                                        if break_inner_loop:
                                            break
                                    else:
                                        print("Opción de recompensa no válida.")
                                except ValueError:
                                    print("Por favor, introduce el número de la recompensa.")
                        break
                    else:
                        print("Opción de ofrenda no válida.")
                except ValueError:
                    print("Por favor, introduce el número de la ofrenda (o 'c' para cancelar).")
        else:
            print("Opción no válida. Por favor, elige 1 o 2.")

    print("\nEl canto misterioso ha terminado, por ahora. El grupo se prepara para lo que venga mañana.")
    enseñarequipo(equipo)
    return inventario, talentos, equipo

def traicion_campamento(inventario, talentos, nombrejugador, equipo):
    while True:
        vida_jugador = 100
        vida_max_jugador = 100

        print(f"\n{'=' * 50}")
        print("🌹 CAPÍTULO: LA NIEBLA DE LA TRAICIÓN 🌹")
        print(f"{'=' * 50}\n")

        print(
            f"\nTe despiertas con un dolor de cabeza punzante. No hay gritos de guerra, solo el sonido irritante de voces discutiendo en voz baja junto a las brasas moribundas.\n")
        enter()


        print("--- ¿A quién protegerás (y elegirás como pareja)? ---")
        print("1. Eliel (El Místico)")
        print("2. Verónica (La Guerrera)")
        print("3. Paco (El Gigante)")
        print("4. Blanca (La Superviviente)")

        # Validación para la elección inicial de pareja
        while True:
            eleccion_amor = input("Elige (1-4): ")
            if eleccion_amor in ["1", "2", "3", "4"]:
                break
            else:
                print("⚠️ Opción no válida. Debes elegir un número del 1 al 4.")

        aliado = ""
        enemigos = []

        stats_base = {
            "Eliel": {"hp": 60, "desc": "prepara conjuros inestables", "ataque": "Magia Oscura"},
            "Verónica": {"hp": 80, "desc": "busca puntos vitales con técnica militar", "ataque": "Lanza Precisa"},
            "Paco": {"hp": 100, "desc": "usa fuerza bruta descontrolada", "ataque": "Golpe Demoledor"},
            "Blanca": {"hp": 50, "desc": "se mueve rápido y ataca sucio", "ataque": "Navaja Oculta"}
        }

        if eleccion_amor == "1":
            aliado = "Eliel"
            enemigos = ["Verónica", "Paco", "Blanca"]
        elif eleccion_amor == "2":
            aliado = "Verónica"
            enemigos = ["Eliel", "Paco", "Blanca"]
        elif eleccion_amor == "3":
            aliado = "Paco"
            enemigos = ["Eliel", "Verónica", "Blanca"]
        else:
            aliado = "Blanca"
            enemigos = ["Eliel", "Verónica", "Paco"]

        print(
            f"\nTe pones del lado de {aliado}. {aliado} te mira sorprendido/a pero asiente. Juntos se enfrentan a los otros tres.\n")
        enter()

        game_over = False

        for nombre_enemigo in enemigos:
            if game_over: break

            datos_enemigo = stats_base[nombre_enemigo]
            vida_enemigo = datos_enemigo["hp"]

            print(f"\n🔴 ENFRENTAMIENTO: Tú VS {nombre_enemigo} 🔴")
            enter()

            arma_actual = "Tus puños"
            dano_arma = 5

            if equipo:
                print("\n🎒 Elige un arma de tu equipo para esta pelea: ")
                for i, item in enumerate(equipo):
                    print(f"{i + 1}. {item[0]}")

                while True:
                    try:
                        sel = int(input("Número del arma: "))
                        if 1 <= sel <= len(equipo):
                            arma_actual = equipo[sel - 1][0]
                            dano_arma = 20
                            break
                        else:
                            print("Número inválido.")
                    except ValueError:
                        print("Introduce un número.")

            while vida_enemigo > 0 and vida_jugador > 0:
                print(f"\n------------------------------------------")
                print(f"💚 Tu Vida: {vida_jugador}/{vida_max_jugador} | 💀 Vida de {nombre_enemigo}: {vida_enemigo}")
                print(f"------------------------------------------\n")

                ataques_posibles = [
                    f"{nombre_enemigo} viene a por ti gritando como un loco.",
                    f"{nombre_enemigo} te intenta pillar por la espalda.",
                    f"{nombre_enemigo} te tira arena a la cara.",
                    f"{nombre_enemigo} prepara una leche que te va a dejar tonto."
                ]
                print(f"⚠️ ¡Cuidado! {random.choice(ataques_posibles)}")

                print(f"\n¿Cómo respondes con {arma_actual}?")
                print("1. Ir a saco y chocar.")
                print("2. Esquivar el golpe y contraatacar al costado.")
                print("3. Fingir miedo para que baje la guardia y atacar.")

                while True:
                    respuesta = input("Tu táctica (1-3): ")
                    if respuesta in ["1", "2", "3"]:
                        break
                    else:
                        print("❌ Entrada inválida. Por favor, escribe 1, 2 o 3 para realizar un movimiento.")

                dado = tirardado1al20()
                dano_infligido = 0
                dano_recibido = 0
                mensaje_resultado = ""

                if dado == 1:
                    dano_recibido = random.randint(20, 30)
                    mensaje_resultado = "¡DESASTRE! Tropiezas. El enemigo te golpea con brutalidad."
                elif dado < 8:
                    dano_recibido = random.randint(10, 15)
                    dano_infligido = random.randint(0, 5)
                    mensaje_resultado = f"Fallas. {nombre_enemigo} anticipa tu movimiento."
                elif dado < 15:
                    dano_recibido = random.randint(5, 10)
                    dano_infligido = random.randint(15, 25) + dano_arma
                    mensaje_resultado = f"¡Buen movimiento! Conectas un golpe sólido."
                elif dado < 20:
                    dano_recibido = 0
                    dano_infligido = random.randint(25, 35) + dano_arma
                    mensaje_resultado = f"¡Perfecto! Castigas a {nombre_enemigo} sin piedad."
                else:
                    dano_recibido = 0
                    dano_infligido = (random.randint(25, 35) + dano_arma) * 2
                    mensaje_resultado = f"¡GOLPE MAESTRO! Impacto crítico."

                print(f"\n>>> {mensaje_resultado}")
                vida_jugador -= dano_recibido
                vida_enemigo -= dano_infligido
                enter()

            if vida_jugador <= 0:
                game_over = True
                break

        if game_over:
            print("\n💀 HAS MUERTO.")
            decision = input("¿Reintentar? (si/no): ").lower()
            if decision == 'si':
                continue
            else:
                exit()
        else:
            break

    print(f"\nEl sol sale sobre los cuerpos. {aliado} te mira fijamente...")
    enter()

    requisitos = {
        "Blanca": ["Detallismo", "Sentido del humor", "Sarcasmo"],
        "Paco": ["Ingenio", "Ego", "Sensibilidad"],
        "Eliel": ["Inteligencia", "Confianza", "Empatía"],
        "Verónica": ["Controlador/a", "Fuerza", "Rebeldía"]
    }

    req_actuales = requisitos[aliado]
    tiene_talento = True

    print(f"--- ⚖️ JUICIO DE SUPERVIVENCIA ---")
    for req in req_actuales:
        valor = next((t[1] for t in talentos if t[0] == req), 0)
        if valor >= 1:
            print(f"✅ Tienes suficiente {req}.")
        else:
            print(f"❌ Te falta {req}.")
            tiene_talento = False
    enter()

    if tiene_talento:
        print(f"\n🌟 ¡FINAL CONSEGUIDO: AMOR CANÍBAL! 🌟")
        if aliado == "Blanca":
            print("'Siempre supe que eras detallista. Ahora la isla es solo nuestra... y hay mucha carne fresca'.")
        elif aliado == "Paco":
            print("'Tu ingenio nos salvó. Ahora ellos formarán parte de nuestra cena'.")
        elif aliado == "Eliel":
            print("'Tu inteligencia guió mi mano. Los espíritus están saciados. Comamos'.")
        elif aliado == "Verónica":
            print("'Esa fuerza rebelde es lo que necesitaba. El nuevo orden empieza hoy'.")
        print("\nVivís felices para siempre como caníbales. 🍖💀")
    else:
        print(f"\n💔 FINAL TRÁGICO: LA PURGA 💔")
        if aliado == "Blanca":
            print("'¡Estás loco!'. Blanca te corta el cuello.")
        elif aliado == "Paco":
            print("'No tienes sensibilidad'. Paco te aplasta el cráneo.")
        elif aliado == "Eliel":
            print("'No hay empatía en ti'. Eliel te apuñala el corazón.")
        elif aliado == "Verónica":
            print("'Eres una amenaza'. Verónica te atraviesa con su lanza.")
        print("\nTu historia termina aquí. 🌊💀")
        exit()

    return inventario, talentos, equipo

def desayuno(inventario, talentos, nombrejugador, equipo):
    print(f"\n--- DÍA UNO ---\n")
    print(f"\nDespiertas junto con el amanecer y como todas las mañanas buscas en tu inventario para preparar el desayuno.\n")
    abreinventario(inventario)
    print(f"\n¡Ohhh no! No tienes suficiente comida 🥐🥞 para preparar un desayuno.\n")
    enter()
    print(f"\nTienes que ir buscar comida URGENTE.\n")
    ubicaciones_disponibles = ["mar", "montaña", "cueva", "playa"]

    while ubicaciones_disponibles:
        print(f"\nUbicaciones 📍 restantes: {ubicaciones_disponibles}")

        donde = input("\n¿A dónde deseas ir a buscar (Mar, Montaña, Cueva, Playa)?:\n").lower().strip()

        if donde in ubicaciones_disponibles:
            if donde == "mar":
                mar(inventario, talentos, nombrejugador)

            elif donde == "montaña":
                montana(talentos, inventario, nombrejugador)

            elif donde == "cueva":
                cueva(inventario, talentos, nombrejugador)

            elif donde == "playa":
                playa(inventario, talentos, nombrejugador)
            ubicaciones_disponibles.remove(donde)
            enter()
            print("---")
        else:
            print("Opción no válida o ya visitada. Por favor, elige una de las ubicaciones restantes.")
    print("\n¡Has explorado todas las ubicaciones posibles por hoy! Es hora de volver al campamento 🏕️.")
    noche(inventario, talentos, nombrejugador)
    cantomisterioso(inventario, talentos, nombrejugador)
    intercambiomar(inventario, talentos, nombrejugador, equipo)

    traicion_campamento(inventario, talentos, nombrejugador, equipo)

desayuno(inventario, talentos, nombrejugador, equipo)
