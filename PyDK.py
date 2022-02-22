from fnmatch import translate
from OpenGL.GL import *
from glew_wish import *
import math
from math import *
import pygame

from pygame import mixer

import glfw

from collision_escaleras import *
from draw_stairs import *
from draw_plataforms import *

pygame.mixer.init()

# mixer.music.load("LVL_Music.wav")
# mixer.music.play(-1)
#proyecto parcial 1    
#unidades por segundo
window = None
velocidad = 0.5
tiempo_anterior = 0.0
velocidad_x = 0.5
velocidad_y = 0.5
JUMP = False
IS_JUMPING = False
IS_FALLING = False

posicion_y_triangulo_anterior = 0.0
posicion_cuadrado = [-0.4,0.9, 0.0]

posicion_barrel = [-0.4,0.85, 0.0]
direccion_barrelx = 1
direccion_barrely = 0
velocidad_barrel = 0.9

angulo_platano = 0.0
direccion_platano = 1
posicion_platano = [-0.9,0.85,0.0]
velocidad_platano = 0.5

def actualizar_platano(tiempo_delta):
    global direccion_platano
    global velocidad_platano
    global posicion_platano

    cantidad_movimiento = velocidad_platano * tiempo_delta

    if direccion_platano == 1:
        posicion_platano[0] = posicion_platano[0] + cantidad_movimiento
        posicion_platano[1] = posicion_platano[1] + (
            math.sin((angulo_platano + -90) * pi / 180.0) * cantidad_movimiento
        )
        if posicion_platano[0] >= 1:
            direccion_platano = 0

    if direccion_platano == 0:
        posicion_platano[0] = posicion_platano[0] - cantidad_movimiento
        posicion_platano[1] = posicion_platano[1] - (
            math.sin((angulo_platano - 90) * pi / 180.0) * cantidad_movimiento
        )
        if posicion_platano[0] <= -1:
            direccion_platano = 1

    # if posicion_platano[1] <= -0.6:
    #     posicion_platano[0] = posicion_platano[0] - cantidad_movimiento
    #     posicion_platano[1] = posicion_platano[1] - (
    #         math.sin((angulo_platano - 90) * pi / 180.0) * cantidad_movimiento
    #     )
def actualizar_barrel(tiempo_delta):
    global direccion_barrelx
    global direccion_barrely
    global velocidad_barrel
    global tiempo_anterior
    global posicion_barrel

    cantidad_movimiento = velocidad_barrel * tiempo_delta

    if direccion_barrelx == 0:
        posicion_barrel[0] = posicion_barrel[0] - cantidad_movimiento
    elif direccion_barrelx == 1:    
        posicion_barrel[0] = posicion_barrel[0] + cantidad_movimiento

    # elif direccion_barrely == 1: 
    #     posicion_barrel[1] = posicion_barrel[1] + cantidad_movimiento

    if posicion_barrel[0] <= -0.45 and direccion_barrelx == 0:
        direccion_barrelx = 1
        if direccion_barrely == 0:
            posicion_barrel[1] = posicion_barrel[1] - (cantidad_movimiento + 0.3)
        
    if posicion_barrel[0] >= 0.75 and direccion_barrelx == 1:
        direccion_barrelx = 0
        if direccion_barrely == 0:
            posicion_barrel[1] = posicion_barrel[1] - (cantidad_movimiento + 0.3)
    
    if posicion_barrel[1] <= -0.9:
        posicion_barrel = [-0.4,0.85, 0.0]
        velocidad_barrel = velocidad_barrel + 0.2
    
def actualizar():    
    global window
    global tiempo_anterior    
    global estado_tecla_arriba
    global cantidad_movimiento
    global estado_tecla_abajo
    global posicion_triangulo, posicion_barrel, posicion_cuadrado
    global velocidad_x, velocidad_y, posicion_y_triangulo_anterior
    global JUMP, IS_JUMPING, IS_FALLING 
    global angulo_platano, fase

    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecucion actual
    #y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    #Leer los estados de las teclas que queremos
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    estado_tecla_w = glfw.get_key(window, glfw.KEY_W)
    estado_tecla_s = glfw.get_key(window, glfw.KEY_S)
    estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_a = glfw.get_key(window, glfw.KEY_A)

    #Revisamos estados y realizamos acciones
    cantidad_movimiento = velocidad * tiempo_delta
    # if estado_tecla_arriba == glfw.PRESS:
    #     posicion_triangulo[1] = posicion_triangulo[1] + cantidad_movimiento
    if estado_tecla_derecha == glfw.PRESS:
        posicion_triangulo[0] = posicion_triangulo[0] + cantidad_movimiento
    # if estado_tecla_abajo == glfw.PRESS:
    #     posicion_triangulo[1] = posicion_triangulo[1] - cantidad_movimiento
    if estado_tecla_izquierda == glfw.PRESS:
        posicion_triangulo[0] = posicion_triangulo[0] - cantidad_movimiento

    actualizar_barrel(tiempo_delta)
    actualizar_platano(tiempo_delta)

    poder_salto = 1.5
    vel_y = velocidad_y * tiempo_delta * poder_salto
    gravedad = -0.3
    cantidad_de_salto = 0.1
    estado_tecla_space = glfw.get_key(window, glfw.KEY_SPACE)
    
    if JUMP is False and IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
        JUMP = True
        posicion_y_triangulo_anterior = posicion_triangulo[1]

    if JUMP is True:
        # Añade a la y la velocidad_y a la velocidad anteiror
        # Añade la velocidad del salto
        posicion_triangulo[1] += vel_y
        IS_JUMPING = True

    # Ver si ya se paso de burger
    if IS_JUMPING:
        if posicion_triangulo[1] - posicion_y_triangulo_anterior >= cantidad_de_salto:
            # print("Bruhc")
            JUMP = False
            vel_y = gravedad * tiempo_delta
            posicion_triangulo[1] += vel_y
            IS_FALLING = True

    if IS_FALLING: 
        vel_y = gravedad * tiempo_delta
        posicion_triangulo[1] += vel_y

        if posicion_triangulo[1] <= posicion_y_triangulo_anterior:
            IS_JUMPING = False
            JUMP = False
            IS_FALLING = False
            posicion_triangulo[1] = posicion_y_triangulo_anterior   

    tiempo_anterior = tiempo_actual

def colisionando():
    colisionando = False
    #Metodo de bounding box:
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #Extremo inferior del triangulo <= Extremo superior del cuadrado
    if (posicion_triangulo[0] + 0.05 >= posicion_barrel[0] - 0.01
    and posicion_triangulo[0] - 0.05 <= posicion_barrel[0] + 0.01 
    and posicion_triangulo[1] + 0.05 >= posicion_barrel[1] - 0.01
    and posicion_triangulo[1] - 0.05 <= posicion_barrel[1] + 0.01):
        colisionando = True
    if (posicion_triangulo[0] + 0.05 >= posicion_cuadrado[0] - 0.01
    and posicion_triangulo[0] - 0.05 <= posicion_cuadrado[0] + 0.01 
    and posicion_triangulo[1] + 0.05 >= posicion_cuadrado[1] - 0.01
    and posicion_triangulo[1] - 0.05 <= posicion_cuadrado[1] + 0.01):
        colisionando = True
    return colisionando

def draw_triangulo():
    glPushMatrix()
    glTranslatef(posicion_triangulo[0], posicion_triangulo[1],0.0)

    glBegin(GL_TRIANGLES)
    if colisionando():
        glColor3f(0,0,1)
        glfw.destroy_window(window)
    else:
        glColor3f(1,0,0.7)

    if colisionando_escaleras() and estado_tecla_arriba == glfw.PRESS :
        posicion_triangulo[1] = posicion_triangulo[1] + cantidad_movimiento

    if colisionando_escaleras() and estado_tecla_abajo == glfw.PRESS:
        posicion_triangulo[1] = posicion_triangulo[1] - cantidad_movimiento
 
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0.0,0.05,0)
    glVertex3f(0.05,-0.05,0)
    glEnd()

    # glBegin(GL_LINE_LOOP)

    # glColor(1,1,1)
    # glVertex3f(-0.05, -0.05, 0)
    # glVertex3f(-0.05, 0.05, 0)
    # glVertex3f(0.05, 0.05, 0)
    # glVertex3f(0.05, -0.05, 0)

    # glEdnwad()
    glPopMatrix()
    
def draw_cuadrado():
    glPushMatrix()
    glTranslatef(posicion_cuadrado[0], posicion_cuadrado[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(0.9, 0.2, 0.21)

    glVertex3f(-0.1,0.1,0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(-0.1,-0.1,0.0)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(1,1,1)

    glVertex3f(-0.1,0.1,0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(-0.1,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_barrel():
    sides = 32    
    radius = 0.04  
    glPushMatrix()
    glTranslatef(posicion_barrel[0], posicion_barrel[1], 0.0)
    glBegin(GL_POLYGON)
    glColor3f(150/255,62/255,0)    
    for i in range(100):    
        cosine= radius * cos(i*2*pi/sides)     
        sine  = radius * sin(i*2*pi/sides)   
        glVertex2f(cosine,sine)
    glEnd()
    glPopMatrix()      

def draw_cajas():
    glPushMatrix()
    glTranslatef(0,-0.6,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.0,0)
    glVertex3f(0.95,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(79/255,37/255,0)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.0,0)
    glVertex3f(0.94,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(79/255,37/255,0)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.0,0)
    glVertex3f(0.88,0.0,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(128/255,62/255,0)
    glVertex3f(0.86,-0.1,0.0)
    glVertex3f(0.94,0.0,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(128/255,62/255,0)
    glVertex3f(0.94,-0.1,0.0)
    glVertex3f(0.86,0.0,0.0)
    glEnd()
    glPopMatrix()  

    #2dacaja
    glPushMatrix()
    glTranslatef(0.04,-0.5,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.0,0)
    glVertex3f(0.95,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(79/255,37/255,0)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.0,0)
    glVertex3f(0.94,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(79/255,37/255,0)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.0,0)
    glVertex3f(0.88,0.0,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(128/255,62/255,0)
    glVertex3f(0.86,-0.1,0.0)
    glVertex3f(0.94,0.0,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(128/255,62/255,0)
    glVertex3f(0.94,-0.1,0.0)
    glVertex3f(0.86,0.0,0.0)
    glEnd()
    glPopMatrix()  

    glPushMatrix()
    glTranslatef(-1.5,0.9,0)
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.0,0)
    glVertex3f(0.95,0.0,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(222/255,222/255,222/255)
    glVertex3f(0.95,-0.03,0)
    glVertex3f(0.85,-0.03,0)
    glVertex3f(0.85,-0.05,0)
    glVertex3f(0.95,-0.05,0)
    glEnd()
    glPopMatrix()  

def draw_barril():
    glPushMatrix()
    glTranslatef(-1.5,0.3,0)

    glBegin(GL_QUADS)
    glColor3f(0,105/255,12/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.08,0)
    glVertex3f(0.95,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(49/255,214/255,69/255)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.08,0)
    glVertex3f(0.94,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(49/255,214/255,69/255)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.08,0)
    glVertex3f(0.88,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(49/255,214/255,69/255)
    glVertex3f(0.89,-0.1,0)
    glVertex3f(0.91,-0.1,0)
    glVertex3f(0.91,0.08,0)
    glVertex3f(0.89,0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(2/255,66/255,0)
    glVertex3f(0.95,-0.09,0.0)
    glVertex3f(0.85,-0.09,0.0)
    glVertex3f(0.95,-0.08,0.0)
    glVertex3f(0.85,-0.08,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(2/255,66/255,0)
    glVertex3f(0.95,0.04,0.0)
    glVertex3f(0.85,0.04,0.0)
    glVertex3f(0.95,0.05,0.0)
    glVertex3f(0.85,0.05,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(128/255,62/255,0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.9 , 0.01* math.sin(angulo * math.pi / 180) +0.08, 0)

    glEnd()
    glPopMatrix()  

def draw_barriltwo():
    glPushMatrix()
    glTranslatef(-1.65,-0.7,0)

    glBegin(GL_QUADS)
    glColor3f(230/255,158/255,2/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.08,0)
    glVertex3f(0.95,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(161/255,110/255,0)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.08,0)
    glVertex3f(0.94,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(161/255,110/255,0)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.08,0)
    glVertex3f(0.88,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(161/255,110/255,0)
    glVertex3f(0.89,-0.1,0)
    glVertex3f(0.91,-0.1,0)
    glVertex3f(0.91,0.08,0)
    glVertex3f(0.89,0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(54/255,0,161/255)
    glVertex3f(0.95,-0.09,0.0)
    glVertex3f(0.85,-0.09,0.0)
    glVertex3f(0.95,-0.08,0.0)
    glVertex3f(0.85,-0.08,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(54/255,0,161/255)
    glVertex3f(0.95,0.04,0.0)
    glVertex3f(0.85,0.04,0.0)
    glVertex3f(0.95,0.05,0.0)
    glVertex3f(0.85,0.05,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(128/255,62/255,0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.9 , 0.01* math.sin(angulo * math.pi / 180) +0.08, 0)

    glEnd()
    glPopMatrix()  

#tercer barril
    glPushMatrix()
    glTranslatef(-1.75,-0.7,0)

    glBegin(GL_QUADS)
    glColor3f(32/255,0,97/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.08,0)
    glVertex3f(0.95,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(118/255,101/255,153/255)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.08,0)
    glVertex3f(0.94,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(118/255,101/255,153/255)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.08,0)
    glVertex3f(0.88,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(118/255,101/255,153/255)
    glVertex3f(0.89,-0.1,0)
    glVertex3f(0.91,-0.1,0)
    glVertex3f(0.91,0.08,0)
    glVertex3f(0.89,0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(232/255,135/255,0)
    glVertex3f(0.95,-0.09,0.0)
    glVertex3f(0.85,-0.09,0.0)
    glVertex3f(0.95,-0.08,0.0)
    glVertex3f(0.85,-0.08,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(232/255,135/255,0)
    glVertex3f(0.95,0.04,0.0)
    glVertex3f(0.85,0.04,0.0)
    glVertex3f(0.95,0.05,0.0)
    glVertex3f(0.85,0.05,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(128/255,62/255,0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.9 , 0.01* math.sin(angulo * math.pi / 180) +0.08, 0)

    glEnd()
    glPopMatrix()  

    #dalkq 

    glPushMatrix()
    glTranslatef(-1.65,-0.51,0)

    glBegin(GL_QUADS)
    glColor3f(0,140/255,158/255)
    glVertex3f(0.95,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.08,0)
    glVertex3f(0.95,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(91/255,189/255,140/255)
    glVertex3f(0.94,-0.1,0)
    glVertex3f(0.92,-0.1,0)
    glVertex3f(0.92,0.08,0)
    glVertex3f(0.94,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(91/255,189/255,140/255)
    glVertex3f(0.88,-0.1,0)
    glVertex3f(0.86,-0.1,0)
    glVertex3f(0.86,0.08,0)
    glVertex3f(0.88,0.08,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(91/255,189/255,140/255)
    glVertex3f(0.89,-0.1,0)
    glVertex3f(0.91,-0.1,0)
    glVertex3f(0.91,0.08,0)
    glVertex3f(0.89,0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(191/255,0,0)
    glVertex3f(0.95,-0.09,0.0)
    glVertex3f(0.85,-0.09,0.0)
    glVertex3f(0.95,-0.08,0.0)
    glVertex3f(0.85,-0.08,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(191/255,0,0)
    glVertex3f(0.95,0.04,0.0)
    glVertex3f(0.85,0.04,0.0)
    glVertex3f(0.95,0.05,0.0)
    glVertex3f(0.85,0.05,0.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(128/255,62/255,0)
    for angulo in range(0, 359, 5):
        glVertex3f(0.05 * math.cos(angulo * math.pi / 180) + 0.9 , 0.01* math.sin(angulo * math.pi / 180) +0.08, 0)

    glEnd()
    glPopMatrix()  


def draw_bote():
    glBegin(GL_QUADS)
    glColor3f(19/255,0,191/255)
    glVertex3f(0.98,-0.1,0)
    glVertex3f(0.85,-0.1,0)
    glVertex3f(0.85,0.05,0)
    glVertex3f(0.98,0.05,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(168/255,158/255,0)
    glVertex3f(0.98,0.03,0.0)
    glVertex3f(0.85,0.03,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(168/255,158/255,0)
    glVertex3f(0.98,0.02,0.0)
    glVertex3f(0.85,0.02,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(168/255,158/255,0)
    glVertex3f(0.98,-0.08,0)
    glVertex3f(0.85,-0.08,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(168/255,158/255,0)
    glVertex3f(0.98,-0.07,0)
    glVertex3f(0.85,-0.07,0)
    glEnd()

def draw_letrero():
    
    glPushMatrix()
    glTranslatef(1.75,0.6,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(-0.84,-0.1,0)
    glVertex3f(-0.84,0.1,0)
    glVertex3f(-0.86,0.1,0)
    glVertex3f(-0.86,-0.1,0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(230/255,158/255,2/255)
    glVertex3f(-0.8,0.0,0)
    glVertex3f(-0.9,0.1,0)
    glVertex3f(-0.9,0.0,0)
    glVertex3f(-0.8,0.1,0)
    glEnd()

    glPopMatrix()  

    glPushMatrix()
    glTranslatef(1.8,0.7,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(-0.84,-0.2,0)
    glVertex3f(-0.84,0.1,0)
    glVertex3f(-0.86,0.1,0)
    glVertex3f(-0.86,-0.2,0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(173/255,0,173/255)
    glVertex3f(-0.8,0.0,0)
    glVertex3f(-0.9,0.1,0)
    glVertex3f(-0.9,0.0,0)
    glVertex3f(-0.8,0.1,0)
    glEnd()

    glPopMatrix()  

    glPushMatrix()
    glTranslatef(0,-0.42,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(-0.84,-0.2,0)
    glVertex3f(-0.84,0.1,0)
    glVertex3f(-0.86,0.1,0)
    glVertex3f(-0.86,-0.2,0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(0,219/255,37/255)
    glVertex3f(-0.8,0.0,0)
    glVertex3f(-0.9,0.1,0)
    glVertex3f(-0.9,0.0,0)
    glVertex3f(-0.8,0.1,0)
    glEnd()

    glPopMatrix()  
    
    glPushMatrix()
    glTranslatef(0.1,-0.32,0)
    glBegin(GL_QUADS)
    glColor3f(163/255,95/255,36/255)
    glVertex3f(-0.84,-0.1,0)
    glVertex3f(-0.84,0.1,0)
    glVertex3f(-0.86,0.1,0)
    glVertex3f(-0.86,-0.1,0)
    glEnd()
    
    glBegin(GL_QUADS)
    glColor3f(255/255,225/255,28/255)
    glVertex3f(-0.8,0.0,0)
    glVertex3f(-0.9,0.1,0)
    glVertex3f(-0.9,0.0,0)
    glVertex3f(-0.8,0.1,0)
    glEnd()

    glPopMatrix() 


def draw_explosiva():
    glBegin(GL_QUADS)
    glColor3f(156/255,156/255,156/255)
    glVertex3f(-0.65,-0.3,0)
    glVertex3f(-0.55,-0.3,0)
    glVertex3f(-0.55,-0.4,0)
    glVertex3f(-0.65,-0.4,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(156/255,156/255,156/255)
    glVertex3f(-0.59,-0.25,0)
    glVertex3f(-0.61,-0.25,0)
    glVertex3f(-0.61,-0.4,0)
    glVertex3f(-0.59,-0.4,0)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(138/255,138/255,138/255)
    glVertex3f(-0.65,-0.23,0)
    glVertex3f(-0.55,-0.23,0)
    glVertex3f(-0.55,-0.25,0)
    glVertex3f(-0.65,-0.25,0)
    glEnd()

def draw_platano():
    glPushMatrix()
    glScale(0.8,0.8,0)
    glTranslatef(posicion_platano[0], posicion_platano[1], 0.0)

    glBegin(GL_POLYGON)
    glColor3f(0.9, 1.0, 0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.08,0.1,0.0)
    glVertex3f(0.06,0.05,0.0)
    glVertex3f(0.06,0.0,0.0)
    glVertex3f(0.07,-0.05,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0.12,-0.1,0.0)

    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.3,0.3,0.3)
    glVertex3f(0.08,0.1,0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,0.12,0.0)
    glVertex3f(0.08,0.12,0.0)

    glEnd()

    glPopMatrix()

def draw():  
    draw_plataform_0_1()
    draw_escaleras()
    draw_escaleras_2()
    draw_escaleras_3()
    draw_escaleras_4()
    draw_escaleras_5()
    draw_plataform()
    draw_plataform_2()   
    draw_plataform_3()   
    draw_plataform_4()   
    draw_plataform_5()   
    draw_plataform_6()   
    draw_plataform_7()   
    draw_cuadrado()
    draw_barrel()
    draw_cajas()
    draw_explosiva()
    draw_bote()
    draw_letrero()
    draw_barril()
    draw_triangulo()
    draw_platano()

def main():
    global window
    global tiempo_anterior
    width = 900
    height = 900
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        glViewport(0,0,800,800)
        #Establecer color de borrado
        glClearColor(0,0,0,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        actualizar()
        #Dibujar
        draw()
        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()