from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

name = 'ball_glut'
X=-2.0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)

    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    '''
    lightZeroPosition = [10.,4.0,10.0,1.0]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    glLightfv(GL_LIGHT0, GL_POSITION, 10.,2.0,15.0)  #*lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, *lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    '''
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    glutMainLoop()
    return

def display():

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,20,
              0,0,0,
              0,1,0)
    glPushMatrix() ## /* after setting up camera this resets the co-rds to origin */


    lightZeroPosition = [10.,0,5,1.0]
    lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
    global X
    glLightfv(GL_LIGHT0, GL_POSITION,X,0,-10)  #*lightZeroPosition)
    X+=0.05
    print X
    glLightfv(GL_LIGHT0, GL_DIFFUSE, 0.8,1.0,0.8)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    #glPushMatrix()
    color = [1.0,1.0,0.0,1.0]
    glMaterialfv(GL_FRONT,GL_DIFFUSE, 1.0,1.0,0.0) #* color)
    glutSolidSphere(2,20,20)
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
