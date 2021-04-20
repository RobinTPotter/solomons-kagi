#!/bin/python3

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import sys
from time import time
from math import sin, cos, pi, floor, ceil, sqrt
import random
from Models import lists, MakeLists, colours
from Action import Action, ActionGroup
from Joystick import Joystick
import Letters
import Level
from Solomon import Solomon
from Burst import Burst
from Logic import gogogo

import Logic

import threading

name = "solomon\'s key"

class XYZ:
    def __init__(self, x=None, y=None, z=None):
        self.x = x
        self.y = y
        self.z = z

    def sub(self, xyz):
        x = self.x - xyz.x
        y = self.y - xyz.y
        z = self.z - xyz.z
        return XYZ(x,y,z)
        
    def add(self, xyz):
        x = self.x + xyz.x
        y = self.y + xyz.y
        z = self.z + xyz.z
        return XYZ(x,y,z)

    def mult(self, sc):
        x = self.x * sc
        y = self.y * sc
        z = self.z * sc
        return XYZ(x,y,z)

class SolomonsKey(threading.Thread):

    thing = 0
    level=None
    keys={}
    cam_pos = XYZ(0,0,0)
    cam_pos_target= XYZ(0,0,0)
    cam_focus = XYZ(0,0,0)
    cam_focus_target = XYZ(0,0,0)
    key_light = XYZ(0,0,0)
    lastFrameTime=0
    topFPS=0
    camera_sweep = 20
    joystick=Joystick()
    
    def animate(self,FPS=30):

        currentTime=time()

        #key movement for omnicontrol
        try:
            if self.keys[b"x"]: self.cam_focus.x+=1
            if self.keys[b"z"]: self.cam_focus.x-=1
            if self.keys[b"d"]: self.cam_focus.y+=1
            if self.keys[b"c"]: self.cam_focus.y-=1
            if self.keys[b"f"]: self.cam_focus.z+=1
            if self.keys[b"v"]: self.cam_focus.z-=1
        except:
            pass

        # run calculations for level inc collision etc
        #if not self.level==None: self.level.evaluate(self.joystick,self.keys)

        glutPostRedisplay()

        glutTimerFunc(int(1000/FPS), self.animate, FPS)

        drawTime=currentTime-self.lastFrameTime

        self.topFPS = int(1000/drawTime)

        # set camera target focus points
        self.cam_focus_target = XYZ(self.solomon.solx+0.2*self.solomon.sol_dir,self.solomon.soly-0.5,3.5)

        # set camera target position
        self.cam_pos_target = XYZ(self.solomon.solx, self.solomon.soly, float(self.level.target_z)) #XYZ(self.solomon.solx+1*self.solomon.sol_dir, self.solomon.soly-0.2,float(self.level.target_z))

        # calculate current focal point and camera position
        # self.camera_sweep is the "speed" at which transitions are being made
        self.cam_pos = self.cam_pos.add( self.cam_pos_target.sub(self.cam_pos).mult(1/self.camera_sweep) )
        self.cam_focus = self.cam_focus.add( self.cam_focus_target.sub(self.cam_focus).mult(1/self.camera_sweep) )
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
        super().__init__()

    def run(self):
    
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
        glEnable(GL_NORMALIZE)

        print ("set light 1")
        lightZeroPosition = [0,0,00,1]
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        lightZeroColor = [0.2,0.2,0.2,0.5] #green tinged
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.025)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.0025)
        
        #print ("set light 2")
        #lightZeroPosition2 = [0,1,0]
        #glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition2)
        #lightZeroColor2 = [1,1,1,1.0] #green tinged
        #glEnable(GL_LIGHT1)
        #glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor2)
        #glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.2)
        #glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)
        
        #print ("set light 3")
        ##self.key_light.z=5
        #self.key_light = XYZ(10,0,15)
        #glLightfv(GL_LIGHT2, GL_POSITION, [self.key_light.x,self.key_light.y,self.key_light.z,0.01])
        #glEnable(GL_LIGHT2)
        #glLightfv(GL_LIGHT2, GL_DIFFUSE, [0.8,0.8,0.8,1.0])
        #glLightfv(GL_LIGHT2, GL_AMBIENT, [0.5,0.5,0.5,1.0])
        #glLightfv(GL_LIGHT2, GL_SPECULAR, [1.0,1.0,1.0,1.0])
        #glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.01)
        #glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.01)
        #
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
        self.level=Level.generateLevel(0)
        self.solomon=Solomon(self.level.solomon_start)


        print("keys set up")
        self.initkey("zxdcfvqaopm")
        self.animate()

        print("about to loop...")       
        glutMainLoop()

        return


    def initkey(self,cl):
        for c in cl:
            self.keydownevent(str(c.lower()).encode(),0,0)
            self.keyupevent(str(c.lower()).encode(),0,0)
        print("end initkey")

    def display(self):

        glLoadIdentity()
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        gluLookAt(self.cam_pos.x,self.cam_pos.y,self.cam_pos.z,
                  self.cam_focus.x, self.cam_focus.y, self.cam_focus.z,
                  0,1,0)

        glScale(0.9,0.9,0.9)

        if False:
            
            xx=(self.thing%100)/100
            print ("set light 2 {}".format(xx))
            #glDisable(GL_LIGHT1)
            lightZeroPosition2 = [0,-1,0]
            glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition2)
            lightZeroColor2 = [1,1,1,1.0] #green tinged
            #glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, xx*xx)
            #glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, xx*xx)
            glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor2)
            #glEnable(GL_LIGHT1)
            
        if False:
            if self.thing%100>50:
                glEnable(GL_LIGHT1)
                pass
            else:
                glDisable(GL_LIGHT1)
            
            
            if self.thing%50>25:
                glEnable(GL_LIGHT0)
                pass
            else:
                glDisable(GL_LIGHT0)
            


        self.level.draw()  
        for b in self.level.bursts:
            print("doing burst {}".format(b))
            if b.draw():
                print("burst complete {}".format(b))
                self.level.bursts.remove(b)
        
        
        gogogo(self.level, self.solomon, self.keys)
        #glLightfv(GL_LIGHT2, GL_POSITION, [self.solomon.solx,self.solomon.soly,10,0.01])
        #glLightfv(GL_LIGHT2, GL_POSITION, [0,0,0.7,0.01])
      
        
        
        self.solomon.draw()      
        if self.solomon.sol_walking==1: self.solomon.AG_walk.do()  

        self.thing +=1
        ###glDisable(GL_LIGHT0)

        #if debug==True:
        if False:
            glLoadIdentity()
            gluLookAt(0, -0.5, 2.5,
                      0, 0, 0  ,
                      0, 1, 0  )
            wdth=0.2
            joystick_actions=[x for x in dir(self.joystick) if x[0:2]=="is"]
            glTranslate(0.0-(len(joystick_actions)-1)*2*wdth/2.0,-1.0,0)
            for k in joystick_actions:
                #print(k)
                col="red"
                if getattr(self.joystick,k)(self.keys): col="green"
                glMaterialfv(GL_FRONT,GL_DIFFUSE,colours[col])
                glutSolidCube(2*wdth-0.02)
                glTranslate(2*wdth,0,0)
                glPushMatrix()
                #glLoadIdentity()
                glScale(0.007,0.01,-0.01)
                glTranslate(-75,0,-20)
                #glTranslate(-180,-70,0)
                glTranslate(-2*wdth,0,0)
                self.letters.drawString(k[2:5])
                glPopMatrix()

        ##glLoadIdentity()
        ##
        ##gluLookAt(0, 0, 2.5,
        ##          0, 0, 0  ,
        ##          0, 1, 0  )
        ##
        ##glScale(0.01,0.01,-0.01)
        ##glTranslate(-180,-70,0)

        #if debug==True:
        ##if True:
        ##    self.letters.drawString('X:'+str(self.solomon.solx)+' Y:'+str(self.solomon.soly))
        ##    glTranslate(0,0-15,0)
        ##    gx,gy=int(self.solomon.solx),int(self.solomon.soly)            
        ##    self.letters.drawString('G {0} on: {1} below: {2}'.format(str((gx,gy)),self.level.grid[gy][gx],self.level.grid[gy-1][gx]))
        ##    glTranslate(0,0-15,0)
        ##    self.letters.drawString('')

        glutSwapBuffers()

    def keydownevent(self,c,x,y):
        #print ("*******************************************************************************")
        try:
            self.keys[c]=True
            if self.joystick.callback_down is not None: self.joystick.callback_down(c)
            #print(self.keys)
            if self.joystick.isFire(self.keys):
                Logic.event(self.keys,c,self.solomon)
        except Exception as e:
            print(e)    
            pass

        glutPostRedisplay()

    def keyupevent(self,c,x,y):
        try:
            if c in self.keys: self.keys[c]=False
            if self.joystick.callback_up is not None: self.joystick.callback_up(c)
            #print(self.keys)
        except Exception as e:
            print(e)    
            pass

        glutPostRedisplay()






if __name__ == '__main__':
    s = SolomonsKey()
    s.start()
