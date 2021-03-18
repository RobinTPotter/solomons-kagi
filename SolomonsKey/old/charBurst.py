from Action import *
from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Models import lists, MakeLists, colours
import random

class Burst:
    
    def __init__(self,life=3,size=0.5,intensity=18,diminish=True,x=0,y=0,z=0,burst_colours=["gold","red","white","red","yellow"],delay=0,callback=None):
        self.life=life
        self.x=x
        self.y=y
        self.z=z
        self.burst_colours=burst_colours
        self.size=size
        self.intensity=intensity
        self.diminish=diminish
        self.delay=delay
        self.callback=callback
        
    def draw(self):
        
        if self.delay>0:
            self.delay-=1
            return False
            
        glDisable(GL_LIGHTING)
        glPushMatrix()
        glTranslate(self.x,self.y,self.z)
        
        for i in range(self.intensity):
            glLineWidth(5.0)
            col = self.burst_colours[random.randint(0,-1+len(self.burst_colours))]
            glColor(colours[col])
            glBegin(GL_LINES)
            #print col            
            glVertex3f(0,0,0)
            glVertex3f(random.uniform(0,self.size*2)-self.size,random.uniform(0,self.size*2)-self.size,random.uniform(0,self.size*2)-self.size)
            glEnd()
            
        glPopMatrix()
        glEnable(GL_LIGHTING)
        self.life-=1
        if self.diminish: self.size-=0.1
        if self.life==0:
            if self.callback!=None: self.callback()
            return True
            
        return False
    
    def createBurst(self,burst_from=[0.0,0.0,0.0], burst_to=[1.0,0.0,0.0], control=None, steps=10, delay=15, callback=None):
        list_of_burst=[]
        if control==None:
            control = [(burst_from[0]+burst_to[0])/2, (burst_from[1]+burst_to[1])/2, (burst_from[2]+burst_to[2])/2]
        for s in range(0,steps+1):
            
            pfrxx=burst_from[0]+(float(s)/steps)*(control[0]-burst_from[0])
            pfryy=burst_from[1]+(float(s)/steps)*(control[1]-burst_from[1])
            pfrzz=burst_from[2]+(float(s)/steps)*(control[2]-burst_from[2])
            
            ptrxx=control[0]+(float(s)/steps)*(burst_to[0]-control[0])
            ptryy=control[1]+(float(s)/steps)*(burst_to[1]-control[1])
            ptrzz=control[2]+(float(s)/steps)*(burst_to[2]-control[2])
            
            pxx = pfrxx + (float(s)/steps)*(ptrxx-pfrxx)
            pyy = pfryy + (float(s)/steps)*(ptryy-pfryy)
            pzz = pfrzz + (float(s)/steps)*(ptrzz-pfrzz)
            
            cb=None
            if s==steps: cb=callback
            
            list_of_burst.append(Burst(x=pxx,y=pyy,z=pzz,delay=s*delay,callback=cb))
        
        return list_of_burst
            
        