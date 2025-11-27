import pygame
from paquete.config import *
from paquete.logica import *
from paquete.interfaz import *
from paquete.manejo_archivos import *

pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Nonograma")
font = pygame.font.SysFont(None, TAM_FUENTE)

RUTA_FACIL = "nonogramas/facil/"
RUTA_MEDIO = "nonogramas/medio/"
RUTA_DIFICIL = "nonogramas/dificil/"


def menu_principal():
    activo = True
    while activo:
        ventana.fill(BLANCO)

        boton_jugar = pygame.Rect(0, 0, 200, 60)
        boton_ranking = pygame.Rect(0, 0, 200, 60)
        boton_salir = pygame.Rect(0, 0, 200, 60)

        boton_jugar.center = (ANCHO // 2, ALTO // 2 - 120)
        boton_ranking.center = (ANCHO // 2, ALTO // 2)
        boton_salir.center = (ANCHO // 2, ALTO // 2 + 120)

        dibujar_boton(ventana, boton_jugar, "Jugar", font, GRIS, NEGRO)
        dibujar_boton(ventana, boton_ranking, "Ranking", font, GRIS, NEGRO)
        dibujar_boton(ventana, boton_salir, "Salir", font, GRIS, NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    menu_dificultad()
                if boton_ranking.collidepoint(evento.pos):
                    print("Ranking todavía no implementado.")
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    exit()

        pygame.display.update()


def menu_dificultad():
    activo = True
    while activo:
        ventana.fill(BLANCO)

        boton_facil = pygame.Rect(0, 0, 200, 60)
        boton_medio = pygame.Rect(0, 0, 200, 60)
        boton_dificil = pygame.Rect(0, 0, 200, 60)

        boton_facil.center = (ANCHO // 2, ALTO // 2 - 120)
        boton_medio.center = (ANCHO // 2, ALTO // 2)
        boton_dificil.center = (ANCHO // 2, ALTO // 2 + 120)

        dibujar_boton(ventana, boton_facil, "Fácil", font, GRIS, NEGRO)
        dibujar_boton(ventana, boton_medio, "Medio", font, GRIS, NEGRO)
        dibujar_boton(ventana, boton_dificil, "Difícil", font, GRIS, NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_facil.collidepoint(evento.pos):
                    iniciar_juego(RUTA_FACIL)
                if boton_medio.collidepoint(evento.pos):
                    iniciar_juego(RUTA_MEDIO)
                if boton_dificil.collidepoint(evento.pos):
                    iniciar_juego(RUTA_DIFICIL)

        pygame.display.update()


def iniciar_juego(ruta_carpeta):
    ruta = elegir_nonograma_random(ruta_carpeta)
    jugador, resuelto = iniciar_partida(ruta)

    filas = len(resuelto)
    columnas = len(resuelto[0])

    TAM_CELDA = min(
        (ANCHO - PADDING_IZQ - PADDING_DER) // columnas,
        (ALTO - PADDING_SUP - PADDING_INF) // filas
    )

    offset_x = PADDING_IZQ
    offset_y = PADDING_SUP

    pistas_filas, pistas_columnas = calcular_pistas(resuelto)

    
    vidas = 3
    error_en_revision = False
    tiempo_error = 0
    fila_error = None
    columna_error = None

    activo = True
    while activo:
        ventana.fill(BLANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos

                if offset_x <= x < offset_x + columnas*TAM_CELDA and \
                   offset_y <= y < offset_y + filas*TAM_CELDA:

                    fila = (y - offset_y) // TAM_CELDA
                    columna = (x - offset_x) // TAM_CELDA

                    
                    if evento.button == 1:
                        cambiar_estado(jugador, fila, columna, 1)
                    
                    elif evento.button == 3:
                        cambiar_estado(jugador, fila, columna, 2)

                   
                    if controlar_error(jugador, resuelto, fila, columna):
                        print("Error cometido. Tienes 3 segundos para corregirlo.")
                        error_en_revision = True
                        tiempo_error = pygame.time.get_ticks()
                        fila_error = fila
                        columna_error = columna

                    
                    if comparar_nonogramas(jugador, resuelto):
                        print("¡Ganaste!")
                        return

       
        if error_en_revision:

            
            if not controlar_error(jugador, resuelto, fila_error, columna_error):
                print("Error corregido a tiempo.")
                error_en_revision = False

            else:
                
                if pygame.time.get_ticks() - tiempo_error >= 3000:
                    vidas -= 1
                    print(f"Vida perdida. Vidas restantes: {vidas}")

                    
                    if vidas == 0:
                        mostrar_game_over(ventana, font)
                        return

                   
                    error_en_revision = False

        
        dibujar_tablero(ventana, jugador, TAM_CELDA, filas, columnas,
                        offset_x, offset_y)

        dibujar_pistas(ventana, font, pistas_filas, pistas_columnas,
                       TAM_CELDA, offset_x, offset_y)

        pygame.display.update()

                               
                               
                               
                               



