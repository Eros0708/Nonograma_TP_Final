import pygame
from paquete.config import *



def render_texto(texto: str, fuente_principal, color: tuple):
    """_summary_

    Args:
        texto (str): texto a renderizar
        fuente_principal (pygame.font.Font): fuente utilizada para renderizar el texto
        color (tuple): color del texto

    Returns:
        pygame.Surface: superficie con el texto renderizado
    """
    return fuente_principal.render(texto, True, color)

def dibujar_boton(screen, rect, texto: str, fuente_principal, color_fondo: tuple, color_texto: tuple) -> None:
    """_summary_

    Args:
        screen (pygame.Surface): superficie donde se dibuja el botón
        rect (pygame.Rect): rectángulo que define la posición y tamaño del botón
        texto (str): texto que se muestra en el botón
        fuente_principal (pygame.font.Font): fuente utilizada para renderizar el texto
        color_fondo (tuple): color de fondo del botón
        color_texto (tuple): color del texto del botón
    """
    pygame.draw.rect(screen, color_fondo, rect)
    texto_img = fuente_principal.render(texto, True, color_texto)
    texto_rect = texto_img.get_rect(center=rect.center)
    screen.blit(texto_img, texto_rect)

def dibujar_cruz(screen, rect):
    """_summary_

    Args:
        screen (pygame.Surface): superficie donde se dibuja la cruz
        rect (pygame.Rect): rectángulo que define la posición y tamaño de la cruz
    """
    pygame.draw.line(screen, ROJO, rect.topleft, rect.bottomright, 3)
    pygame.draw.line(screen, ROJO, rect.topright, rect.bottomleft, 3)

def dibujar_tablero(ventana, jugador: list, tam: int, filas: int, columnas: int, offset_x: int, offset_y: int) -> None:
    """_summary_

    Args:
        ventana (pygame.Surface): superficie donde se dibuja el tablero
        jugador (list): matriz que representa el nonograma del jugador
        tam (int): tamaño de cada celda del tablero
        filas (int): número de filas del tablero
        columnas (int): número de columnas del tablero
        offset_x (int): desplazamiento en el eje x para dibujar el tablero
        offset_y (int): desplazamiento en el eje y para dibujar el tablero
    """
    for f in range(filas):
        for c in range(columnas):
            x = offset_x + c * tam
            y = offset_y + f * tam

            valor = jugador[f][c]

            
            if valor == 0:
                pygame.draw.rect(ventana, BLANCO, (x, y, tam, tam))

            
            elif valor == 1:
                pygame.draw.rect(ventana, NEGRO, (x, y, tam, tam))

            
            elif valor == 2:
                pygame.draw.rect(ventana, BLANCO, (x, y, tam, tam))
                pygame.draw.line(ventana, ROJO, (x, y), (x+tam, y+tam), 3)
                pygame.draw.line(ventana, ROJO, (x+tam, y), (x, y+tam), 3)

            
            pygame.draw.rect(ventana, NEGRO, (x, y, tam, tam), 2)

def dibujar_pistas(ventana, fuente_principal, pistas_filas: list, pistas_columnas: list, tam: int, offset_x: int, offset_y: int) -> None:
    """_summary_

    Args:
        ventana (pygame.Surface): superficie donde se dibuja el tablero
        fuente_principal (pygame.font.Font): fuente utilizada para renderizar el texto
        pistas_filas (list): pistas de las filas del nonograma
        pistas_columnas (list): pistas de las columnas del nonograma
        tam (int): tamaño de cada celda del tablero
        offset_x (int): desplazamiento en el eje x para dibujar las pistas
        offset_y (int): desplazamiento en el eje y para dibujar las pistas
    """
    
    for i, pista in enumerate(pistas_filas):
        texto = " ".join(str(n) for n in pista)
        img = fuente_principal.render(texto, True, NEGRO)
        ventana.blit(img, (offset_x - 10 - img.get_width(), offset_y + i * tam + tam//3))


    for j, pista in enumerate(pistas_columnas):
        texto = "\n".join(str(n) for n in pista)
        lineas = texto.split("\n")

        for idx, linea in enumerate(lineas):
            img = fuente_principal.render(linea, True, NEGRO)
            ventana.blit(img, (
                offset_x + j * tam + tam//3,
                offset_y - (len(lineas) * img.get_height()) - 10 + idx * img.get_height()
            ))

def mostrar_game_over(ventana, font_game_over, calavera_img) -> None:
    """_summary_

    Args:
        ventana (pygame.Surface): superficie donde se dibuja el mensaje de game over
        fuente_game_over (pygame.font.Font): fuente utilizada para renderizar el texto de game over
        calavera_img (pygame.Surface): imagen de la calavera que se muestra en el game over
    """
    ventana.fill(NEGRO)
    ventana.blit(calavera_img, (250, 400))
    texto = font_game_over.render("GAME OVER", True, ROJO)
    rect = texto.get_rect(center=(ANCHO // 2, ALTO // 2 - 200))
    ventana.blit(texto, rect)
    pygame.display.update()
    pygame.time.delay(3000)
    
def dibujar_corazones(ventana, corazon_img, vidas: int) -> None:
    """_summary_

    Args:
        ventana (pygame.Surface): superficie donde se dibujan los corazones
        corazon_img (pygame.Surface): imagen del corazón que representa una vida
        vidas (int): número de vidas restantes
    """
    
    for i in range(vidas):
        
        ventana.blit(corazon_img, (0 + i * 40, -10))

def pedir_nombre(ventana, fuente_principal) -> str:
    """_summary_

    Args:
        ventana (pygame.Surface): superficie donde se dibuja la interfaz
        fuente_principal (pygame.font.Font): fuente utilizada para renderizar el texto

    Returns:
        str: nombre ingresado por el usuario
    """
    nombre = ""
    activo = True

    while activo:
        ventana.fill(GRIS)

        texto = fuente_principal.render("Ingresa tu nombre:", True, NEGRO)
        ventana.blit(texto, (200, 200))

        
        cuadro = pygame.Rect(200, 300, 400, 50)
        pygame.draw.rect(ventana, NEGRO, cuadro, 2)

        texto_nombre = fuente_principal.render(nombre, True, NEGRO)
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

    

def mostrar_ranking(ventana, fuente_principal, ranking: list) -> None:
    """_summary_

    Args:
        ventana (pygame.Surface): superficie donde se dibuja la interfaz
        fuente_principal (pygame.font.Font): fuente utilizada para renderizar el texto
        ranking (list): lista de diccionarios con los datos del ranking
    """
    activo = True

    while activo:
        ventana.fill(GRIS)

        
        titulo = fuente_principal.render("RANKING", True, NEGRO)
        ventana.blit(titulo, (ANCHO//2 - titulo.get_width()//2, 50))

        
        y = 150
        if not ranking:
            texto = fuente_principal.render("No hay registros aún.", True, NEGRO)
            ventana.blit(texto, (ANCHO//2 - texto.get_width()//2, y))
        else:
            for entry in ranking[:10]:
                nombre = entry["nombre"]
                tiempo = entry["tiempo"]
                archivo = entry["ruta"].split("/")[-1]

                linea = f"{nombre}  -  {tiempo}s  -  {archivo}"
                texto = fuente_principal.render(linea, True, NEGRO)
                ventana.blit(texto, (100, y))
                y += 40

        
        boton_volver = pygame.Rect(20, 700, 150, 50)
        dibujar_boton(ventana, boton_volver, "Volver", fuente_principal, GRIS, NEGRO)

    
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.collidepoint(evento.pos):
                    return

        pygame.display.update()



    
def mostrar_victoria(ventana, victoria_img) -> None:
    """_summary_

    Args:
        ventana (pygame.Surface): superficie donde se dibuja la interfaz
        victoria_img (pygame.Surface): imagen que se muestra al ganar
    """
    
    ventana.fill(BLANCO)
    ventana.blit(victoria_img, (0, 0))
    pygame.display.update()
    pygame.time.delay(3000)