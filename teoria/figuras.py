import pygame
import sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Titulo de la ventana")
#Colores
colorFondo = (1, 150, 70)
colorLinea = (255,128, 0)
colorCirculo = (255, 255, 0)
colorFiguras = (205,0,155)
while True:
    ventana.fill(colorFondo)
    #Lineas
    pygame.draw.line(ventana, colorLinea, (20,30),(200,100),10)
    pygame.draw.line(ventana, colorLinea, (80,190),(100,150),10)
    pygame.draw.line(ventana, colorLinea, (10,30),(250,190),10)
    #Circulos
    pygame.draw.circle(ventana, colorCirculo, (400,200),100,10)
    pygame.draw.circle(ventana, colorCirculo, (150,150),100,10)
    #Figuras
    pygame.draw.rect(ventana, colorFiguras, (100,200,120,250))
    pygame.draw.polygon(ventana, colorFiguras, ((400, 400),
                        (500,400), (550, 500), (490, 500)))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()