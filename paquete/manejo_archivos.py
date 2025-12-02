import csv
import os

RUTA_RANKING = "paquete/ranking/ranking.csv"


def cargar_nonograma_csv(ruta: str) -> list:
    """_summary_

    Args:
        ruta (str): ruta al archivo CSV que contiene el nonograma resuelto

    Returns:
        list: matriz que representa el nonograma resuelto
    """
    nonograma_resuelto = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(",")))
            nonograma_resuelto.append(fila)
    return nonograma_resuelto


def cargar_ranking():
    """_summary_

    Returns:
        list: lista de diccionarios con los datos del ranking
    """
    ranking = []

    if not os.path.exists(RUTA_RANKING):
        
        with open(RUTA_RANKING, "w", newline="", encoding="utf-8") as archivo:
            pass
        return ranking

    with open(RUTA_RANKING, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)

        for fila in lector:
            if len(fila) == 3:
                nombre, ruta_nonograma, tiempo = fila
                ranking.append({
                    "nombre": nombre,
                    "ruta": ruta_nonograma,
                    "tiempo": int(tiempo)
                })
    return ranking


def guardar_ranking(ranking: list) -> None:
    """_summary_

    Args:
        ranking (list): lista de diccionarios con los datos del ranking
    """
    with open(RUTA_RANKING, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for entrada in ranking:
            escritor.writerow([
                entrada["nombre"],
                entrada["ruta"],
                entrada["tiempo"]
            ])


def agregar_entrada(ranking: list, nombre: str, nonograma: str, tiempo: int) -> list:
    """_summary_

    Args:
        ranking (list): _description_
        nombre (str): nombre del jugador
        nonograma (str): ruta al archivo CSV del nonograma
        tiempo (int): tiempo que tardó en completar el nonograma

    Returns:
        list: lista actualizada del ranking
    """
    nueva = {
        "nombre": nombre,
        "ruta": nonograma,
        "tiempo": tiempo
    }
    return ranking + [nueva]


def ordenar_ranking(ranking: list) -> list:
    """_summary_

    Args:
        ranking (list): lista de diccionarios con los datos del ranking

    Returns:
        list: lista ordenada del ranking
    """
    return sorted(ranking, key=lambda x: x["tiempo"])

