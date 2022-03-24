from fnmatch import translate
from OpenGL.GL import *
from glew_wish import *
from math import *
from Character import *
from Barril import *
from Enemy import *
from Platano import *
from Escaleras import *
from Fondo import *

from pygame import mixer
import pygame
import glfw



pygame.mixer.init()

# mixer.music.load("LVL_Music.wav")
# mixer.music.play(-1)

window = None
player = Player()
barril_mov = Barril()
enemy = Enemy()
platano = Platano()
escaleras = Escaleras()
fondo = Fondo()
tiempo_anterior = 0.0

# escaleras = []

def colisionando():
    colisionando = False
    #Método de bounding box:
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extremo superior del triangulo >= Extremo inferior del cuadrado
    #Extremo inferior del triangulo <= Extremo superior del cuadrado
    return colisionando   

def actualizar():
    global window
    global tiempo_anterior

    tiempo_actual = glfw.get_time()
    tiempo_delta = tiempo_actual - tiempo_anterior



    if player.vivo:
        player.actualizar(window, tiempo_delta)
        if player.colisionando(platano):
            player.vivo = False
        if player.colisionando(barril_mov):
            player.vivo = False

        barril_mov.actualizar_barrel(tiempo_delta)
        platano.actualizar_platano(tiempo_delta)
    
    tiempo_anterior = tiempo_actual

# def escaleras_init():
#     for i in range(10):
#         escaleras.append(Escaleras(0.6, 0.6, 0, 0))

def draw():  
    fondo.draw_plataform_0_1()
    fondo.draw_plataform()
    fondo.draw_plataform_2()   
    fondo.draw_plataform_3()   
    fondo.draw_plataform_4()   
    fondo.draw_plataform_5()   
    fondo.draw_plataform_6()   
    fondo.draw_plataform_7()   
    escaleras.draw_escaleras()
    enemy.draw_cuadrado()
    barril_mov.draw_barrel()
    fondo.draw_cajas()
    fondo.draw_explosiva()
    fondo.draw_bote()
    fondo.draw_letrero()
    fondo.draw_barril()
    player.draw()
    fondo.draw_barriltwo()
    platano.draw_platano()

    # escaleras.draw_escaleras()

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

    # escaleras_init()

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