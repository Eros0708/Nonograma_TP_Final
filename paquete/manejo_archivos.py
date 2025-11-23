def cargar_nonograma_csv(ruta):
    nonograma_resuelto = []
    with open(ruta, "r") as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split(",")))
            nonograma_resuelto.append(fila)
    return nonograma_resuelto
