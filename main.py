from paquete import *
import pygame

RUTA_FACIL = "nonogramas/facil/"
RUTA_MEDIO = "nonogramas/medio/"
RUTA_DIFICIL = "nonogramas/dificil/"

pygame.init()

ventana = pygame.display.set_mode((ANCHO, ALTO), pygame.RESIZABLE)

pygame.display.set_caption("Nonograma")

activo = True
while activo:
    
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            activo = False
            


pygame.quit()
        
    
   
            
            
           
            
            
            
            
        
                
                
        
            
            
            
            
        