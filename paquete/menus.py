import pygame
from paquete.config import *
from paquete.logica import *
from paquete.interfaz import *
from paquete.manejo_archivos import *



pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Nonograma")
fuente_principal = pygame.font.Font("paquete/fuentes/orbitron.ttf", TAM_FUENTE)
font_game_over = pygame.font.Font("paquete/fuentes/orbitron.ttf", FONT_GRANDE)
font_victoria = pygame.font.Font("paquete/fuentes/orbitron.ttf", FONT_GRANDE)
font_titulo = pygame.font.Font("paquete/fuentes/orbitron.ttf", 60)

RUTA_FACIL = "nonogramas/facil/"
RUTA_MEDIO = "nonogramas/medio/"
RUTA_DIFICIL = "nonogramas/dificil/"


def menu_principal(sonidos: dict) -> None:
    """_summary_

    Args:
        sonidos (dict): diccionario con los sonidos del juego
    """

    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.load("paquete/musica/ambiente.mp3")
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    activo = True
    while activo:
        ventana.fill(GRIS)
        texto_titulo = font_titulo.render("BIENVENIDO", True, NEGRO)
        rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, 150))
        ventana.blit(texto_titulo, rect_titulo)

        boton_jugar = pygame.Rect(0, 0, 200, 60)
        boton_ranking = pygame.Rect(0, 0, 200, 60)
        boton_salir = pygame.Rect(0, 0, 200, 60)

        boton_jugar.center = (ANCHO // 2, ALTO // 2 - 120)
        boton_ranking.center = (ANCHO // 2, ALTO // 2)
        boton_salir.center = (ANCHO // 2, ALTO // 2 + 120)

        dibujar_boton(ventana, boton_jugar, "Jugar", fuente_principal, NEGRO, GRIS)
        dibujar_boton(ventana, boton_ranking, "Ranking", fuente_principal, NEGRO, GRIS)
        dibujar_boton(ventana, boton_salir, "Salir", fuente_principal, NEGRO, GRIS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_jugar.collidepoint(evento.pos):
                    mostrar_menu_dificultad(sonidos)
                if boton_ranking.collidepoint(evento.pos):
                    ranking = cargar_ranking()
                    ranking = ordenar_ranking(ranking)
                    mostrar_ranking(ventana, fuente_principal, ranking)
                if boton_salir.collidepoint(evento.pos):
                    pygame.quit()
                    exit()

        pygame.display.update()


def mostrar_menu_dificultad(sonidos: dict) -> None:
    """_summary_

    Args:
        sonidos (dict): diccionario con los sonidos del juego

    """
    
    activo = True
    while activo:
        ventana.fill(GRIS)
        texto_titulo = font_titulo.render("DIFICULTADES", True, NEGRO)
        rect_titulo = texto_titulo.get_rect(center=(ANCHO // 2, 150))
        ventana.blit(texto_titulo, rect_titulo)

        boton_facil = pygame.Rect(0, 0, 200, 60)
        boton_medio = pygame.Rect(0, 0, 200, 60)
        boton_dificil = pygame.Rect(0, 0, 200, 60)
        boton_volver = pygame.Rect(20, 700, 150, 50)
        dibujar_boton(ventana, boton_volver, "Volver", fuente_principal, GRIS, NEGRO)
        
        boton_facil.center = (ANCHO // 2, ALTO // 2 - 120)
        boton_medio.center = (ANCHO // 2, ALTO // 2)
        boton_dificil.center = (ANCHO // 2, ALTO // 2 + 120)

        dibujar_boton(ventana, boton_facil, "Facil", fuente_principal, NEGRO, GRIS)
        dibujar_boton(ventana, boton_medio, "Medio", fuente_principal, NEGRO, GRIS)
        dibujar_boton(ventana, boton_dificil, "Difícil", fuente_principal, NEGRO, GRIS)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if boton_facil.collidepoint(evento.pos):
                    resultado = iniciar_juego(RUTA_FACIL, sonidos)

                    if resultado is None: 
                        return  menu_principal(sonidos)

                    nombre, tiempo, ruta_nonograma = resultado
                    ranking = cargar_ranking()
                    ranking = agregar_entrada(ranking, nombre, ruta_nonograma, tiempo)
                    ranking = ordenar_ranking(ranking)
                    guardar_ranking(ranking)
                    return menu_principal(sonidos)
                
                if boton_medio.collidepoint(evento.pos):
                    resultado = iniciar_juego(RUTA_MEDIO, sonidos)

                    if resultado is None:  
                        return menu_principal(sonidos) 

                    nombre, tiempo, ruta_nonograma = resultado
                    ranking = cargar_ranking()
                    ranking = agregar_entrada(ranking, nombre, ruta_nonograma, tiempo)
                    ranking = ordenar_ranking(ranking)
                    guardar_ranking(ranking)
                    return menu_principal(sonidos)
                    
                if boton_dificil.collidepoint(evento.pos):
                    resultado = iniciar_juego(RUTA_DIFICIL, sonidos)

                    if resultado is None:  
                        return menu_principal(sonidos) 

                    nombre, tiempo, ruta_nonograma = resultado
                    ranking = cargar_ranking()
                    ranking = agregar_entrada(ranking, nombre, ruta_nonograma, tiempo)
                    ranking = ordenar_ranking(ranking)
                    guardar_ranking(ranking)
                    return menu_principal(sonidos)

                if boton_volver.collidepoint(evento.pos):
                    return menu_principal(sonidos)
                    
        pygame.display.update()
    

    
def iniciar_juego(ruta_carpeta: str, sonidos: dict) -> tuple:
    """_summary_

    Args:
        ruta_carpeta (str): ruta a la carpeta que contiene los nonogramas
        sonidos (dict): diccionario con los sonidos del juego

    Returns:
        tuple: tupla con el nombre del jugador, el tiempo total y la ruta del nonograma
    """
    nombre_juagor = pedir_nombre(ventana, fuente_principal)
    ruta = elegir_nonograma_random(ruta_carpeta)
    jugador, resuelto = iniciar_partida(ruta)
    
    tiempo_inicio = pygame.time.get_ticks()
    corazon_img = pygame.image.load("paquete/imagenes/vida.png")
    corazon_img = pygame.transform.scale(corazon_img, (60, 60)) 
    calavera_img = pygame.image.load("paquete/imagenes/calavera.png")
    calavera_img = pygame.transform.scale(calavera_img, (300, 300))
    victoria_img = pygame.image.load("paquete/imagenes/victoria.png")
    victoria_img = pygame.transform.scale(victoria_img, (ANCHO, ALTO))


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
        ventana.fill(GRIS)
        dibujar_corazones(ventana, corazon_img, vidas)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos

                if offset_x <= x < offset_x + columnas * TAM_CELDA and \
                   offset_y <= y < offset_y + filas * TAM_CELDA:

                    fila = (y - offset_y) // TAM_CELDA
                    columna = (x - offset_x) // TAM_CELDA

                    
                    if evento.button == 1:
                        cambiar_estado(jugador, fila, columna, 1)
                    
                    elif evento.button == 3:
                        cambiar_estado(jugador, fila, columna, 2)

                   
                    if controlar_error(jugador, resuelto, fila, columna):
                    
                        error_en_revision = True
                        tiempo_error = pygame.time.get_ticks()
                        fila_error = fila
                        columna_error = columna

                    
                    if comparar_nonogramas(jugador, resuelto):
                        tiempo_total = (pygame.time.get_ticks() - tiempo_inicio) // 1000
                        pygame.mixer.music.stop()
                        sonidos["victoria"].play()
                        mostrar_victoria(ventana, victoria_img)
                        return nombre_juagor, tiempo_total, ruta

       
        if error_en_revision:

            
            if not controlar_error(jugador, resuelto, fila_error, columna_error):
                
                error_en_revision = False

            else:
                
                if pygame.time.get_ticks() - tiempo_error >= 3000:
                    vidas -= 1
                    sonidos["perder_vida"].play()
                    

                    
                    if vidas == 0:
                        pygame.mixer.music.stop()
                        sonidos["game_over"].play()
                        mostrar_game_over(ventana, font_game_over, calavera_img)
                        return

                   
                    error_en_revision = False

        
        dibujar_tablero(ventana, jugador, TAM_CELDA, filas, columnas,
                        offset_x, offset_y)

        dibujar_pistas(ventana, fuente_principal, pistas_filas, pistas_columnas,
                       TAM_CELDA, offset_x, offset_y)

        pygame.display.update()
                
    
                
    
                                    


        
        

                               
                               
                               
                               



