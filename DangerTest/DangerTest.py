from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random 
import sys
from time import time
#import math

name = "thing"

colours={}

colours["gold"]=[1.0,0.9,0.0,1.0]
colours["red"]=[1.0,0.0,0.0,1.0]
colours["green"]=[0.0,1.0,0.0,1.0]
colours["blue"]=[0.0,0.0,1.0,1.0]
colours["yellow"]=[1.0,1.0,0.0,1.0]
colours["cyan"]=[0.0,1.0,1.0,1.0]
colours["pink"]=[1.0,0.0,1.0,1.0]
colours["white"]=[1.0,1.0,1.0,1.0]
  
  
  
  
lists={}

def MakeLists():

    global lists

    lists[" "] = glGenLists(1) 
    glNewList(lists[" "],GL_COMPILE) 
    glEndList()

    lists["A"] = glGenLists(1) 
    glNewList(lists["A"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()


    lists["B"] = glGenLists(1) 
    glNewList(lists["B"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["C"] = glGenLists(1) 
    glNewList(lists["C"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()


    lists["D"] = glGenLists(1) 
    glNewList(lists["D"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(10.0, 8.0)
    glVertex2f(10.0, 2.0)
    glVertex2f(8.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["E"] = glGenLists(1) 
    glNewList(lists["E"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()


    lists["F"] = glGenLists(1) 
    glNewList(lists["F"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()


    lists["G"] = glGenLists(1) 
    glNewList(lists["G"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(8.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(8.0, 10.0) 
    glEnd()
    glEndList()


    lists["H"] = glGenLists(1) 
    glNewList(lists["H"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()


    lists["I"] = glGenLists(1) 
    glNewList(lists["I"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()


    lists["J"] = glGenLists(1) 
    glNewList(lists["J"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 2.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(3.0, 0.0)
    glVertex2f(5.0, 2.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()


    lists["K"] = glGenLists(1) 
    glNewList(lists["K"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["L"] = glGenLists(1) 
    glNewList(lists["L"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["M"] = glGenLists(1) 
    glNewList(lists["M"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["N"] = glGenLists(1) 
    glNewList(lists["N"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["O"] = glGenLists(1) 
    glNewList(lists["O"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["P"] = glGenLists(1) 
    glNewList(lists["P"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["Q"] = glGenLists(1) 
    glNewList(lists["Q"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["R"] = glGenLists(1) 
    glNewList(lists["R"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["S"] = glGenLists(1) 
    glNewList(lists["S"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["T"] = glGenLists(1) 
    glNewList(lists["T"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(5.0, 0.0) 
    glEnd()
    glEndList()



    lists["U"] = glGenLists(1) 
    glNewList(lists["U"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()



    lists["V"] = glGenLists(1) 
    glNewList(lists["V"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()



    lists["W"] = glGenLists(1) 
    glNewList(lists["W"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["X"] = glGenLists(1) 
    glNewList(lists["X"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()



    lists["Y"] = glGenLists(1) 
    glNewList(lists["Y"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(5.0, 0.0) 
    glEnd()
    glEndList()



    lists["Z"] = glGenLists(1) 
    glNewList(lists["Z"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["0"] = glGenLists(1) 
    glNewList(lists["0"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["1"] = glGenLists(1) 
    glNewList(lists["1"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["2"] = glGenLists(1) 
    glNewList(lists["2"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(7.0, 5.0)
    glVertex2f(10.0, 8.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(2.0, 10.0)
    glVertex2f(0.0, 8.0) 
    glEnd()
    glEndList()



    lists["3"] = glGenLists(1) 
    glNewList(lists["3"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(3.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(10.0, 3.0)
    glVertex2f(10.0, 2.0)
    glVertex2f(8.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0) 
    glEnd()
    glEndList()



    lists["4"] = glGenLists(1) 
    glNewList(lists["4"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(8.0, 0.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(10.0, 2.0) 
    glEnd()
    glEndList()



    lists["5"] = glGenLists(1) 
    glNewList(lists["5"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(10.0, 2.0)
    glVertex2f(8.0, 0.0)
    glVertex2f(2.0, 0.0)
    glVertex2f(0.0, 2.0) 
    glEnd()
    glEndList()



    lists["6"] = glGenLists(1) 
    glNewList(lists["6"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["7"] = glGenLists(1) 
    glNewList(lists["7"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(2.0, 0.0) 
    glEnd()
    glEndList()



    lists["8"] = glGenLists(1) 
    glNewList(lists["8"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["9"] = glGenLists(1) 
    glNewList(lists["9"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0) 
    glEnd()
    glEndList()
  
  
  
  
  
  
class Thing:

    lastFrameTime=0
    
    xx,yy,zz=0,0,40
    cxx,cyy,czz=0,0,0
    X=0
    
    xRot=0
    yRot=0
    mPos=[0,0]
    speed=0.1

    def animate(self,FPS=1):
        
        currentTime=time()         
        
        
        self.X+=1
        if self.X>1000: self.X=0
               
        #print "posting redisplay"
        glutPostRedisplay()    
        
        tt=int(1000/FPS)
        #print tt, FPS
        glutTimerFunc(tt, self.animate, FPS)
        drawTime=currentTime-self.lastFrameTime
        self.topFPS=int(1000/drawTime)
        if int(100*time())%100==0: print "draw time "+str(drawTime)+" top FPS "+str(1000/drawTime)
        
    def draw(self):
                
        glTranslate(0,0,8)
        glRotate(-self.yRot*2,1,0,0)
        glRotate(-self.xRot*2,0,1,0)
                                
        global lists
        string="ROBIN POTTER"
        glScale(0.1,0.1,0.1)
        for l in range(0,len(string)):
            glTranslate(10.1,0,0)
            glCallList(lists[string[l]])
        
        f=open("DangerCode.txt","r")
        code=f.read()
        #print "DC:"+code
        exec(code)

    def __init__(self):   
     
             
    
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(640,480)
        glutCreateWindow(name)

        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_FLAT)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        lightZeroPosition = [10.,4.,10.,1.]
        lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)
        glutMotionFunc(self.mousedrag)
        glutMouseFunc(self.mouse)
        '''
        glutSpecialFunc(self.keydownevent)
        glutSpecialUpFunc(self.keyupevent)
        glutKeyboardFunc(self.keydownevent)
        glutKeyboardUpFunc(self.keyupevent)
        '''
        
        glutDisplayFunc(self.display)
        #glutIdleFunc(self.display)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(60.0,640.0/480.,1.,50.)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        
        self.animate(FPS=5)
        
        MakeLists()
        glutMainLoop()
        
        
        return

    def mousedrag(self,x,y):
        #print ((x,y))
        self.xRot+=(self.mPos[0]-x)*self.speed
        self.yRot+=(self.mPos[1]-y)*self.speed
        self.mPos=[x,y]

    def mouse(self,button,state,x,y):
        #print ((button,state,x,y))
        self.mPos=[x,y]

    def display(self):

        glEnable (GL_BLEND)
        glEnable (GL_POLYGON_SMOOTH)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #print (self.xx,self.yy,self.zz)                 
        
        gluLookAt(self.xx,self.yy,self.zz,
                  self.cxx,self.cyy,self.czz,
                  0,1,0)          
        
        self.draw()
        self.yRot+=0.5
        self.xRot+=0.5
    
    
        glutSwapBuffers()
        #return


"""
Do this because if it gets put through pydoc or imported its automatically executed
"""
if __name__ == '__main__': Thing()
