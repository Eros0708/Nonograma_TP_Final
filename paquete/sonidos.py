import pygame

def cargar_sonidos():
    sonidos = {}

    sonidos["fondo"] = pygame.mixer.Sound("paquete/musica/ambiente.mp3")
    sonidos["perder_vida"] = pygame.mixer.Sound("paquete/musica/perder_vida.mp3")
    sonidos["game_over"] = pygame.mixer.Sound("paquete/musica/game_over.mp3")
    sonidos["victoria"] = pygame.mixer.Sound("paquete/musica/victoria.mp3")

    return sonidos
