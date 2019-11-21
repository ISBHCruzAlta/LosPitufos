class Gargame:
    def __init__(self,imagen,cordenada):
        self.imagen=imagen
        self.cordenadas=cordenada
        self.rectangulo=""
    def mover (self,cordenada): 
        
        
        difx= self.cordenadas[0]-cordenada[0]
        
        if difx >0:
            
            self.cordenadas[0]= self.cordenadas[0]-1
            self.rectangulo[0]= self.rectangulo[0]-1
        else:
            self.cordenadas[0]= self.cordenadas[0]+1
            self.rectangulo[0]= self.rectangulo[0]+1
        dify=self.cordenadas[1]-cordenada[1] 
        if dify >0:
            self.cordenadas[1]=self.cordenadas[1]-1
            self.rectangulo[1]=self.rectangulo[1]-1
        else:
            self.cordenadas[1]=self.cordenadas[1]+1
            self.rectangulo[1]=self.rectangulo[1]+1
    def choquepit(self,pituforect):
        
        if self.rectangulo.colliderect(pituforect):
            return "toca"
        else:
            return 0   
           


            