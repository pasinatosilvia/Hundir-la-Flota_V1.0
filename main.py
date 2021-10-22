from clase_tablero import Tablero
import numpy as np
import random


turno = 0  ###  turno = 0, juego yo / turno = 1, juega la máquina
victoria = False

tablero_Silvia = Tablero("Silvia")

print(Tablero("Silvia"))

print(tablero_Silvia.inicializar_tablero_automatico_jugador())

print(tablero_Silvia.inicializar_tablero_automatico_maquina())

while victoria == False:
    if turno % 2 == 0:
       tablero_Silvia.jugada_jugador()
       if "1" not in Tablero.tablero_maquina and "2" not in Tablero.tablero_maquina and "3" not in Tablero.tablero_maquina and "4" not in Tablero.tablero_maquina:
           victoria = True
           print(Tablero.tablero_maquina)
    else:
        tablero_Silvia.jugada_maquina()
        if "1" not in Tablero.tablero_jugador and "2" not in Tablero.tablero_jugador and "3" not in Tablero.tablero_jugador and "4" not in Tablero.tablero_jugador:
            victoria = True
    turno += 1
if turno % 2 == 1:  #esto significa que el ultimo en tirar ha sido el usuario
    print("HAS GANADO, JUGADOR")
else:
    print("HA GANADO LA MAQUINA")
print(Tablero.tablero_maquina)









