from msilib.schema import Class
from OpenGL.GL import *
from glew_wish import *
from math import *
from Modelo import *
import glfw

class Escaleras(Modelo):

    def __init__(self):
        super().__init__(0.0,0.0,0.0,0.5,0.0)
        # super().__init__(0.6,-0.6,0.0,0.5,0.0)
        self.extremo_izquierdo = 0.02
        self.extremo_derecho = 0.02
        self.extremo_inferior = 0.05
        self.extremo_superior = 0.05

    def draw_escaleras(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, 0.0)
        glBegin(GL_QUADS)

        glColor3f(3/255,252/255,244/255)
        glVertex3f(0.0,0.11,0.0)
        glVertex3f(0.1,0.11,0.0)
        glVertex3f(0.1,-0.1,0.0)
        glVertex3f(0.0,-0.1,0.0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(0.09,0.11,0.0)
        glVertex3f(0.01,0.11,0.0)
        glVertex3f(0.01,0.09,0.0)
        glVertex3f(0.09,0.09,0.0)
        glEnd() 

        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(0.09,0.08,0.0)
        glVertex3f(0.01,0.08,0.0)
        glVertex3f(0.01,0.06,0.0)
        glVertex3f(0.09,0.06,0.0)
        glEnd() 

        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(0.09,0.04,0.0)
        glVertex3f(0.01,0.04,0.0)
        glVertex3f(0.01,0.02,0.0)
        glVertex3f(0.09,0.02,0.0)
        glEnd() 

        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(0.09,0.0,0.0)
        glVertex3f(0.01,0.0,0.0)
        glVertex3f(0.01,-0.02,0.0)
        glVertex3f(0.09,-0.02,0.0)
        glEnd() 

        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(0.09,-0.04,0.0)
        glVertex3f(0.01,-0.04,0.0)
        glVertex3f(0.01,-0.06,0.0)
        glVertex3f(0.09,-0.06,0.0)
        glEnd() 

        glBegin(GL_QUADS)
        glColor3f(0,0,0)
        glVertex3f(0.09,-0.08,0.0)
        glVertex3f(0.01,-0.08,0.0)
        glVertex3f(0.01,-0.1,0.0)
        glVertex3f(0.09,-0.1,0.0)
        glEnd() 

        glPopMatrix()

    # def actualizar_escaleras(self, tiempo_delta):
