

import numpy as np
import random




class Tablero:
    '''
    Clase Tablero para el juego de Hundir la Flota

    Args: id_jugador, para saber de quién es el tablero

    Variables fijas:
            tamanho_tablero, será siempre 10x10
            tableros vacíos (jugador y adversario)
            barcos (diccionario: clave = nombre barcos, valor = eslora barcos)

    Return:
    '''
    tamanho_tablero = (10,10)

    tablero_jugador = np.full((10,10), " ")
    tablero_maquina = np.full((10,10), " ")

    tablero_guess = np.full((10,10), " ")

    barcos = {
            "portaviones1" : 4,
            "submarino1" : 3 ,
            "submarino2" : 3,
            "lancha1" : 2,
            "lancha2" : 2,
            "lancha3" : 2,
            "bote1" : 1,
            "bote2" : 1,
            "bote3" : 1,
            "bote4" : 1
             }

    eslora = 0



    def __init__(self, id_jugador):
        self.id_jugador = id_jugador  

    def __str__(self):
        return f'''
        **************************************************************************************************************
        Hola {self.id_jugador}!
        Bienvenid@ al juego de Hundir la Flota!
        El juego consiste en hundir los barcos de tu oponente.
        Jugarás tú contra la máquina y ambos empezaréis con los botes posicionados aleatoriamente en vuestro tablero.
        El tablero tendrá un tamaño de {self.tamanho_tablero}.
        En cada turno habrá que indicar unas coordenadas de disparo. Será:
        \t\"AGUA\" si no se alcanza ningun barco del adversario (aparecerá el símbolo \"~\"),
        \t\"TOCADO\" si el disparo coincide con una parte de un barco adversario (aparecerá el símbolo \"X\").
        Si el disparo da a un barco, el jugador puede volver a disparar.
        Si el disparo es agua, el turno pasará al otro jugador.
        Gana quien hunde primero todos los barcos del adversario.
        !Adelante, empiezas tú!
        **************************************************************************************************************
        '''


    def inicializar_tablero_automatico_jugador(self):
        print(f"\nInicializando tablero de {self.id_jugador}...\nBarcos posicionados aleatoriamente:")
        eslora = 0
        for pos,value in enumerate(self.barcos):
            #defino lista de orientaciones desde las que elegir a random
            orient = random.choice(["N", "E", "S", "O"])
            #posición inicial de cada barco
            init_pos = np.random.randint(10, size=2)
            row = init_pos[0]
            col = init_pos[1]
            #defino posiciones desde punto inicial (para los barcos con eslora de 2 a 4)
            orient_N = self.tablero_jugador[row : (row - eslora) : -1 , col]
            orient_E = self.tablero_jugador[row, col : (col + eslora)]
            orient_S = self.tablero_jugador[row : (row + eslora) , col]
            orient_O = self.tablero_jugador[row, col : (col - eslora) : -1]

            #posición del barco de eslora = 4, a random
            if pos == 0:
                eslora = 4
                bandera = False
                while bandera == False:
                    if orient == "N" and 0<= (row - eslora) < 10:
                        self.tablero_jugador[row : (row - eslora) : -1 , col] = "4"
                        print(value, init_pos, "norte")
                        bandera = True
                    elif orient == "E" and 0<= (col + eslora) < 10:
                        self.tablero_jugador[row, col : (col + eslora)] = "4"
                        print(value, init_pos, "este")
                        bandera = True
                    elif orient == "S" and 0<= (row + eslora) < 10:
                        self.tablero_jugador[row : (row + eslora) , col] = "4"
                        print(value, init_pos, "sur")
                        bandera = True
                    elif orient == "O" and 0<= (col - eslora) < 10:
                        self.tablero_jugador[row, col : (col - eslora) : -1] = "4"
                        print(value, init_pos, "oeste")
                        bandera = True
                    else:
                        orient = random.choice(["N", "E", "S", "O"])
                        init_pos = np.random.randint(10, size=2)
                        row = init_pos[0]
                        col = init_pos[1]
                        orient_N = self.tablero_jugador[row : (row - eslora) : -1 , col]
                        orient_E = self.tablero_jugador[row, col : (col + eslora)]
                        orient_S = self.tablero_jugador[row : (row + eslora) , col]
                        orient_O = self.tablero_jugador[row, col : (col - eslora) : -1]
            #posición de los 2 barcos de eslora = 3, a random
            if 1 <= pos < 3:
                eslora = 3
                bandera = False
                while bandera == False:
                    if orient == "N" and 0<= (row - eslora) < 10 and "3" not in orient_N and "4" not in orient_N:   
                        self.tablero_jugador[row : (row - eslora) : -1 , col] = "3"
                        print(value, init_pos, "norte")
                        bandera = True
                    elif orient == "E" and 0<= (col + eslora) < 10 and "3" not in orient_E and "4" not in orient_E:
                        self.tablero_jugador[row, col : (col + eslora)] = "3"
                        print(value, init_pos, "este")
                        bandera = True
                    elif orient == "S" and 0<= (row + eslora) < 10 and "3" not in orient_S and "4" not in orient_S:
                        self.tablero_jugador[row : (row + eslora) , col] = "3"
                        print(value, init_pos, "sur")
                        bandera = True
                    elif orient == "O" and 0<= (col - eslora) < 10 and "3" not in orient_O and "4" not in orient_O:
                        self.tablero_jugador[row, col : (col - eslora) : -1] = "3"
                        print(value, init_pos, "oeste")
                        bandera = True
                    else:
                        orient = random.choice(["N", "E", "S", "O"])
                        init_pos = np.random.randint(10, size=2)
                        row = init_pos[0]
                        col = init_pos[1]
                        orient_N = self.tablero_jugador[row : (row - eslora) : -1 , col]
                        orient_E = self.tablero_jugador[row, col : (col + eslora)]
                        orient_S = self.tablero_jugador[row : (row + eslora) , col]
                        orient_O = self.tablero_jugador[row, col : (col - eslora) : -1]
            #posición de los 3 barcos de eslora = 2, a random
            if 3 <= pos < 6:
                eslora = 2
                bandera = False
                while bandera == False:
                    if orient == "N" and 0<= (row - eslora) < 10 and "2" not in orient_N and "3" not in orient_N and "4" not in orient_N:
                        self.tablero_jugador[row : (row - eslora) : -1 , col] = "2"
                        print(value, init_pos, "norte")
                        bandera = True
                    elif orient == "E" and 0<= (col + eslora) < 10 and "2" not in orient_E and "3" not in orient_E and "4" not in orient_E:
                        self.tablero_jugador[row, col : (col + eslora)] = "2"
                        print(value, init_pos, "este")
                        bandera = True
                    elif orient == "S" and 0<= (row + eslora) < 10 and "2" not in orient_S and "3" not in orient_S and "4" not in orient_S:
                        self.tablero_jugador[row : (row + eslora) , col] = "2"
                        print(value, init_pos, "sur")
                        bandera = True
                    elif orient == "O" and 0<= (col - eslora) < 10 and "2" not in orient_O and "3" not in orient_O and "4" not in orient_O:
                        self.tablero_jugador[row, col : (col - eslora) : -1] = "2"
                        print(value, init_pos, "oeste")
                        bandera = True
                    else:
                        orient = random.choice(["N", "E", "S", "O"])
                        init_pos = np.random.randint(10, size=2)
                        row = init_pos[0]
                        col = init_pos[1]
                        orient_N = self.tablero_jugador[row : (row - eslora) : -1 , col]
                        orient_E = self.tablero_jugador[row, col : (col + eslora)]
                        orient_S = self.tablero_jugador[row : (row + eslora) , col]
                        orient_O = self.tablero_jugador[row, col : (col - eslora) : -1]
            #posición de los 4 barcos de eslora = 1, a random
            if pos > 5:
                eslora = 1
                bandera = False
                while bandera == False:
                    if "1" not in self.tablero_jugador[row,col] and "2" not in self.tablero_jugador[row,col] and "3" not in self.tablero_jugador[row,col] and "4" not in self.tablero_jugador[row,col]:
                        self.tablero_jugador[row,col] = "1"
                        print(value, init_pos)
                        bandera = True
                    else:
                        init_pos = np.random.randint(10, size=2)
                        row = init_pos[0]
                        col = init_pos[1]

        print(f"\n{self.id_jugador}, éste es tu tablero:")
        return self.tablero_jugador

    def inicializar_tablero_automatico_maquina(self):
        print("\nInicializando tablero de la máquina...")
        eslora = 0
        for pos,value in enumerate(self.barcos):
            #defino lista de orientaciones desde las que elegir a random
            orient = random.choice(["N", "E", "S", "O"])
            #posición inicial de cada barco
            init_pos = np.random.randint(10, size=2)
            row = init_pos[0]
            col = init_pos[1]
            #defino posiciones desde punto inicial (para los barcos con eslora de 2 a 4)
            orient_N = self.tablero_maquina[row : (row - eslora) : -1 , col]
            orient_E = self.tablero_maquina[row, col : (col + eslora)]
            orient_S = self.tablero_maquina[row : (row + eslora) , col]
            orient_O = self.tablero_maquina[row, col : (col - eslora) : -1]

            #posición del barco de eslora = 4, a random
            if pos == 0:
                eslora = 4
                bandera = False
                while bandera == False:
                    if orient == "N" and 0<= (row - eslora) < 10:
                        self.tablero_maquina[row : (row - eslora) : -1 , col] = "4"
                        bandera = True
                    elif orient == "E" and 0<= (col + eslora) < 10:
                        self.tablero_maquina[row, col : (col + eslora)] = "4"
                        bandera = True
                    elif orient == "S" and 0<= (row + eslora) < 10:
                        self.tablero_maquina[row : (row + eslora) , col] = "4"
                        bandera = True
                    elif orient == "O" and 0<= (col - eslora) < 10:
                        self.tablero_maquina[row, col : (col - eslora) : -1] = "4"
                        bandera = True
                    else:
                        orient = random.choice(["N", "E", "S", "O"])
                        init_pos = np.random.randint(10, size=2)
                        row = init_pos[0]
                        col = init_pos[1]
                        orient_N = self.tablero_jugador[row : (row - eslora) : -1 , col]
                        orient_E = self.tablero_jugador[row, col : (col + eslora)]
                        orient_S = self.tablero_jugador[row : (row + eslora) , col]
                        orient_O = self.tablero_jugador[row, col : (col - eslora) : -1]
            #posición de los 2 barcos de eslora = 3, a random
            if 1 <= pos < 3:
                eslora = 3
                bandera = False
                while bandera == False:
                    if orient == "N" and 0<= (row - eslora) < 10 and "3" not in orient_N and "4" not in orient_N:   # si ponía if " " not in orient_N no me funcionaba y se solapaban los numeros
                        self.tablero_maquina[row : (row - eslora) : -1 , col] = "3"
                        bandera = True
                    elif orient == "E" and 0<= (col + eslora) < 10 and "3" not in orient_E and "4" not in orient_E:
                        self.tablero_maquina[row, col : (col + eslora)] = "3"
                        bandera = True
                    elif orient == "S" and 0<= (row + eslora) < 10 and "3" not in orient_S and "4" not in orient_S:
                        self.tablero_maquina[row : (row + eslora) , col] = "3"
                        bandera = True
                    elif orient == "O" and 0<= (col - eslora) < 10 and "3" not in orient_O and "4" not in orient_O:
                        self.tablero_maquina[row, col : (col - eslora) : -1] = "3"
                        bandera = True
                    else:
                        orient = random.choice(["N", "E", "S", "O"])
                        init_pos = np.random.randint(10, size=2)
                        row = init_pos[0]
                        col = init_pos[1]
                        orient_N = self.tablero_jugador[row : (row - eslora) : -1 , col]
                        orient_E = self.tablero_jugador[row, col : (col + eslora)]
                        orient_S = self.tablero_jugador[row : (row + eslora) , col]
                        orient_O = self.tablero_jugador[row, col : (col - eslora) : -1]
            #posición de los 3 barcos de eslora = 2, a random
            if 3 <= pos < 6:
                eslora = 2
                bandera = False
                while bandera == False:
                    if orient == "N" and 0<= (row - eslora) < 10 and "2" not in orient_N and "3" not in orient_N and "4" not in orient_N:
                        self.tablero_maquina[row : (row - eslora) : -1 , col] = "2"
                        bandera = True
                    elif orient == "E" and 0<= (col + eslora) < 10 and "2" not in orient_E and "3" not in orient_E and "4" not in orient_E:
                        self.tablero_maquina[row, col : (col + eslora)] = "2"
                        bandera = True
                    elif orient == "S" and 0<= (row + eslora) < 10 and "2" not in orient_S and "3" not in orient_S and "4" not in orient_S:
                        self.tablero_maquina[row : (row + eslora) , col] = "2"
                        bandera = True
                    elif orient == "O" and 0<= (col - eslora) < 10 and "2" not in orient_O and "3" not in orient_O and "4" not in orient_O:
                        self.tablero_maquina[row, col : (col - eslora) : -1] = "2"
                        bandera = True
                    else:
                        orient = random.choice(["N", "E", "S", "O"])
                        init_pos = np.random.randint(10, size=2)
                        row = init_pos[0]
                        col = init_pos[1]
                        orient_N = self.tablero_jugador[row : (row - eslora) : -1 , col]
                        orient_E = self.tablero_jugador[row, col : (col + eslora)]
                        orient_S = self.tablero_jugador[row : (row + eslora) , col]
                        orient_O = self.tablero_jugador[row, col : (col - eslora) : -1]
            #posición de los 4 barcos de eslora = 1, a random
            if pos > 5:
                eslora = 1
                bandera = False
                while bandera == False:
                    if "1" not in self.tablero_maquina[row,col] and "2" not in self.tablero_maquina[row,col] and "3" not in self.tablero_maquina[row,col] and "4" not in self.tablero_maquina[row,col]:
                        self.tablero_maquina[row,col] = "1"
                        bandera = True
                    else:
                        init_pos = np.random.randint(10, size=2)
                        row = init_pos[0]
                        col = init_pos[1]
        # print(self.tablero_maquina)  ##esto lo dejo oculto porque no puedo ver el tablero el oponente
        return "Tablero máquina inicializado. YA EMPIEZA EL JUEGO!.\n"



    ##jugada mia
    def jugada_jugador(self):
        bandera = False
        while bandera == False:

            disparo = (int(input(f"\n{self.id_jugador}, introduce un número del 0 al 9 inclusive:\n")), int(input("Introduce otro número del 0 al 9:\n")))

            if self.tablero_maquina[disparo[0],disparo[1]] == "~" or self.tablero_maquina[disparo[0],disparo[1]] == "X":
                print("Ya has disparado esta coordenada, inténtalo con otra.\n")
                bandera = False

            elif self.tablero_maquina[disparo[0],disparo[1]] != " ":
                self.tablero_guess[disparo[0],disparo[1]] = "X"
                self.tablero_maquina[disparo[0],disparo[1]] = "X" #esto es solo para que almacene los disparos en el tablero maquina, aunque no me lo muestre
                print(f"Bien {self.id_jugador}! Has encontrado un barco o parte de él, sigue disparando!")
                print("Éste es el daño que le has hecho a tu oponente:\n",self.tablero_guess)
                bandera = False

            else:
                self.tablero_guess[disparo[0],disparo[1]] = "~"
                self.tablero_maquina[disparo[0],disparo[1]] = "~" #esto es solo para que almacene los disparos en el tablero maquina, aunque no me lo muestre
                print(f"¡Vaya {self.id_jugador}! Le has dado al agua... ahora le toca a tu adversario")
                print("Situación disparos en tablero máquina:\n",self.tablero_guess)
                bandera = True


    ##jugada maquina
    def jugada_maquina(self):
        bandera = False
        while bandera == False:
            print("\nMáquina disparando...")
            disparo = np.random.randint(9,size=(2)) 


            if self.tablero_jugador[disparo[0],disparo[1]] == "~" or self.tablero_jugador[disparo[0],disparo[1]] == "X":
                print("La máquina ha repetido coordenada, volverá a intentarlo ahora.\n")
                bandera = False

            elif self.tablero_jugador[disparo[0],disparo[1]] != " ":
                self.tablero_jugador[disparo[0],disparo[1]] = "X"
                print("La máquina ha encontrado un barco o parte de él, te va a disparar de nuevo.\n")
                bandera = False

            else:
                self.tablero_jugador[disparo[0],disparo[1]] = "~"
                print("La máquina ha encontrado agua, te vuelve a tocar a tí.")
                print("Éste es tu tablero con los disparos que te ha hecho la máquina:\n",self.tablero_jugador)
                bandera = True

