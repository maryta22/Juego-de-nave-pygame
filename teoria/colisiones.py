import pygame
import sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Movimiento Raton")
#Colores
colorFondo = (1, 150, 70)
colorCuadro01 = (255,255,0)
colorCuadro02 = (0, 255, 255)
#variables 
velocidad = 5
direccion = True
posX01, posY01 = randint(1, 400), randint(1, 300)
posX02, posY02 = randint(1, 400), randint(1, 300)
lado = 40
while True:
    ventana.fill(colorFondo)
    cuadro01 = pygame.draw.rect(ventana, colorCuadro01, (posX01, posY01, lado, lado))
    cuadro02 = pygame.draw.rect(ventana, colorCuadro02, (posX02, posY02, lado, lado))
    #detecta colision
    if cuadro01.colliderect(cuadro02):
        print(f"Collision! en coordena {posX01} : {posY01}")
        posX02, posY02 = randint(1, 400), randint(1, 300)
        cuadro02.left = posX02 - (lado/2)
        cuadro02.top = posY02 - (lado/2)
    #detecta movimiento ratón
    posX01, posY01 = pygame.mouse.get_pos()
    posX01 = posX01 - (lado/2)
    posY01 = posY01 - (lado/2)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()