import os
import random
from paquete.config import *


def cargar_nonograma_csv(ruta):
    """_summary_

    Args:
        ruta (_type_): _description_

    Returns:
        _type_: _description_
    """
    nonograma_resuelto = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(",")))
            nonograma_resuelto.append(fila)
    return nonograma_resuelto

def elegir_nonograma_random(ruta_categoria):
    """_summary_

    Args:
        ruta_categoria (_type_): _description_

    Returns:
        _type_: _description_
    """
    archivos = os.listdir(ruta_categoria)
    elegido = random.choice(archivos)
    
    return ruta_categoria + elegido

def crear_nonograma_jugador(filas, columnas):
    """_summary_

    Args:
        filas (_type_): _description_
        columnas (_type_): _description_

    Returns:
        _type_: _description_
    """
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
    """_summary_

    Args:
        jugador (_type_): _description_
        resuelto (_type_): _description_

    Returns:
        _type_: _description_
    """
    for i in range(len(resuelto)):
        for j in range(len(resuelto[i])):
            if resuelto[i][j] == 1 and jugador[i][j] != 1:
                return False
            if resuelto[i][j] == 0 and jugador[i][j] == 1:
                return False
    return True

def elegir_nonograma_random(ruta_categoria):
    """_summary_

    Args:
        ruta_categoria (_type_): _description_

    Returns:
        _type_: _description_
    """
    archivos = os.listdir(ruta_categoria)
    elegido = random.choice(archivos)
    return ruta_categoria + elegido

def iniciar_partida(ruta):
    """_summary_

    Args:
        ruta (_type_): _description_

    Returns:
        _type_: _description_
    """
    resuelto = cargar_nonograma_csv(ruta)
    filas = len(resuelto)
    columnas = len(resuelto[0])
    resuelto = cargar_nonograma_csv(ruta)
    jugador = crear_nonograma_jugador(filas, columnas)
    return jugador, resuelto


def calcular_pistas(nonograma):
    """_summary_

    Args:
        nonograma (_type_): _description_

    Returns:
        _type_: _description_
    """
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

def controlar_error(jugador, resuelto, fila, columna):
    """_summary_

    Args:
        jugador (_type_): _description_
        resuelto (_type_): _description_
        fila (_type_): _description_
        columna (_type_): _description_

    Returns:
        _type_: _description_
    """
    if resuelto[fila][columna] == 1 and jugador[fila][columna] == 0:
        return True
    if resuelto[fila][columna] == 0 and jugador[fila][columna] == 1:
        return True
    return False





    

        
