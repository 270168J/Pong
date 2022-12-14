import pygame as pg

class Pelota:
    def __init__(self,pos_x,pos_y,radio=15,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
        self.font = pg.font.Font (None, 40)#marcador

    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)

    def mover(self,y_max=600,x_max=800):
        self.pos_x += self.vx
        self.pos_y += self.vy

        #print("posicion x:", self.pos_x + self.radio)imprime la posicion en la consola
        #print("posicion y:",self.pos_y + self.radio)imprime la posicion en la consola

        if self.pos_y >= y_max-self.radio or self.pos_y < 0+self.radio:#para que rebote arriba y abajo
            self.vy *= -1
        #objetivo que la pelota desaparezcaen los limites y vuelva a aparecer rebotando
        #hacia el lado que vino
        if self.pos_x >= x_max+self.radio*10:#limite derecha 
            #contar el gol
            #self.contadorIzquierda +=1

            self.pos_x = x_max//2
            self.pos_y = y_max//2

            self.vx *= -1 
            self.vy *= -1

            return "right"    

        if self.pos_x < 0 - self.radio*10:#limite izquierdo
            #self.contadorDerecha +=1

            self.pos_x = x_max//2
            self.pos_y = y_max//2

            self.vx *= -1 
            self.vy *= -1

            return "left"

    #def marcador(self,pantalla_principal):     
           #marcadorIzquierdo = self.font.render(str(self.contadorDerecha),0,(255,255,0))
           #marcadorDerecho = self.font.render(str(self.contadorIzquierda),0,(255,255,0))
           #pantalla_principal.blit(marcadorDerecho, (200,50))#marcador
           #pantalla_principal.blit(marcadorIzquierdo, (600,50))#marcador

    @property#con property evitamos pasar los datos entre parentesis
    def derecha(self):
        return self.pos_x + self.radio
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    @property
    def arriba(self):
        return self.pos_y - self.radio
    @property
    def abajo(self):
        return self.pos_y + self.radio

    def comprobar_choque(self,r1,r2):
        if self.derecha >= r2.izquierda and \
           self.izquierda <= r2.derecha and\
           self.abajo >= r2.arriba and\
           self.arriba <= r2.abajo:
           self.vx *= -1

        if self.derecha >= r1.izquierda and \
           self.izquierda <= r1.derecha and\
           self.abajo >= r1.arriba and\
           self.arriba <= r1.abajo:
           self.vx *= -1
    def comprobar_choqueV2(self,*raquetas):
        for r in raquetas:
            if self.derecha >= r.izquierda and \
               self.izquierda <= r.derecha and\
               self.abajo >= r.arriba and\
               self.arriba <= r.abajo:
                    self.vx *= -1
                    return

    """
    def posicionX(self):
        return self.pos_x+self.radio
    
    def posicionY(self):
        return self.pos_y+self.radio

    def izquierda(self):
        if self.pos_x < 400:
            return True
        return False

    def derecha(self):
        if self.pos_y > 400:
            return True
        return False

    def arriba(self):
        if self.pos_y < 300:
            return True
        return False

    def abajo(self):
        if self.pos_y > 300:
            return True
        return False
    """
    '''
        if self.pos_x >= x_max - self.radio or self.pos_x < 0 + self.radio:
            self.vx *= -1
        if self.pos_y >= y_max - self.radio or self.pos_y < 0 + self.radio:
            self.vy *= -1
        
        
        if self.pos_x >= x_max or self.pos_x<0:
            self.pos_x = x_max//2
            self.pos_y = y_max//2

            self.vy *= -1
            self.vx *= -1
    '''


class Raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=100,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h))  


    def mover(self,tecla_arriba,tecla_abajo,y_max=600,y_min=0):
        estado_teclas = pg.key.get_pressed()#movimiento raquetas

        if estado_teclas[tecla_arriba] == True and self.pos_y > (y_min+self.h//2):
           self.pos_y -= 1
        if estado_teclas[tecla_abajo] == True and self.pos_y < (y_max -self.h//2):
           self.pos_y += 1

    @property
    def arriba(self):
        return self.pos_y - self.h//2
   
    @property
    def abajo(self):
        return self.pos_y + self.h//2

    @property
    def izquierda(self):
        return self.pos_x - self.w//2

    @property
    def derecha(self):
        return self.pos_x + self.w//2