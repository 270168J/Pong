import pygame as pg

class Pelota:
    def __init__(self,pos_x,pos_y,radio=15,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)

    def mover(self,x_max=800,y_max=600):
        self.pos_x += self.vx
        self.pos_y += self.vy
        #cambiamos para que si se marca gol a un lado salga exactamante
        #en el sentido contrario rebotando
        
        if self.pos_y >= y_max- self.radio or self.pos_y < self.radio:
            self.vy = self.vy*-1

        if self.pos_x >= x_max or self.pos_x<0:
            self.pos_x = x_max//2
            self.pos_y = y_max//2

            self.vy *= -1
            self.vx *= -1
        


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