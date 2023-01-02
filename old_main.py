from figura_class import Pelota,Raqueta
import pygame as pg

pg.init()#pantalla principal en bucle hata el game_over
pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")


#font = pg.font.Font (None, 40)#marcador
#text = font.render('Puntos:',1,(255,255,0))#marcador


#definir la tasa de refresco de nuestro bucle de fotogramas fps=fotograma por segundo
cronometro = pg.time.Clock()
#objetos
pelota = Pelota(400,300)
raqueta1 = Raqueta(5,300)
raqueta2 = Raqueta(795,300)
#velocidad
raqueta1.vx=5
raqueta2.vy=5
pelota.vx=1

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
     
pg.quit()         