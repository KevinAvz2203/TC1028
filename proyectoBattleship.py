# Ximena Lopez y Kevin Valdez

# 14 de Oct del 2021

# Proyecto Battleship

import random
import time

""" Requisitos: 
* Crear un tablero simulado en un .txt por renglones y columnas                                                 
* Ambos jugadores pueden bajar el archivo de Github                                                                                                                      
* Cada que un jugador ataca, se guarda el daño y se regreasa el archivo a Github                                                                                                          
* No se debe permitir a un jugador jugar cuando es el turno del otro y prevenir si esto ocurre                                                                                                                
* El tamaño del tablero puede ser fijo o mediante INPUT al igual que las naves
* La ubicacion de las naves debe ser random y que no se encimnen 
* Se recomienda que exista un procedimiento de inicialización de dimensiones , número de naves por jugador y localización                                                
* El tablero debe ser un numero igual para ambos jugadores
 """

# Crear el tablero en el txt battleship, abrirlo y crearlo como matriz
# Pedir cantidad de barcos a generar
# Definir tamaño del tablero
# Colocar barcos random
# transformar tablero a txt 

def comprobarControl():
    # Se abre el archivo control para confirmar que jugador es 
    fo = open("control.txt", "r")
    turno = fo.readline()
    fo.close()

    # Se divide el archivo en lista para identificar al jugador
    turno = turno.split(" ")

    # if para saber que jugador eres
    if turno[0] == "1":
        print("Es tu turno, hora de atacar!!")
    else:
        print("No es tu turno, no seas impaciente")
        exit()

def crearTablero(tablero, numBarcos):
    # lista varia para pasar los datos del txt
    arctxt = []

    fo = open("battleship.txt", "r+")

    while True:
        linea = fo.readline()
        if (not linea):
            break
        listaLinea = linea.split(' ')
        arctxt.append(listaLinea)

    fo.truncate(0)
    fo.close()

    for i in range(len(arctxt)):
        for j in range(len(arctxt[0])):
            tablero[i][j] = int(arctxt[i][j])

def tableroaTXT(tablero):

    fo = open("battleship.txt", "a")

    for i in range(len(tablero)):
        dato = ""
        for j in range(len(tablero[0])):
            dato = dato + str(tablero[i][j]) + " "
        
        fo.write(dato)
        fo.write("\n")

    fo.close()

def main(): 
    numBarcos = 3

    # Se predefine el tablero como matrix 10x10
    tablero = [[0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0,0]]

    # Se comprueba si es el jugador 1 o 2
    comprobarControl()
    # Se genera el tablero
    crearTablero(tablero, numBarcos)

    # Se imprime el tablero generado
    for i in range(len(tablero)):
        print(tablero[i])

    # Se convierte la matrix a txt
    tableroaTXT(tablero)

main()