import os
import random

import os
import random

def elegir_nonograma_random(ruta_categoria):
    archivos = os.listdir(ruta_categoria)
    elegido = random.choice(archivos)
    ruta_completa = ruta_categoria + elegido
    return ruta_completa



def comparar_nonogramas(nonograma_jugador, nonograma_resuelto):
    for i in range(len(nonograma_resuelto)):
        for j in range(len(nonograma_resuelto[i])):

            
            if nonograma_resuelto[i][j] == 1:
                if nonograma_jugador[i][j] != 1:
                    return False

          
            else:
                if nonograma_jugador[i][j] == 1:
                    return False

    return True


def cambiar_estado(nonograma_jugador, fila, columna):
    valor = nonograma_jugador[fila][columna]
    valor = valor + 1
    if valor > 2:
        valor = 0
    nonograma_jugador[fila][columna] = valor

def crear_nonograma_jugador(filas, columnas):
    nonograma_jugador = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0) 
        nonograma_jugador.append(fila)
    return nonograma_jugador






    

        
