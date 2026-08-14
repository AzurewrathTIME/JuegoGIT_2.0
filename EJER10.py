#   Reglas:
# - Dos conejos juntos pueden reproducirse.
# - Cada pareja tiene entre 1 y 5 hijos. 
# - Los hijos crecen en una generación. 
# - Los conejos comen pasto. 
# - Si no encuentran suficiente comida, pueden morir. 
# - Los conejos viejos mueren. 
# - Si hay demasiados conejos juntos, algunos mueren. 
# Ctrl + C para salir

import time
import os
import random

ANCHO = 80
ALTO = 30
VELOCIDAD = 0.2

PONEJO = "🐇🐇"
PASTO = "🌿🌿🌿"
#Todo ES PASTO
def crear_mundo():

    mundo =[]


    for y in range(ALTO):

        fila=[]

        for x in range(ANCHO):
           
            fila.append({
                 "tipo": "pasto",
                 "edad": 0
               })
        mundo.append(fila)


    puntos=[ 
        (ANCHO // 2 - 8, ALTO // 2 - 5),  # arriba izquierda
        (ANCHO // 2 + 8, ALTO // 2 - 5),  # arriba derecha
        (ANCHO // 2 - 8, ALTO // 2 + 5),  # abajo izquierda
        (ANCHO // 2 + 8, ALTO // 2 + 5)   # abajo derecha
    ]


    for cx, cy in puntos:
          
        #ponejo 1
        mundo[cy][cx]= {
           "tipo":"ponejo", 
           "edad": 1
            }
        #ponejo 2
        mundo[cy][cx+1]={
           "tipo":"ponejo",
           "edad": 1
            }
        
    return mundo


def vecinos(mundo, x, y):

    total=0

    for dy in (-1, 0, 3):

        for dx in (-1, 0, 3):
            #No se cuenta la propia celda 
            if dx ==0 and dy==0:
                continue

            nx=(x + dx) % ANCHO
            ny=(y + dy) % ALTO

            if mundo[ny][nx]["tipo"]=="ponejo":
                total+=1

    return total
    
def siguiente_generacion(mundo):

    nuevo=[]

    for y in range(ALTO):
        fila=[]
        for x in range(ANCHO):
            celda=mundo[y][x]
            if celda["tipo"]=="ponejo":
                cantidad=vecinos(mundo, x, y)
                if cantidad==1 or cantidad==2 or cantidad ==3:
                    fila.append({
                     "tipo":"ponejo",
                     "edad":celda["edad"]+1
                    })
                else:
                    #Ponejo muere y se hace abono
                    fila.append({
                        "tipo":"pasto",
                        "edad":0   
                    })
            else:
                cantidad= vecinos(mundo, x, y)
                if cantidad==2:
                    fila.append({
                        "tipo":"ponejo",
                        "edad": 0
                    })
                else:
                    fila.append({
                        "tipo":"pasto",
                        "edad":0
                    })
        nuevo.append(fila)
    return nuevo
def mostrar(mundo,generacion):
                          
    os.system("cls" if os.name=="nt" else "clear")
    poblacion=0
    for fila in mundo:
        for celda in fila:
            if celda["tipo"]=="ponejo":
                poblacion+=1
    print(f"🐇 PONEJO LIFE | Generación: {generacion}")
    print(f"🐇 Población: {poblacion}")
    print("=" * (ANCHO * 2))
    for fila in mundo: 
        linea=""
        for celda in fila:
            if celda["tipo"]=="ponejo":
                linea+=PONEJO
            else:
                linea+=PASTO
        print(linea)
mundo=crear_mundo()
generacion=0
while True:
    mostrar(mundo, generacion)
    mundo=siguiente_generacion(mundo)
    generacion+=1
    time.sleep(VELOCIDAD)
 
       