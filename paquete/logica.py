import os
import random
from paquete.config import *
from paquete.manejo_archivos import cargar_nonograma_csv
def elegir_nonograma_random(ruta_categoria: str) -> str:
    """_summary_

    Args:
        ruta_categoria (str): carpeta de la categoria

    Returns:
        str: retorna la ruta completa del nonograma elegido
    """
    archivos = os.listdir(ruta_categoria)
    elegido = random.choice(archivos)
    
    return ruta_categoria + elegido

def crear_nonograma_jugador(filas: int, columnas: int) -> list:
    """_summary_

    Args:
        filas (int): número de filas del nonograma
        columnas (int): número de columnas del nonograma

    Returns:
        list: matriz que representa el nonograma del jugador
    """
    nonograma_jugador = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        nonograma_jugador.append(fila)
    return nonograma_jugador

def cambiar_estado(nonograma_jugador: list, fila: int, columna: int, estado: int) -> None:
    nonograma_jugador[fila][columna] = estado

def comparar_nonogramas(jugador: list, resuelto: list) -> bool:
    """_summary_

    Args:
        jugador (list): matriz que representa el nonograma del jugador
        resuelto (list): matriz que representa el nonograma resuelto

    Returns:
        bool: True si los nonogramas coinciden, False en caso contrario
    """
    for i in range(len(resuelto)):
        for j in range(len(resuelto[i])):
            if resuelto[i][j] == 1 and jugador[i][j] != 1:
                return False
            if resuelto[i][j] == 0 and jugador[i][j] == 1:
                return False
    return True

def iniciar_partida(ruta: str):
    """_summary_

    Args:
        ruta (str): ruta del archivo del nonograma

    Returns:
        tuple: retorna una tupla con el nonograma del jugador y el nonograma resuelto
    """
    resuelto = cargar_nonograma_csv(ruta)
    filas = len(resuelto)
    columnas = len(resuelto[0])
    resuelto = cargar_nonograma_csv(ruta)
    jugador = crear_nonograma_jugador(filas, columnas)
    return jugador, resuelto


def calcular_pistas(nonograma: list) -> tuple:
    """_summary_

    Args:
        nonograma (list): matriz que representa el nonograma

    Returns:
        tuple: retorna una tupla con las pistas de filas y columnas
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

def controlar_error(jugador: list, resuelto: list, fila: int, columna: int) -> bool:
    """_summary_

    Args:
        jugador (list): matriz que representa el nonograma del jugador
        resuelto (list): matriz que representa el nonograma resuelto
        fila (int): índice de la fila
        columna (int): índice de la columna

    Returns:
        bool: True si hay un error en la celda especificada, False en caso contrario
    """
    if resuelto[fila][columna] == 1 and jugador[fila][columna] == 0:
        return True
    if resuelto[fila][columna] == 0 and jugador[fila][columna] == 1:
        return True
    return False







    

        
