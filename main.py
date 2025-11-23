import pygame
from config import ANCHO, ALTO
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


# ---------------------------------------------------------
#  MENÚ PRINCIPAL
# ---------------------------------------------------------
def menu_principal():
    activo = True
    while activo:
        ventana.fill(BLANCO)

        boton_jugar = pygame.Rect(300, 150, 200, 60)
        boton_ranking = pygame.Rect(300, 250, 200, 60)
        boton_salir = pygame.Rect(300, 350, 200, 60)

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


# ---------------------------------------------------------
#  MENÚ DE DIFICULTAD
# ---------------------------------------------------------
def menu_dificultad():
    activo = True
    while activo:
        ventana.fill(BLANCO)

        b1 = pygame.Rect(300, 150, 200, 60)
        b2 = pygame.Rect(300, 250, 200, 60)
        b3 = pygame.Rect(300, 350, 200, 60)

        dibujar_boton(ventana, b1, "Fácil", font, GRIS, NEGRO)
        dibujar_boton(ventana, b2, "Medio", font, GRIS, NEGRO)
        dibujar_boton(ventana, b3, "Difícil", font, GRIS, NEGRO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(evento.pos):
                    iniciar_juego(RUTA_FACIL)
                if b2.collidepoint(evento.pos):
                    iniciar_juego(RUTA_MEDIO)
                if b3.collidepoint(evento.pos):
                    iniciar_juego(RUTA_DIFICIL)

        pygame.display.update()


# ---------------------------------------------------------
#  JUEGO
# ---------------------------------------------------------
def iniciar_juego(ruta_carpeta):
    ruta = elegir_nonograma_random(ruta_carpeta)
    jugador, resuelto = iniciar_partida(ruta)

    filas = len(resuelto)
    columnas = len(resuelto[0])

    TAM_CELDA = min(ANCHO // columnas, ALTO // filas)

    activo = True
    while activo:
        ventana.fill(BLANCO)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                fila = y // TAM_CELDA
                columna = x // TAM_CELDA

                if fila < filas and columna < columnas:
                    if evento.button == 1:
                        cambiar_estado(jugador, fila, columna, 1)
                    elif evento.button == 3:
                        cambiar_estado(jugador, fila, columna, 2)

                    if comparar_nonogramas(jugador, resuelto):
                        print("¡Ganaste!")
                        return

        dibujar_tablero(ventana, jugador, TAM_CELDA, filas, columnas)
        pygame.display.update()


# ---------------------------------------------------------
menu_principal()



            
            
            
        
                
                
        
            
            
            
            
        