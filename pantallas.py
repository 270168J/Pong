import pygame as pg
from figura_class import Pelota,Raqueta

ANCHO = 800
ALTO = 600

class Partida:
     def __init__(self):
        self.pantalla_inicial = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()


        self.pelota = Pelota(ANCHO//2,ALTO//2,vx=2,vy=2)
        self.raqueta1 = Raqueta(5,ALTO//2,vy=5)
        self.raqueta2 = Raqueta(ANCHO-5,ALTO//2,vy=5)

     def bucle_fotograma(self):
        game_over = False

        while not game_over:
    
         #imprimir los milisegundos que tarda cada fotograma actualmente
         vt = cronometro.tick(300)#vt=variable para controlar la velocidad entre fotogramas, puedes llamarlo como quieras
         #print(vt)
         for evento in pg.event.get():
           if evento.type == pg.QUIT:
             game_over = True 


    raqueta1.mover(pg.K_w,pg.K_s)#mover raqueta1 izquierda
    raqueta2.mover(pg.K_UP,pg.K_DOWN)#mover raqueta2 derecha
    pelota.mover()#mover pelota
    
    pantalla_principal.fill((0,128,24))#pintado de pantalla

    #logica de choque
    """
    if pelota.derecha >= raqueta2.izquierda and \
       pelota.izquierda <= raqueta2.derecha and\
       pelota.abajo >= raqueta2.arriba and\
       pelota.arriba <= raqueta2.abajo:
           pelota.vx *= -1

    if pelota.derecha >= raqueta1.izquierda and \
       pelota.izquierda <= raqueta1.derecha and\
       pelota.abajo >= raqueta1.arriba and\
       pelota.arriba <= raqueta1.abajo:
           pelota.vx *= -1
    """
    #pelota.comprobar_choque(raqueta1,raqueta2)
    pelota.comprobar_choqueV2(raqueta1,raqueta2)
    pelota.marcador(pantalla_principal)#pintado de marcador
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=10)#linea del medio
    pelota.dibujar(pantalla_principal)#pintado de pelota
    raqueta1.dibujar(pantalla_principal)#pintado raqueta1
    raqueta2.dibujar(pantalla_principal)#pintado raqueta2


    
    pg.display.flip()