import os
import random

def cargar_nonograma_csv(ruta):
    nonograma_resuelto = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(",")))
            nonograma_resuelto.append(fila)
    return nonograma_resuelto

def crear_nonograma_jugador(filas, columnas):
    nonograma_jugador = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        nonograma_jugador.append(fila)
    return nonograma_jugador

def cambiar_estado(nonograma_jugador, fila, columna, estado):
    nonograma_jugador[fila][columna] = estado

def comparar_nonogramas(jugador, resuelto):
    for i in range(len(resuelto)):
        for j in range(len(resuelto[i])):
            if resuelto[i][j] == 1 and jugador[i][j] != 1:
                return False
            if resuelto[i][j] == 0 and jugador[i][j] == 1:
                return False
    return True

def elegir_nonograma_random(ruta_categoria):
    archivos = os.listdir(ruta_categoria)
    elegido = random.choice(archivos)
    return ruta_categoria + elegido

def iniciar_partida(ruta):
    resuelto = cargar_nonograma_csv(ruta)
    filas = len(resuelto)
    columnas = len(resuelto[0])
    jugador = crear_nonograma_jugador(filas, columnas)
    return jugador, resuelto


def calcular_pistas(nonograma):
    filas = len(nonograma)
    columnas = len(nonograma[0])

    pistas_filas = []
    pistas_columnas = []


    for fila in nonograma:
        pistas = []
        contador = 0
        for celda in fila:
            if celda == 1:
                contador += 1
            else:
                if contador > 0:
                    pistas.append(contador)
                contador = 0
        if contador > 0:
            pistas.append(contador)

        if pistas == []:
            pistas = [0]

        pistas_filas.append(pistas)


    for col in range(columnas):
        pistas = []
        contador = 0
        for fila in range(filas):
            if nonograma[fila][col] == 1:
                contador += 1
            else:
                if contador > 0:
                    pistas.append(contador)
                contador = 0
        if contador > 0:
            pistas.append(contador)

        if pistas == []:
            pistas = [0]

        pistas_columnas.append(pistas)

    return pistas_filas, pistas_columnas





    

        
