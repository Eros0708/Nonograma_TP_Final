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

def dibujar_tablero(ventana, jugador, tam, filas, columnas, offset_x, offset_y):
    for f in range(filas):
        for c in range(columnas):
            x = offset_x + c * tam
            y = offset_y + f * tam

            valor = jugador[f][c]

            # 0 = vacío
            if valor == 0:
                pygame.draw.rect(ventana, GRIS, (x, y, tam, tam))

            # 1 = pintado
            elif valor == 1:
                pygame.draw.rect(ventana, NEGRO, (x, y, tam, tam))

            # 2 = cruz
            elif valor == 2:
                pygame.draw.rect(ventana, BLANCO, (x, y, tam, tam))
                pygame.draw.line(ventana, ROJO, (x, y), (x+tam, y+tam), 3)
                pygame.draw.line(ventana, ROJO, (x+tam, y), (x, y+tam), 3)

            # borde
            pygame.draw.rect(ventana, NEGRO, (x, y, tam, tam), 2)

def dibujar_pistas(ventana, font, pistas_filas, pistas_columnas, tam, offset_x, offset_y):
    # PISTAS DE FILAS (izquierda)
    for i, pista in enumerate(pistas_filas):
        texto = " ".join(str(n) for n in pista)
        img = font.render(texto, True, NEGRO)
        ventana.blit(img, (offset_x - 10 - img.get_width(), offset_y + i * tam + tam//3))

    # PISTAS DE COLUMNAS (arriba)
    for j, pista in enumerate(pistas_columnas):
        texto = "\n".join(str(n) for n in pista)
        lineas = texto.split("\n")

        for idx, linea in enumerate(lineas):
            img = font.render(linea, True, NEGRO)
            ventana.blit(img, (
                offset_x + j * tam + tam//3,
                offset_y - (len(lineas) * img.get_height()) - 10 + idx * img.get_height()
            ))
