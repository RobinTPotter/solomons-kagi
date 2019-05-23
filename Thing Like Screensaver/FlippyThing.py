"""
=================
Flippy Tile thing
=================

A near remake of the flip-flopping tile screen saver I found in Ubuntu.
Needing to develop Python skills, took it up myself to write this
using PyOpenGL. It uses dictionaries to capture the available holes and checks to see 
if there is a tile there already or a tile has the hole as a target.

There are various hard coded parameters as it amuses me to leave these there.

"""

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random 
import sys
from time import time
#import math

name = "thing"

colours={}
colours["red"]=[1.0,0.0,0.0,1.0]
colours["green"]=[0.0,1.0,0.0,1.0]
colours["blue"]=[0.0,0.0,1.0,1.0]
#colours["yellow"]=[1.0,1.0,0.0,1.0]
#colours["cyan"]=[0.0,1.0,1.0,1.0]
#colours["white"]=[1.0,1.0,1.0,1.0]

class Tile:
    
    x,y=None,None #current position
    hinge=None # side hinge is on currently
    state=0 #between 0 anf 1 for state of rotration 0 at rest always
    turning=0
    colour=None
    controller=None
    target=[0,0]
    speed=(random.randint(0,9)+1)/40.0
    
    def __init__(self,x,y,controller):
        self.x,self.y=x,y  
        #col=random.randint(0,len(colours)-1)
        col=x % len(colours)
        self.colour=colours.keys()[col]
        self.controller=controller
        
    def have_turn(self,target, hinge):
        self.target=target
        self.hinge=hinge
        self.state=0.0
        self.turning=1
        
    def draw(self):
    
       
        glPushMatrix()         
        glTranslate(self.x,self.y,0)   
        
        #print "drawing "+str(self.hinge)+" "+str(self.state)
        
        
        if self.turning==1:
            glRotate(90.0*self.hinge,0,0,1)
        
        
            #glTranslate(-self.state,0,0)
            glTranslate(-.5,0,0)
            glRotate(-180*self.state,0,1,0)
            glTranslate(.5,0,0)
            
            
                 
        glScale(0.95,0.95,0.2)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours[self.colour])
        glutSolidCube(1) 


        
        
                
        if self.turning==1:
        
            #glTranslate(-1,0,0)
            
            self.state+=self.speed
            
            if self.state>1.0:
                self.state=0
                self.turning=0
                #print "done "+str(self.hinge)                
             
                if self.hinge==0:
                    self.x-=1
                elif self.hinge==1:
                    self.y-=1
                elif self.hinge==2:
                    self.x+=1
                elif self.hinge==3:
                    self.y+=1
            
                self.controller.next()
                

        #glTranslate(1,0,0)                  
        glPopMatrix()
            
            
        
        
    

class Thing:

    tiles=[]
    
    lastFrameTime=0
    
    max_number_going=30
    
    xx,yy,zz=10,10,10
    X=0
    cxx,cyy,czz=2,-2,1

    def draw(self,FPS=1):
        
        #self.X+=1
	#if self.X % 100==0: self.X=0
	
	#s#elf.yy=7*math.sin(2*math.pi*self.X/100)
	#self.xx=7*math.cos(2*math.pi*self.X/100)
	
        currentTime=time()
        
        '''
        glPushMatrix()     
        glTranslate(0,0,0)
        glScale(1,1,1)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
        glutSolidCube(1)                   
        glPopMatrix()
        '''
        
        
        glPushMatrix()     
        for t in self.tiles: t.draw()
        glPopMatrix()
        
        
        glutPostRedisplay()
        
        
        
        #glutTimerFunc(int(1000/FPS), self.draw, FPS)

        #drawTime=currentTime-self.lastFrameTime
        #self.topFPS=int(1000/drawTime)
        #if int(100*time())%100==0: print "draw time "+str(drawTime)+" top FPS "+str(1000/drawTime)
        
        

    def isTileHere(self,xx,yy):
        for t in self.tiles:
            if t.x==xx and t.y==yy:
                return t
        
        return None
        

    def next(self):
    
        #random.shuffle(self.tiles)
    
        #print "next"
        
        holes={}
        
        for t in self.tiles:
            if t.turning==0:
                if self.isTileHere(t.x-1,t.y)==None: holes[(t.x-1,t.y)]=[t,0]
                if self.isTileHere(t.x+1,t.y)==None: holes[(t.x+1,t.y)]=[t,2]
                if self.isTileHere(t.x,t.y-1)==None: holes[(t.x,t.y-1)]=[t,1]
                if self.isTileHere(t.x,t.y+1)==None: holes[(t.x,t.y+1)]=[t,3]
                
            
        #print len(holes)
        for t in self.tiles:
            if holes.has_key((t.x,t.y)): del(holes[(t.x,t.y)])
            if holes.has_key((t.target[0],t.target[1])): del(holes[(t.target[0],t.target[1])])
    
    
        for k in holes.keys():
            if k[0]<0: del(holes[k])
            if k[1]<0: del(holes[k])
            if k[0]>22: del(holes[k])
            if k[1]>22: del(holes[k])
        
        #print len(holes)
        next_hole=random.randint(0,len(holes)-1)
        key=holes.keys()[next_hole]
        #print key
        #print holes
        holes[key][0].have_turn( key , holes[key][1])
                 
            


    def __init__(self):   
     
     
     
        for xx in range(0,20):
            for yy in range(0,20):
                if   (xx-10)*(xx-10)+(yy-10)*(yy-10) <80 and random.randint(0,30)>3:
                    self.tiles.append(Tile(xx,yy,self))
    
        if self.max_number_going>len(self.tiles): self.max_number_going=len(self.tiles)
            
        #print str(self.tiles)
        for n in range(1,self.max_number_going): self.next()
        
        
    
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
        
        '''
        glutSpecialFunc(self.keydownevent)
        glutSpecialUpFunc(self.keyupevent)
        glutKeyboardFunc(self.keydownevent)
        glutKeyboardUpFunc(self.keyupevent)
        '''
        
        glutDisplayFunc(self.display)
        #glutIdleFunc(self.display)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(110.0,640.0/480.,1.,50.)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glutMainLoop()
        
        return

    def display(self):

        glEnable (GL_BLEND)
        glEnable (GL_POLYGON_SMOOTH)
        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #print (self.xx,self.yy,self.zz)
        
        xx,yy,zz=0.0,0.0,0.0
        
        for t in self.tiles:
            xx+=t.x
            yy+=t.y
            
        yy/=len(self.tiles)
        xx/=len(self.tiles)
        
        self.cxx+=(xx-self.cxx)/20
        self.cyy+=(yy-self.cyy)/20
        self.czz+=(zz-self.czz)/20
        
    
        
        gluLookAt(self.xx,self.yy,self.zz,
                  self.cxx,self.cyy,self.czz,
                  0,1,0)
                  
        glRotatef(10,0,1,0)
        
                  
        glPushMatrix()     
        self.draw()
        glPopMatrix()
    
    
        glutSwapBuffers()
        #return


"""
Do this because if it gets put through pydoc or imported its automatically executed
"""
if __name__ == '__main__': Thing()
