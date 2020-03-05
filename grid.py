from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

nX = 10.0
nY = 10.0

x0 = -1
y0 = -1

xf = 1
yf = 1

deltaX = (xf - x0) / nX   
deltaY = (yf - y0) / nY 

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )    

def f(x, y):
    return 1 / (x**2 + y**2)
    #return x**2 - y**2

def Grid():   
    i = 0
    y = y0
    while y <= yf:
        x = x0
        glBegin(GL_QUAD_STRIP)  
        while x <= xf:

            glColor3fv(cores[i%len(cores)])

            glVertex3f(x,y,f(x, y))
            glVertex3f(x,y + deltaY, f(x, y + deltaY))
            
            x +=  deltaX
            i = i+1
                    
        glEnd()
        y += deltaY    

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Grid()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL    
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("GRID")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()
