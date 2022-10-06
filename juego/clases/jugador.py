import pygame
from clases import disparo

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("juego/imagenes/nave.png")
        self.imagenExplota = pygame.image.load("juego/imagenes/naveExplota.png")
        #tomamos rextangulo imagen
        self.rect = self.imagenNave.get_rect()
        #posicion inicial nave
        self.rect.centerx = 240
        self.rect.centery = 690
        self.velocidad = 10 
        self.vida = True
        self.listaDisparo = []
        pygame.mixer.init()
        self.sonidoDisparo = pygame.mixer.Sound("juego/sonidos/meteoritos_sonidos_disparo.aiff")
        
    def mover(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > 490:
                self.rect.right = 490

    def disparar(self, x, y):
        if self.vida == True:
            misil = disparo.Misil(x, y)
            self.listaDisparo.append(misil)
            self.sonidoDisparo.play()

    def dibujar(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.imagenExplota , self.rect)