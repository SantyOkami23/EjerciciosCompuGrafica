import pygame
import sys
import mi_lib
ANCHO = 600
ALTO = 600
ORIGEN = (400,450)
LIMITES = [-ORIGEN[0],ANCHO-ORIGEN[0]]
Pantalla = pygame.display.set_mode([800, 650])
rojo=[255,0,0]
blanco=[255,255,255]
azul=[0,255,255]
morado=[116,11,228]
negro=[0,0,0]
amarillo=[228,218,11]


def Linea (ventana,color,pos_inicio,pos_final):
    pygame.draw.line(ventana,color,pos_inicio,pos_final,5)
    pygame.display.flip()

linea = negro
frontal = rojo
lateral = azul
superior = morado
piso = blanco
atras = amarillo


puntos= [[0,0],[0,70],[-105,35], [-105,105],[70, 105],[-35, 140],[70, 175],[-35, 210], [105, 192.5],[0, 227.5],
         [105, 122.5],[0, 157.5],[175, 157.5],[70, 192.5],[175, 87.5],[70, 122.5]]

def figura(s, g, v):
    # Coordenadas de cada punto del isometrico
    p1 = [0, 0]
    p2 = [0, 70]
    p3 = [-105, 35]
    p4 = [-105, 105]
    p5 = [70, 105]
    p6 = [-35, 140]
    p7 = [70, 175]
    p8 = [-35, 210]
    p9 = [105, 192.5]
    p10 = [0, 227.5]
    p11 = [105, 122.5]
    p12 = [0, 157.5]
    p13 = [175, 157.5]
    p14 = [70, 192.5]
    p15 = [175, 87.5]
    p16 = [70, 122.5]

    p1 = CartesianoPos(origen, pp1)
    p2 = CartesianoPos(origen, pp2)
    p3 = CartesianoPos(origen, pp3)
    p4 = CartesianoPos(origen, pp4)
    p5 = CartesianoPos(origen, pp5)
    p6 = CartesianoPos(origen, pp6)
    p7 = CartesianoPos(origen, pp7)
    p8 = CartesianoPos(origen, pp8)
    p9 = CartesianoPos(origen, pp9)
    p10 = CartesianoPos(origen, pp10)
    p11 = CartesianoPos(origen, pp11)
    p12 = CartesianoPos(origen, pp12)
    p13 = CartesianoPos(origen, pp13)
    p14 = CartesianoPos(origen, pp14)
    p15 = CartesianoPos(origen, pp15)
    p16 = CartesianoPos(origen, pp16)

pygame.draw.polygon(Pantalla, atras, [p6, p12, p10, p8])  # primer cara atras
pygame.draw.polygon(Pantalla, atras, [p3, p16, p14, p4])  # segunda cara atras
pygame.draw.polygon(Pantalla, piso, [p1, p15, p16, p3])  # priemr del piso
pygame.draw.polygon(Pantalla, lateral, [p1, p2, p4, p3])  # primer cara lateral
pygame.draw.polygon(Pantalla, superior, [p2, p5, p6, p4])  # priemr cara superior
pygame.draw.polygon(Pantalla, lateral, [p15, p13, p14, p16])  # cuarta cara lateral
pygame.draw.polygon(Pantalla, frontal, [p1, p15, p13, p2])  # segunda cara adelante
pygame.draw.polygon(Pantalla, superior, [p11, p13, p14, p12])  # tercera cara superior
pygame.draw.polygon(Pantalla, lateral, [p5, p6, p8, p7])  # segunda cara lateral
pygame.draw.polygon(Pantalla, lateral, [p11, p12, p10, p9])  # tercera cara lateral
pygame.draw.polygon(Pantalla, frontal, [p5, p11, p9, p7])  # primer cara adelante
pygame.draw.polygon(Pantalla, superior, [p7, p9, p10, p8])  # segunda cara superior


puntos_pantalla=[]
x = 0

for i in puntos:
    punto = mi_lib.transformada_r2(i,ORIGEN)
    puntos_pantalla.append(punto)
if __name__ == "__main__":
    pygame.init()
    ventana = pygame.display.set_mode([ANCHO,ALTO])
    while True:
        puntos_dibujar = []
        #captura todos los eventos
        for event in pygame.event.get():
            #registra el cierre del programa
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    aux_punto=[]
                    puntos_pantalla=[]
                    for i in puntos:
                        aux=mi_lib.transformada_desplazamiento(i,40,0)
                        aux_dibujar = mi_lib.transformada_r2(aux,ORIGEN)
                        aux_punto.append(aux)
                        puntos_pantalla.append(aux_dibujar)
                    puntos = []
                    puntos = aux_punto
                    ventana.fill([0,0,0])






                if event.key == pygame.K_LEFT:
                    aux_punto=[]
                    puntos_pantalla=[]
                    for i in puntos:
                        aux=mi_lib.transformada_desplazamiento(i,-10,0)
                        aux_dibujar = mi_lib.transformada_r2(aux,ORIGEN)
                        aux_punto.append(aux)
                        puntos_pantalla.append(aux_dibujar)
                    puntos = []
                    puntos = aux_punto
                    ventana.fill([0,0,0])
                if event.key == pygame.K_UP:
                    aux_punto=[]
                    puntos_pantalla=[]
                    for i in puntos:
                        aux=mi_lib.transformada_desplazamiento(i,0,10)
                        aux_dibujar = mi_lib.transformada_r2(aux,ORIGEN)
                        aux_punto.append(aux)
                        puntos_pantalla.append(aux_dibujar)
                    puntos = []
                    puntos = aux_punto
                    ventana.fill([0,0,0])
                if event.key == pygame.K_DOWN:
                    aux_punto=[]
                    puntos_pantalla=[]
                    for i in puntos:
                        aux=mi_lib.transformada_desplazamiento(i,0,-10)
                        aux_dibujar = mi_lib.transformada_r2(aux,ORIGEN)
                        aux_punto.append(aux)
                        puntos_pantalla.append(aux_dibujar)
                    puntos = []
                    puntos = aux_punto
                    ventana.fill([0,0,0])
        mi_lib.dibujar_plano(ORIGEN,[ANCHO,ALTO],ventana)
        pygame.draw.polygon(ventana,[255,255,255],puntos_pantalla,2)
        pygame.display.flip()
