import pygame
from paquete.menus import menu_principal
from paquete.sonidos import cargar_sonidos

pygame.init()
pygame.mixer.init()
sonidos = cargar_sonidos()

menu_principal(sonidos)




            
            
            
        
                
                
        
            
            
            
            
        