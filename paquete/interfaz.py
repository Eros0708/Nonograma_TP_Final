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

def mostrar_game_over(ventana, font_game_over, calavera_img):
    """_summary_

    Args:
        ventana (_type_): _description_
        font_game_over (_type_): _description_
        calavera_img (_type_): _description_
    """
    ventana.fill(NEGRO)
    ventana.blit(calavera_img, (250, 400))
    texto = font_game_over.render("GAME OVER", True, ROJO)
    rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2 - 200))
    ventana.blit(texto, rect)
    pygame.display.update()
    pygame.time.delay(3000)
    
def dibujar_corazones(ventana, corazon_img, vidas):
    """_summary_

    Args:
        ventana (_type_): _description_
        corazon_img (_type_): _description_
        vidas (_type_): _description_
    """
    
    for i in range(vidas):
        
        ventana.blit(corazon_img, (600 + i * 60, 0))

def pedir_nombre(ventana, font):
    """_summary_

    Args:
        ventana (_type_): _description_
        font (_type_): _description_

    Returns:
        _type_: _description_
    """
    nombre = ""
    activo = True

    while activo:
        ventana.fill(BLANCO)

        texto = font.render("Ingresa tu nombre:", True, NEGRO)
        ventana.blit(texto, (200, 200))

        
        cuadro = pygame.Rect(200, 300, 400, 50)
        pygame.draw.rect(ventana, NEGRO, cuadro, 2)

        texto_nombre = font.render(nombre, True, NEGRO)
        ventana.blit(texto_nombre, (210, 310))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    if nombre.strip() != "":
                        return nombre

                elif evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]

                else:
                    if len(nombre) < 15:  
                        nombre += evento.unicode

        pygame.display.update()

    

def mostrar_ranking(ventana, font, ranking):
    activo = True
    while activo:
        ventana.fill(BLANCO)

        titulo = font.render("RANKING", True, NEGRO)
        ventana.blit(titulo, (330, 50))

        y = 150
        for entrada in ranking[:10]:
            linea = f"{entrada['nombre']} - {entrada['nonograma']} - {entrada['tiempo']}s"
            texto = font.render(linea, True, NEGRO)
            ventana.blit(texto, (50, y))
            y += 40

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return

        pygame.display.update()


    
def mostrar_victoria(ventana, font_victoria):
    
    ventana.fill(VERDE)
    
    texto = font_victoria.render("GANASTE", True, AMARILLO)
    rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2 - 200))
    ventana.blit(texto, rect)
    pygame.display.update()
    pygame.time.delay(3000)