import pygame
from paquete.config import *


def render_texto(texto, font, color):
    """_summary_

    Args:
        texto (_type_): _description_
        font (_type_): _description_
        color (_type_): _description_

    Returns:
        _type_: _description_
    """
    return font.render(texto, True, color)

def dibujar_boton(screen, rect, texto, font, color_fondo, color_texto):
    """_summary_

    Args:
        screen (_type_): _description_
        rect (_type_): _description_
        texto (_type_): _description_
        font (_type_): _description_
        color_fondo (_type_): _description_
        color_texto (_type_): _description_
    """
    pygame.draw.rect(screen, color_fondo, rect)
    texto_img = font.render(texto, True, color_texto)
    texto_rect = texto_img.get_rect(center=rect.center)
    screen.blit(texto_img, texto_rect)

def dibujar_cruz(screen, rect):
    """_summary_

    Args:
        screen (_type_): _description_
        rect (_type_): _description_
    """
    pygame.draw.line(screen, ROJO, rect.topleft, rect.bottomright, 3)
    pygame.draw.line(screen, ROJO, rect.topright, rect.bottomleft, 3)

def dibujar_tablero(ventana, jugador, tam, filas, columnas, offset_x, offset_y):
    """_summary_

    Args:
        ventana (_type_): _description_
        jugador (_type_): _description_
        tam (_type_): _description_
        filas (_type_): _description_
        columnas (_type_): _description_
        offset_x (_type_): _description_
        offset_y (_type_): _description_
    """
    for f in range(filas):
        for c in range(columnas):
            x = offset_x + c * tam
            y = offset_y + f * tam

            valor = jugador[f][c]

            
            if valor == 0:
                pygame.draw.rect(ventana, GRIS, (x, y, tam, tam))

            
            elif valor == 1:
                pygame.draw.rect(ventana, NEGRO, (x, y, tam, tam))

            
            elif valor == 2:
                pygame.draw.rect(ventana, BLANCO, (x, y, tam, tam))
                pygame.draw.line(ventana, ROJO, (x, y), (x+tam, y+tam), 3)
                pygame.draw.line(ventana, ROJO, (x+tam, y), (x, y+tam), 3)

            
            pygame.draw.rect(ventana, NEGRO, (x, y, tam, tam), 2)

def dibujar_pistas(ventana, font, pistas_filas, pistas_columnas, tam, offset_x, offset_y):
    """_summary_

    Args:
        ventana (_type_): _description_
        font (_type_): _description_
        pistas_filas (_type_): _description_
        pistas_columnas (_type_): _description_
        tam (_type_): _description_
        offset_x (_type_): _description_
        offset_y (_type_): _description_
    """
    
    for i, pista in enumerate(pistas_filas):
        texto = " ".join(str(n) for n in pista)
        img = font.render(texto, True, NEGRO)
        ventana.blit(img, (offset_x - 10 - img.get_width(), offset_y + i * tam + tam//3))


    for j, pista in enumerate(pistas_columnas):
        texto = "\n".join(str(n) for n in pista)
        lineas = texto.split("\n")

        for idx, linea in enumerate(lineas):
            img = font.render(linea, True, NEGRO)
            ventana.blit(img, (
                offset_x + j * tam + tam//3,
                offset_y - (len(lineas) * img.get_height()) - 10 + idx * img.get_height()
            ))

def mostrar_game_over(ventana, font):
    ventana.fill(NEGRO)
    texto = font.render("GAME OVER", True, ROJO)
    rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2))
    ventana.blit(texto, rect)
    pygame.display.update()
    pygame.time.delay(2000)

    