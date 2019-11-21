import pygame

from pygame.locals import *

class Pitufo:
    def __init__(self,cordenada,imagenA,imagenC):

        self.imagen=""
        self.cordenadas=cordenada
        self.imagenA=imagenA
        self.imagenC=imagenC
        self.rectangulo="" 
    def mover(self,dimenciones):

        tecla=pygame.key.get_pressed()
    
        if tecla[K_RIGHT]:
            if self.rectangulo.right<dimenciones[0]-5:
                
                self.cordenadas[0]=self.cordenadas[0]+5
                self.rectangulo[0]=self.rectangulo[0]+5
            
        if tecla[K_LEFT]:
            if self.rectangulo.left>0:

                self.cordenadas[0]=self.cordenadas[0]-5
                self.rectangulo[0]=self.rectangulo[0]-5
        if tecla[K_DOWN]:
            if self.rectangulo.bottom<dimenciones[1]-5:
                self.cordenadas[1]=self.cordenadas[1]+5
                self.rectangulo[1]=self.rectangulo[1]+5
        if tecla[K_UP]:
            if self.rectangulo.top>0: 
                self.cordenadas[1]=self.cordenadas[1]-5
                self.rectangulo[1]=self.rectangulo[1]-5  
    def comerletra(self,letrarect):
        
        if self.rectangulo.colliderect(letrarect):
            return 1
        else: 
            return 0


