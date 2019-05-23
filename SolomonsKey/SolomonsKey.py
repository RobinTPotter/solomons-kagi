#!/bin/python

from OpenGL.GLUT import glutSwapBuffers, glutSolidCube, glutKeyboardFunc, glutKeyboardUpFunc, glutDisplayFunc, \
glutIdleFunc, glutInit, glutInitDisplayMode, glutCreateWindow, glutMainLoop, \
glutInitWindowSize, glutIgnoreKeyRepeat, glutSpecialFunc, glutReshapeFunc, glutSpecialUpFunc, glutTimerFunc, glutPostRedisplay, GLUT_DOUBLE, GLUT_RGBA, GLUT_DEPTH

from OpenGL.GLU import gluPerspective, gluLookAt

from OpenGL.GL import GL_PROJECTION,  GL_MODELVIEW, GL_DEPTH_TEST, GL_SMOOTH, \
GL_CULL_FACE, GL_LIGHTING, GL_POSITION, GL_LIGHT0, glLoadIdentity, \
glMatrixMode, glPushMatrix, glBlendFunc, glEnable, glClearColor, glShadeModel, glLightfv, \
GL_LINEAR_ATTENUATION, GL_CONSTANT_ATTENUATION, GL_DIFFUSE, \
glMaterialfv, glTranslate, glPopMatrix, glScale, GL_LIGHT1, GL_FRONT, glLightf, \
glViewport, GL_SRC_ALPHA, GL_ONE, GL_DEPTH_BUFFER_BIT, glClear, GL_COLOR_BUFFER_BIT

import sys
from time import time
from math import sin, cos, pi, floor, ceil, sqrt
import random
from Models import lists, MakeLists, colours
from Action import Action, ActionGroup
from Joystick import Joystick
from Sprite import Sprite
import Letters

from charSolomon import Solomon
from charBurst import Burst
from controller import generateLevel, Level

X=46.0

name = "solomon\'s key"


from config import *

def dump(thing):
    print (thing.__dict__)


class SolomonsKey:

    level=None
    keys={}
    cxx,cyy,czz=None,None,None
    tcxx,tcyy,tczz=0,0,0
    fxx,fyy,fzz=None,None,None
    tfxx,tfyy,tfzz=0,0,0

    lastFrameTime=0
    topFPS=0
    camera_sweep = 20
    joystick=Joystick()
    

    def animate(self,FPS=32):

        currentTime=time()

        #key movement for omnicontrol
        try:
            if self.keys["x"]: self.fxx+=1
            if self.keys["z"]: self.fxx-=1
            if self.keys["d"]: self.fyy+=1
            if self.keys["c"]: self.fyy-=1
            if self.keys["f"]: self.fzz+=1
            if self.keys["v"]: self.fzz-=1
        except:
            pass

        # run calculations for level inc collision etc
        if not self.level==None: self.level.evaluate(self.joystick,self.keys)

        glutPostRedisplay()

        glutTimerFunc(int(1000/FPS), self.animate, FPS)

        drawTime=currentTime-self.lastFrameTime

        self.topFPS=int(1000/drawTime)

        # set camera target focus points
        self.tfxx,self.tfyy,self.tfzz=self.level.solomon.x+0.2*self.level.solomon.facing,self.level.solomon.y-0.5,3.0

        # set camera target position
        self.tcxx,self.tcyy,self.tczz=self.level.solomon.x+1*self.level.solomon.facing,self.level.solomon.y-0.2,float(self.level.target_z)


        # inititalize current camera positions and focal targets
        if self.cxx==None: self.cxx=self.tcxx
        if self.cyy==None: self.cyy=self.tcyy
        if self.czz==None: self.czz=self.tczz
        # ....
        if self.fxx==None: self.fxx=self.tfxx
        if self.fyy==None: self.fyy=self.tfyy
        if self.fzz==None: self.fzz=self.tfzz

        # calculate current focal point and camera position
        # self.camera_sweep is the "speed" at which transitions are being made
        self.cxx+=(self.tcxx-self.cxx)/self.camera_sweep
        self.cyy+=(self.tcyy-self.cyy)/self.camera_sweep
        self.czz+=(self.tczz-self.czz)/self.camera_sweep
        # ...
        self.fxx+=(self.tfxx-self.fxx)/self.camera_sweep
        self.fyy+=(self.tfyy-self.fyy)/self.camera_sweep
        self.fzz+=(self.tfzz-self.fzz)/self.camera_sweep

        self.lastFrameTime=time()

    # if windowed ensure aspect ratio correct
    def reshape(self,width, height):
        r = float(width) / float(height)
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0,r,1.,50.)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #glPushMatrix()

    def __init__(self):

        print(str(bool(glutInit)))
        print("hello and weolcome")
        print("if you see an error next try the unofficial binaries of pyopengl")

        print("initializing glut etc")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(640,480)
        glutCreateWindow(name)

        print("set blend function")
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)

        print("set colours and lights")
        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)

        print ("set light 1")
        lightZeroPosition = [10.,4.,10.,1.]
        lightZeroColor = [0.9,1.0,0.9,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.2)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)

        print ("set light 2")
        lightZeroPosition2 = [-10.,-4.,10.,1.]
        lightZeroColor2 = [1.0,0.9,0.9,1.0] #green tinged
        glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition2)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor2)
        glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.2)
        glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT1)

        #initialization of letters
        print("initialzing letters")
        self.letters = Letters.Letters()

        #for game models
        print("making model lists")
        MakeLists()

        
        print("ignore key repeat")
        glutIgnoreKeyRepeat(1)

        print ("attach glut events to functions")
        glutSpecialFunc(self.keydownevent)
        glutSpecialUpFunc(self.keyupevent)
        glutReshapeFunc(self.reshape)

        glutKeyboardFunc(self.keydownevent)
        glutKeyboardUpFunc(self.keyupevent)
        glutDisplayFunc(self.display)
        #glutIdleFunc(self.display)

        print("initial projection")
        glMatrixMode(GL_PROJECTION)
        gluPerspective(60.0,640.0/480.,1.,50.)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()

        print("generating level")
        self.level=generateLevel(0)

        print("keys set up")
        self.initkey("zxdcfvqaopm")
        self.animate()

        print("about to loop...")
        glutMainLoop()

        return


    def initkey(self,cl):

        for c in cl:
            self.keydownevent(c.lower(),0,0)
            self.keyupevent(c.lower(),0,0)

    def display(self):

        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        gluLookAt(self.cxx,self.cyy,self.czz,
                  self.fxx,self.fyy,self.fzz,
                  0,1,0)

        self.level.draw()

        glLoadIdentity()

        gluLookAt(0, -0.5, 2.5,
                  0, 0, 0  ,
                  0, 1, 0  )

        wdth=0.3
        glTranslate(0.0-(len(self.level.solomon.current_state.keys())-1)*wdth/2.0,-1.3,0)

        if debug==True:
            for k in self.level.solomon.current_state.keys():
                col="red"
                if self.level.solomon.current_state[k]: col="green"
                glMaterialfv(GL_FRONT,GL_DIFFUSE,colours[col])
                glutSolidCube(wdth-0.02)
                glTranslate(wdth,0,0)
                glPushMatrix()
                #glLoadIdentity()
                glScale(0.006,0.01,-0.01)
                glTranslate(-70,4,-20)
                #glTranslate(-180,-70,0)
                glTranslate(wdth,0,0)
                self.letters.drawString(k[:3])
                glPopMatrix()

        glLoadIdentity()

        gluLookAt(0, -0.5, 2.5,
                  0, 0, 0  ,
                  0, 1, 0  )

        wdth=0.2

        joystick_actions=[x for x in dir(self.joystick) if x[0:2]=="is"]
        glTranslate(0.0-(len(joystick_actions)-1)*wdth/2.0,-1.0,0)

        if debug==True:
            for k in joystick_actions:
                #print(k)
                col="red"
                if getattr(self.joystick,k)(self.keys): col="green"
                glMaterialfv(GL_FRONT,GL_DIFFUSE,colours[col])
                glutSolidCube(wdth-0.02)
                glTranslate(wdth,0,0)

        glLoadIdentity()

        gluLookAt(0, 0, 2.5,
                  0, 0, 0  ,
                  0, 1, 0  )

        glScale(0.01,0.01,-0.01)
        glTranslate(-180,-70,0)

        if debug==True:
            self.letters.drawString(self.level.status1)
            glTranslate(0,0-15,0)
            self.letters.drawString(self.level.status2)
            glTranslate(0,0-15,0)
            self.letters.drawString(self.level.status3)

        glutSwapBuffers()

    def keydownevent(self,c,x,y):
        try:
            self.keys[c.lower()]=True
        except:
            pass

        glutPostRedisplay()

    def keyupevent(self,c,x,y):
        try:
            if self.keys.has_key(c.lower()): self.keys[c.lower()]=False
        except:
            pass

        glutPostRedisplay()

if __name__ == '__main__': SolomonsKey()