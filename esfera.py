from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

def Pontos():
    glBegin(GL_POINTS)
    glColor3f(1,1,1)
    for ponto in pontos:        
        glVertex3fv(ponto)
    glEnd()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    Pontos()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
pontos = []
 
nEsfera = 50
nRotacao = 50 
r = 2

pontos += [[0,1,0]]

for i in range(0,nEsfera):

    teta = ((i*math.pi)/nEsfera) - (math.pi/2)

    for j in range(0, nRotacao):

        phi = j*2*math.pi/nRotacao

        x = r*math.cos(teta)*math.cos(phi)
        y = r*math.sin(teta)
        z = r*math.cos(teta)*math.sin(phi)
   
        pontos += [[x,y,z]]
    
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()