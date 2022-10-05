import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Carga imagen y posicion al Azar")
#Colores
colorFondo = (1, 150, 70)
#Carga imagen
imagen = pygame.image.load("imagenes/large.jpeg")
posXI, posYI = (0, 0)
while True:
    ventana.fill(colorFondo)
    ventana.blit(imagen, (posXI, posYI))
    for i in range(1,10):
        posX, posY = randint(1,500), randint(1,500)
        r, g, b = randint(0,255), randint(0, 255), randint(0, 255)
        colorRectangulo = (r, g, b)
        pygame.draw.rect(ventana, colorRectangulo, (posX, posY, 50, 80) )
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()