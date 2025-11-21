import os
import random

def elegir_nonograma_random(ruta):
    archivos = os.listdir(ruta)
    elegido = random.choice(archivos)
    return ruta + elegido

def mostrar_tablero(nonograma_jugador):

    print("TABLERO DEL JUGADOR")

    filas = len(nonograma_jugador)
    columnas = len(nonograma_jugador[0])

    
    print("   ", end="")
    for j in range(columnas):
        if j+1 < 10:
            print(" " + str(j+1), end=" ")
        else:
            print(str(j+1), end=" ")
    print()

    
    for i in range(filas):

        
        if i+1 < 10:
            print(" " + str(i+1), end="  ")
        else:
            print(str(i+1), end=" ")

        
        for j in range(columnas):
            print(" " + nonograma_jugador[i][j], end=" ")
        print()

    print()


def comparar_nonogramas(nonograma_jugador, nonograma_resuelto):
    filas = len(nonograma_resuelto)
    columnas = len(nonograma_resuelto[0])

    for i in range(filas):
        for j in range(columnas):
            # La solución pide 1 (pintado) y el jugador NO pintó
            if nonograma_resuelto[i][j] == 1 and nonograma_jugador[i][j] != "█":
                return False
            
            # La solución pide 0 (vacío) y el jugador pintó
            if nonograma_resuelto[i][j] == 0 and nonograma_jugador[i][j] == "█":
                return False

    return True

def crear_nonograma_jugador(filas, columnas):
    nonograma_jugador = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(" ")  # vacío
        nonograma_jugador.append(fila)
    return nonograma_jugador


def jugar_nonograma(nonograma_resuelto):

    filas = len(nonograma_resuelto)
    columnas = len(nonograma_resuelto[0])

    # Crear tablero del jugador
    nonograma_jugador = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(" ")
        nonograma_jugador.append(fila)

    vidas = 3
    errores = 0
    jugando = True

    while jugando:

        mostrar_tablero(nonograma_jugador)
        print(f"Vidas: {vidas} | Errores: {errores}")
        print("Acciones: 'm' = pintar | 'X' = marcar vacío | ENTER = borrar")
        print("Escriba 'fin' para abandonar.\n")

        entrada = input("Ingrese coordenada (fila,columna): ").strip()

        # Opción de abandonar
        if entrada.lower() == "fin":
            print("Partida finalizada.")
            return

        # Validación de coordenadas
        try:
            partes = entrada.split(",")
            f = int(partes[0]) - 1
            c = int(partes[1]) - 1

            if not (0 <= f < filas and 0 <= c < columnas):
                print("Coordenada fuera del tablero.")
                continue

        except:
            print("Formato inválido. Use: fila,columna (ej: 2,3)")
            continue

        # Acción del jugador
        accion = input("Símbolo (m / X / ENTER): ").strip().lower()

        if accion == "":
            accion = " "
        elif accion == "m":         # pintar
            accion = "█"
        elif accion == "x":         # marcar vacío
            accion = "X"
        else:
            print("Acción inválida.")
            continue

        # Aplicar la jugada
        nonograma_jugador[f][c] = accion

        # Verificar si la jugada es correcta
        valor_real = nonograma_resuelto[f][c]

        es_correcto = (
            (valor_real == 1 and accion == "█") or
            (valor_real == 0 and accion != "█")
        )

        if not es_correcto:
            errores += 1
            vidas -= 1
            print("\n❌ Movimiento incorrecto. Penalización de 3 segundos...\n")
            import time
            time.sleep(3)

            if vidas == 0:
                print("💀 GAME OVER 💀")
                return

        # Verificar victoria
        if comparar_nonogramas(nonograma_jugador, nonograma_resuelto):
            mostrar_tablero(nonograma_jugador)
            print("🎉 ¡GANASTE! Nonograma completado 🎉")
            return


    

        
