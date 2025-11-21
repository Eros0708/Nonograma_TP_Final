def cargar_nonograma_csv(ruta):
    nonograma_facil = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(",")))
            nonograma_facil.append(fila)
    return nonograma_facil
