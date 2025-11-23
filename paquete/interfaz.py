import pygame
from config import *

def render_texto(texto, font, color):
    return font.render(texto, True, color)

def dibujar_boton(screen, rect, texto, font, color_fondo, color_texto):
    pygame.draw.rect(screen, color_fondo, rect)
    texto_img = font.render(texto, True, color_texto)
    texto_rect = texto_img.get_rect(center=rect.center)
    screen.blit(texto_img, texto_rect)

def dibujar_cruz(screen, rect):
    pygame.draw.line(screen, ROJO, rect.topleft, rect.bottomright, 3)
    pygame.draw.line(screen, ROJO, rect.topright, rect.bottomleft, 3)

def dibujar_tablero(screen, jugador, tam_celda, filas, columnas):
    for i in range(filas):
        for j in range(columnas):
            x = j * tam_celda
            y = i * tam_celda
            rect = pygame.Rect(x, y, tam_celda, tam_celda)

            if jugador[i][j] == 1:
                pygame.draw.rect(screen, NEGRO, rect)
            elif jugador[i][j] == 2:
                pygame.draw.rect(screen, BLANCO, rect)
                dibujar_cruz(screen, rect)
            else:
                pygame.draw.rect(screen, BLANCO, rect)

            pygame.draw.rect(screen, NEGRO, rect, 1)

