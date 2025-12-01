import pygame

def cargar_sonidos():
    sonidos = {}

    sonidos["fondo"] = "paquete/musica/ambiente.mp3"
    
    sonidos["perder_vida"] = pygame.mixer.Sound("paquete/musica/perder_vida.wav")
    sonidos["game_over"] = pygame.mixer.Sound("paquete/musica/game_over.wav")
    sonidos["victoria"] = pygame.mixer.Sound("paquete/musica/victoria.wav")
    
    return sonidos
