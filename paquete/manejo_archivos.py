import csv
import os
def cargar_nonograma_csv(ruta):
    nonograma_resuelto = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(",")))
            nonograma_resuelto.append(fila)
    return nonograma_resuelto


def cargar_ranking(ruta="ranking.csv"):
    if not os.path.exists(ruta):
        return []

    ranking = []
    with open(ruta, "r", newline="") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            nombre, nonograma, tiempo = fila
            ranking.append({
                "nombre": nombre,
                "nonograma": nonograma,
                "tiempo": int(tiempo)
            })
    return ranking

def guardar_ranking(ranking, ruta="ranking.csv"):
    with open(ruta, "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        for entrada in ranking:
            escritor.writerow([
                entrada["nombre"],
                entrada["nonograma"],
                entrada["tiempo"]
            ])

def agregar_entrada(ranking, nombre, nonograma, tiempo):
    nueva = {
        "nombre": nombre,
        "nonograma": nonograma,
        "tiempo": tiempo
    }
    return ranking + [nueva]     

def ordenar_ranking(ranking):
    return sorted(ranking, key=lambda x: x["tiempo"])
