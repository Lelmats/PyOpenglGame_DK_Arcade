from OpenGL.GL import *
from glew_wish import *

posicion_escaleras = [0.7,-0.7,0.0]
posicion_escaleras_2 = [-0.5,-0.4,0.0]
posicion_escaleras_3 = [0.7,-0.1,0.0]
posicion_escaleras_4 = [-0.5,0.2,0.0]
posicion_escaleras_5 = [0.7,0.6,0.0]


def draw_escaleras():
    glPushMatrix()
    glTranslatef(posicion_escaleras[0], posicion_escaleras[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(3/255,252/255,244/255)

    glVertex3f(0,0.2,0.0)
    glVertex3f(0.1,0.2,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_escaleras_2():
    glPushMatrix()
    glTranslatef(posicion_escaleras_2[0], posicion_escaleras_2[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(3/255,252/255,244/255)

    glVertex3f(0,0.2,0.0)
    glVertex3f(0.1,0.2,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_escaleras_3():
    glPushMatrix()
    glTranslatef(posicion_escaleras_3[0], posicion_escaleras_3[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(3/255,252/255,244/255)

    glVertex3f(0,0.2,0.0)
    glVertex3f(0.1,0.2,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0,-0.1,0.0)

    glEnd()
    glPopMatrix()

def draw_escaleras_4():
    glPushMatrix()
    glTranslatef(posicion_escaleras_4[0], posicion_escaleras_4[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(3/255,252/255,244/255)

    glVertex3f(0,0.2,0.0)
    glVertex3f(0.1,0.2,0.0)
    glVertex3f(0.1,-0.1,0.0)
    glVertex3f(0,-0.1,0.0)
    glEnd()
    glPopMatrix()

    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  

    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  

    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  

    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
    
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
    
    glBegin(GL_QUADS)
    glColor3f(1,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
   
    

def draw_escaleras_5():
    glPushMatrix()
    glTranslatef(posicion_escaleras_5[0], posicion_escaleras_5[1], 0.0)
    glBegin(GL_QUADS)

    glColor3f(3/255,252/255,244/255)

    glVertex3f(0,0.1,0.0)
    glVertex3f(0.1,0.1,0.0)
    glVertex3f(0.1,-0.2,0.0)
    glVertex3f(0,-0.2,0.0)

    glEnd()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0.71,0.03,0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(0.71,0,0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.71,-0.04,0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.71,-0.08,0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.71,-0.12,0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0.71,-0.16,0)
    glBegin(GL_QUADS)
    glColor3f(0,0,0)
    glVertex3f(0,0.08,0.0)
    glVertex3f(0.08,0.08,0.0)
    glVertex3f(0.08,0.06,0.0)
    glVertex3f(0,0.06,0.0)
    glEnd()  
    glPopMatrix()

