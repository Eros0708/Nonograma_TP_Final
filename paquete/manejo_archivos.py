import csv
import os
RUTA_RANKING = "paquete/ranking/ranking.csv"
def cargar_nonograma_csv(ruta):
    nonograma_resuelto = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(",")))
            nonograma_resuelto.append(fila)
    return nonograma_resuelto


def cargar_ranking(ruta="mostrar_ranking.csv"):

    ranking = []
    with open(RUTA_RANKING, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        
        for fila in lector:
            if len(fila) == 3:
                nombre, ruta, tiempo = fila
                ranking.append({
                    "nombre": nombre,
                    "ruta": ruta,
                    "tiempo": int(tiempo)
                })
    return ranking

def guardar_ranking(ranking, ruta="mostrar_ranking.csv"):
    with open(RUTA_RANKING, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        for entrada in ranking:
            escritor.writerow([
                entrada["nombre"],
                entrada["ruta"],
                entrada["tiempo"]
            ])

def agregar_entrada(ranking, nombre, nonograma, tiempo):
    nueva = {
        "nombre": nombre,
        "ruta": nonograma,
        "tiempo": tiempo
    }
    return ranking + [nueva]     

def ordenar_ranking(ranking):
    return sorted(ranking, key=lambda x: x["tiempo"])
