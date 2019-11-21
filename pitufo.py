import pygame
import random

letras=["imagen/A.png","imagen/B.png","imagen/C.png","imagen/D.png","imagen/E.png","imagen/F.png","imagen/G.png","imagen/H.png","imagen/I.png","imagen/J.png","imagen/K.png","imagen/L.png","imagen/n.png","imagen/Ñ.png","imagen/O.png","imagen/P.png","imagen/Q.png","imagen/R.png","imagen/S.png","imagen/T.png","imagen/U.png","imagen/V.png","imagen/ww.png","imagen/X.png","imagen/Y.png","imagen/zz.png"]
from lib.Pitufo import *
from lib.Arbol import *
from lib.Gargame import *
from lib.Letras import *
pygame.init()
pitufo=Pitufo([20,20],"imagen/pitufocabesza.png","imagen/pitufocabesza.png")   
pitufo.imagen=pygame.image.load(pitufo.imagenA)
pitufo.rectangulo=pitufo.imagen.get_rect()
imgarbol=pygame.image.load("imagen/planta1.png")

comienso=pygame.image.load("imagen/principio.png")
fondo=pygame.image.load("imagen/fondo.png")
perdiste=pygame.image.load("imagen/perdiste1.jpg")
terminado=pygame.image.load("imagen/ganaste.png")
gato=Gargame("imagen/gato.png",[600,400])
gato.imagen=pygame.image.load("imagen/gato.png")
gato.rectangulo=gato.imagen.get_rect()
gato.rectangulo[0]=gato.rectangulo[0]+580
gato.rectangulo[1]=gato.rectangulo[1]+400

g=Letra()
g.imagen=pygame.image.load(letras[6])
g.cordenadas=[random.randint(5,670),random.randint(5,450)]
g.rectangulo=g.imagen.get_rect( )
g.rectangulo[0]=g.rectangulo[0]+ g.cordenadas[0]
g.rectangulo[1]=g.rectangulo[1]+ g.cordenadas[1]


a=Letra()
a.imagen=pygame.image.load(letras[0])
a.cordenadas=[random.randint(5,670),random.randint(5,450)]
a.rectangulo=a.imagen.get_rect( )
a.rectangulo[0]=a.rectangulo[0]+ a.cordenadas[0]
a.rectangulo[1]=a.rectangulo[1]+ a.cordenadas[1]
t=Letra()
t.imagen=pygame.image.load(letras[19])
t.cordenadas=[random.randint(5,670),random.randint(5,450)]
t.rectangulo=t.imagen.get_rect( )
t.rectangulo[0]=t.rectangulo[0]+ t.cordenadas[0]
t.rectangulo[1]=t.rectangulo[1]+ t.cordenadas[1]
o=Letra()
o.imagen=pygame.image.load(letras[14])
o.cordenadas=[random.randint(5,670),random.randint(5,450)]
o.rectangulo=o.imagen.get_rect( )
o.rectangulo[0]=o.rectangulo[0]+ o.cordenadas[0]
o.rectangulo[1]=o.rectangulo[1]+ o.cordenadas[1]
gato1=[g,a,t,o]
arbol1=Arbol(imgarbol,(random.randint(40,650,),random.randint(40,450)))
arbol1.rectangulo=arbol1.imagen.get_rect()
arbol2=Arbol(imgarbol,(random.randint(40,650,),random.randint(40,450)))
arbol2.rectangulo=arbol2.imagen.get_rect()
arbol3=Arbol(imgarbol,(random.randint(40,650,),random.randint(40,450)))
arbol3.rectangulo=arbol3.imagen.get_rect()
arbol4=Arbol(imgarbol,(random.randint(40,650,),random.randint(40,450)))
arbol4.rectangulo=arbol4.imagen.get_rect()
arbol5=Arbol(imgarbol,(random.randint(40,650,),random.randint(40,450)))
arbol5.rectangulo=arbol5.imagen.get_rect()


# Establecemos las dimensiones de la pantalla [largo,altura]
dimenciones = [700,500]
pantalla = pygame.display.set_mode(dimenciones) 
pygame.display.set_caption("Mi Primer juego en Informática")
  
#El bucle se ejecuta hasta que el usuario hace click sobre el botón de cierre.
 
hecho = False
musicaganador="sonido/Ganaste.mp3" 
musicaperdedor="sonido/Perdiste.mp3"
musicajuego="sonido/musicafondo.mp3"  
# Se usa para establecer cuan rápido se actualiza la pantalla
listaLetras=[g,a,t,o]
reloj = pygame.time.Clock()
instjuego=0  
cont=0

class musica:
    def __init__(self,musicajuego,musicaganado,musicaperdedor):
        self.juego=musicajuego
        self.ganador=musicaganador
        self.perdedor=musicaperdedor
        self.tipo= 0
    def pley (self):
        if self.tipo == 0:
            pygame.mixer.music.load(self.juego)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
        if self.tipo == 1:
            pygame.mixer.music.load(self.ganador)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(1)
        if self.tipo == 2:
            pygame.mixer.music.load(self.perdedor)
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(1)

musica_so=musica(musicajuego,musicaganador,musicaperdedor)  

             
            
                
# -------- Bucle principal del Programa -----------
while not hecho:
    # --- Bucle principal de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            hecho = True
    termina=0        
    termina= len(listaLetras)-1
    
  
    if cont > termina:
        
        instjuego=3 
        
           
    if instjuego==0:
        
        pantalla.fill((0, 255, 0))
        pantalla.blit(comienso,(0,0))
        pygame.display.flip()
        tecla=pygame.key.get_pressed()
    
        if tecla[K_SPACE]:
            instjuego=1
            musica_so.pley()
            
          
    if instjuego==1:
        
        gato.mover(pitufo.cordenadas)    
        pitufo.mover(dimenciones)
        comida=pitufo.comerletra(listaLetras[cont].rectangulo)
        
        
        
        toca=gato.choquepit(pitufo.rectangulo)
        if toca=="toca":
            instjuego= 2
            musica_so.tipo=2
            musica_so.pley()
            
          


            
            
            # --- LA LÓGICA DEL JUEGO DEBERÍA IR AQUÍ
        else:
            # --- EL CÓDIGO DE DIBUJO DEBERÍA IR AQUÍ
            
            # Primero, limpia la pantalla con blanco. No vayas a poner otros comandos de dibujo encima 
            # de esto, de otra forma serán borrados por este comando:
            pantalla.fill((0, 255, 0))
            pantalla.blit(fondo,(0,0))
            pantalla.blit(pitufo.imagen,pitufo.cordenadas)
            pantalla.blit(arbol1.imagen,arbol1.cordenadas)
            pantalla.blit(arbol2.imagen,arbol2.cordenadas)
            pantalla.blit(arbol3.imagen,arbol3.cordenadas)
            pantalla.blit(arbol4.imagen,arbol4.cordenadas)
            pantalla.blit(arbol5.imagen,arbol5.cordenadas)
            pantalla.blit(gato.imagen,gato.cordenadas)
            pantalla.blit(listaLetras[cont].imagen,listaLetras[cont].cordenadas)
       
        if comida==1:
            cont=cont + 1  
        
        if cont > termina:   
            musica_so.tipo=1
            musica_so.pley()
        

            # --- Avanzamos y actualizamos la pantalla con lo que hemos dibujado.
        pygame.display.flip()
        
            # --- Limitamos a 60 fotogramas por segundo (frames per second)
        reloj.tick(60)
        
        
    if instjuego==2:
       
        pantalla.fill((0, 255, 0))
        pantalla.blit(perdiste,(0,0))
        pygame.display.flip()
    if instjuego==3:
        
        pantalla.fill((0, 255, 0))
        pantalla.blit(terminado,(0,0))
        pygame.display.flip()
# Cerramos la ventana y salimos.
# Si te olvidas de esta última línea, el programa se 'colgará'
# al salir si lo hemos estado ejecutando desde el IDLE.
pygame.quit()