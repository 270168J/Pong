import pygame as pg
from figura_class import Pelota,Raqueta

ANCHO = 800
ALTO = 600
BLANCO = (255,255,255)
AMARILLO = (255,255,0)
ROJO = (255,0,0)
NARANJA = (255,128,0)
VERDE = (0,128,24)
FPS = (280)#fotogramas por segundo
class Partida:
     def __init__(self):
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()


        self.pelota = Pelota(ANCHO//2,ALTO//2,vx=2,vy=2)
        self.raqueta1 = Raqueta(5,ALTO//2,vy=5)
        self.raqueta2 = Raqueta(ANCHO-5,ALTO//2,vy=5)

        self.font = pg.font.Font ("fonts/pressStart2.ttf", 15)#marcador
        self.fuenteTemp = pg.font.Font("fonts/pressStart2.ttf",20)#fuente temporizador
        self.marcador1 = 0
        self.marcador2 = 0
        self.quienMarco = ""
        self.temporizador = 15000#son milisegundos

     def bucle_fotograma(self):
         game_over = False        
         while not game_over and (self.marcador1 < 5 or self.marcador2 < 5) and self.temporizador > 0:
        
             salto_tiempo = self.tasa_refresco.tick(FPS)#1000/280=fotogramas por segundo en milisegundos
             self.temporizador -= salto_tiempo
        

            
             for evento in pg.event.get():                   
                 if evento.type == pg.QUIT:
                     game_over = True          

             self.raqueta1.mover(pg.K_w,pg.K_s)#mover raqueta1 izquierda
             self.raqueta2.mover(pg.K_UP,pg.K_DOWN)#mover raqueta2 derecha
             self.quienMarco = self.pelota.mover()#mover pelota

            
                         
             self.pantalla_principal.fill(VERDE)#pintado de pantalla
             self.pelota.comprobar_choqueV2(self.raqueta1,self.raqueta2)

             self.marcador()
             self.linea_disc()

             tiempo = self.font.render(str(int(self.temporizador/1000) ),0,ROJO)
             self.pantalla_principal.blit(tiempo,(400, 20))

             
    
              #pelota.comprobar_choque(raqueta1,raqueta2)        
              #self.pelota.comprobar_choqueV2(self.raqueta1,self.raqueta2)
             #self.pelota.marcador(self.pantalla_principal)#pintado de marcador
                  
             
             
             self.pelota.dibujar(self.pantalla_principal)#pintado de pelota
             self.raqueta1.dibujar(self.pantalla_principal)#pintado raqueta1
             self.raqueta2.dibujar(self.pantalla_principal)#pintado raqueta2
             
             self.mostrar_jugador()

    
             pg.display.flip()


         pg.quit()


     def linea_disc(self):    
             cont_linea1 = 0
             cont_linea2 = 50

             while cont_linea1 <= 560 and cont_linea2 <= 630:

                 pg.draw.line(self.pantalla_principal, (BLANCO), (400,cont_linea1), (400,cont_linea2), width=10)
                 cont_linea1 += 70
                 cont_linea2 += 70

     def mostrar_jugador(self):

            jugador1 = self.font.render("jugador 1",0,AMARILLO)
            jugador2 = self.font.render("jugador 2",0,AMARILLO)
            self.pantalla_principal.blit(jugador1, (160,30))#marcador
            self.pantalla_principal.blit(jugador2, (565,30))#marcado

     def marcador(self):
            if self.quienMarco == "right":
                self.marcador1 += 1
            elif self.quienMarco == "left":
                self.marcador2 += 1 
            marcadorIzquierdo = self.font.render(str(self.marcador2),0,AMARILLO)
            marcadorDerecho = self.font.render(str(self.marcador1),0,AMARILLO)
            self.pantalla_principal.blit(marcadorDerecho, (200,50))#marcador
            self.pantalla_principal.blit(marcadorIzquierdo, (600,50))#marcador
             