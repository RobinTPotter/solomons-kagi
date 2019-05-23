#!/bin/python

from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from time import time
from math import sin, cos, pi, floor, ceil, sqrt
import random
from Models import lists, MakeLists, colours


import array, struct



X=46.0

name = "testing"

'''

#stolen code for reading/writing binary files

import struct

f = open('file.bin', 'wb')
value = 1.23456
data = struct.pack('f',value)
f.write(data)
f.close()

f = open('file.bin', 'rb')
print struct.unpack('f',f.read(4))
f.close()
'''



'''

##intereswting stuff on file sizes 


$ ls -la chardet-1.0.1.tgz
-rwxr-xr-x 1 vinko vinko 179218 2008-10-20 17:49 chardet-1.0.1.tgz
$ python
Python 2.5.1 (r251:54863, Jul 31 2008, 22:53:39)
[GCC 4.1.2 (Ubuntu 4.1.2-0ubuntu4)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> f = open('chardet-1.0.1.tgz','rb')
>>> f.seek(0,2)
>>> f.tell()
179218L
Adding ChrisJY's idea to the example

>>> import os
>>> os.fstat(f.fileno()).st_size
179218L
>>>      

'''


'''
>>> fp=open("sdjfvsdjf.dat","r")
>>> del(z)
>>> z
>>> z.fromfile(fp,10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'z' is not defined
>>> z=array.array("c")
>>> fp.seek(0)
>>> z.fromfile(fp,10)
>>> z
array('c', 'Neil said ')
>>> fp.seek(0)
>>> z.fromfile(fp,10)
>>> z
array('c', 'Neil said Neil said ')
>>> fp.seek(0)
>>> z.fromfile(fp,10)
>>> z
array('c', 'Neil said Neil said Neil said ')
>>> z.fromfile(fp,20)
>>> z
array('c', 'Neil said Neil said Neil said to use a SUSE machin')
>>> fp.size()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>


'''

class Sprite:

    collision_action=None
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.draw_func=self.temp_drawfunc        
    
        self.AG_move=ActionGroup()
        
        self.AG_move.append("x_action",Action(func=self.x_action,max=100,cycle=True,min=0))
        self.AG_move.append("y_action",Action(func=self.y_action,max=100,cycle=True,min=0)) 
        self.AG_move.append("z_action",Action(func=self.z_action,max=100,cycle=True,min=0)) 

        self.AG_move.append("xrot_action",Action(func=self.xrot_action,max=360,cycle=True,min=0))
        self.AG_move.append("yrot_action",Action(func=self.yrot_action,max=360,cycle=True,min=0)) 
        self.AG_move.append("zrot_action",Action(func=self.zrot_action,max=360,cycle=True,min=0))        

    def setDrawFuncToList(self,listid): 
        self.listnumber=listid
        self.draw_func=self.drawList

    def drawList(self):
        glCallList(self.listnumber)  
        
    def runDetection(self,level):
        level.detect(self.x,self.y,collision_bound=2.0,callback=self.collision_action,ignoreDots=True,ignoreTheseSprites=[self])   

    def draw(self):    
    
        #glPushMatrix()
        #print str((self.x,self.y))
        glTranslate(self.x,self.y,0)
        glTranslate(float(self.AG_move.value("x_action")),float(self.AG_move.value("y_action")),float(self.AG_move.value("z_action")))
        glRotate(float(self.AG_move.value("xrot_action")),1,0,0)
        glRotate(float(self.AG_move.value("yrot_action")),0,1,0)
        glRotate(float(self.AG_move.value("zrot_action")),0,0,1)   
        #glRotate(15,1,0,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
        #glutWireCube(1)
        self.draw_func()
        #glPopMatrix()
        
    def temp_drawfunc(self):    
        glutSolidCube(0.8)
        
        
    def do(self):
        self.AG_move.do()
        
    def x_action(self,tvmm):
        return 0
        
    def y_action(self,tvmm):
        return 0
        
    def z_action(self,tvmm):
        return 0
               
    def xrot_action(self,tvmm):
        return 0
        
    def yrot_action(self,tvmm):
        return 0
        
    def zrot_action(self,tvmm):
        t,v,min,max=tvmm
        v=t*2
        return v
               
        
        


class Action:
    
    tick=0
    min=-5
    max=5
    value=0
    cycle=False 
    reverseloop=False
    dir=1    
    func=None
    init_tick=0
    working=True
    overide=False
    speed=1.0
    callback=None
    
    #defined function must return the value for storage
    def __init__(self,func=func,min=-5,max=5,cycle=False,reverseloop=False,init_tick=0):
        self.func=func
        self.min=min           
        self.max=max
        self.cycle=cycle 
        self.reverseloop=reverseloop
        self.init_tick=init_tick
        self.kick()
    
    def kick(self):    
        self.dir=1      
        self.tick=self.init_tick
        self.working=True

    def do(self):
        
        #print str(("action",self.tick,self.value))
        
        if not self.working: return
        self.tick+=self.dir*self.speed
        
        self.value=self.func((self.tick,self.value,self.min,self.max))  
                
        if self.cycle==True and self.reverseloop==False:
            if self.tick>=self.max: self.tick=self.min
            
        elif self.cycle==True and self.reverseloop==True:
            if self.tick>=self.max or self.tick<=self.min:
                self.dir*=-1
                     
        elif self.cycle==False:
            if self.tick>=self.max:
                self.working=False
                self.overide=False
                if not self.callback==None: self.callback()
                     
        if not self.value==None: return self.value
        else: return 0.0
        
#defines a set of actions to be done as one.
class ActionGroup:

    actions={}

    def __init__(self):
        self.actions={}
        
    def append(self,action_name,action):
        if self.actions.has_key(action_name):
            raise Error("action defined "+action_name)
        else:
            self.actions[action_name]=action
            
        
    def kick(self):
        for a in self.actions.keys():
            self.actions[a].kick()
            
    def speed_scale(self,scale):
        for a in self.actions.keys():
            self.actions[a].speed*=scale
            
    def do(self):
        for a in self.actions.keys():
            self.actions[a].do()
            #print "do action "+str(a)+" "+str((self.actions[a].tick,self.actions[a].value))
            
    def value(self,action_name):
        if self.actions.has_key(action_name):
            #print "action "+str(action_name)+" "+str(self.actions[action_name].value)
            return self.actions[action_name].value
        else:
            raise Error("no such action registered "+action_name)
            
    def action(self,action_name):
        if self.actions.has_key(action_name):
            return self.actions[action_name]
        else:
            raise Error("no such action registered "+action_name)
            


class Joystick:
    
    up,down,left,right,fire="","","","",""

    def __init__(self,up="q",down="a",left="o",right="p",fire="m"):
        self.up=up
        self.down=down
        self.left=left
        self.right=right
        self.fire=fire
        
    def isUp(self,keys):
        if keys.has_key(self.up): return keys[self.up]
        else: return False
         
    def isDown(self,keys):
        if keys.has_key(self.down): return keys[self.down]
        else: return False
         
    def isLeft(self,keys):
        if keys.has_key(self.left): return keys[self.left]
        else: return False
         
    def isRight(self,keys):
        if keys.has_key(self.right): return keys[self.right]
        else: return False
         
    def isFire(self,keys):
        if keys.has_key(self.fire): return keys[self.fire]
        else: return False
         
 
         
class Testing:

    keys={}
    cxx,cyy,czz=0,0,8
    fxx,fyy,fzz=0,0,0   
    joystick=Joystick() 
    
    lock=False
    lastFrameTime=0
    topFPS=0

    def animate(self,FPS=24):
    
        if self.lock==True: return
    
        currentTime=time()
    
        glutPostRedisplay()
        
        glutTimerFunc(int(1000/FPS), self.animate, FPS)

        drawTime=currentTime-self.lastFrameTime
        if drawTime>0:
            self.topFPS=int(1000/(drawTime))
            if int(100*time())%100==0:
                print "draw time "+str(drawTime)+" top FPS "+str(1000/drawTime)           
                #self.tcxx,self.tcyy,self.tczz=random.randint(5,14),random.randint(5,14),random.randint(5,14)
        else:
            drawTime=1
            

        self.lastFrameTime=time()

    def __init__(self):

        
        print bool(glutInit)
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(640,480)
        glutCreateWindow(name)
        
        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    
        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glCullFace(GL_BACK) 
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        
        # // track material ambient and diffuse from surface color, call it before glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)
            
        glEnable(GL_LIGHTING)
        lightZeroPosition = [10.,4.,10.,1.]
        lightZeroColor = [0.9,1.0,0.9,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.2)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)
        
        #lightZeroPosition2 = [-10.,-4.,10.,1.]
        #lightZeroColor2 = [1.0,0.9,0.9,1.0] #green tinged
        #glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition2)
        #glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor2)
        #glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.2)
        #glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)
        #glEnable(GL_LIGHT1)
        
        MakeLists()
        
        glutIgnoreKeyRepeat(1)
        
        glutSpecialFunc(self.keydownevent)
        glutSpecialUpFunc(self.keyupevent)

        glutKeyboardFunc(self.keydownevent)
        glutKeyboardUpFunc(self.keyupevent)
        glutDisplayFunc(self.display)
        #glutIdleFunc(self.display)
        
        glMatrixMode(GL_PROJECTION)
        gluPerspective(60.0,640.0/480.,0.001,20.0)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        
        
        self.initkey("zxdcfvqaopm")
        
        self.animate()
        
        glutMainLoop()

        return




    def draw(self):
        
        self.lock=True
        
        try:
     
            global X,n, nm,cols
            glTranslate(0,0,0.0)
            glRotate(X,1,1,0)
            #glutSolidCube(1)
            #glScale(2,2,2) 
            
            glEnableClientState(GL_NORMAL_ARRAY)
            glEnableClientState(GL_COLOR_ARRAY)
            glEnableClientState(GL_VERTEX_ARRAY) 
            glNormalPointer(GL_FLOAT, 0, nm)    
            glColorPointer(3, GL_FLOAT, 0, cols)   
            glVertexPointer(3, GL_FLOAT, 0, n)   
            glPushMatrix()    
            glDrawArrays(GL_TRIANGLES,0,len(n)/3 )
            glPopMatrix()
            glDisableClientState(GL_VERTEX_ARRAY)
            glDisableClientState(GL_COLOR_ARRAY)
            glDisableClientState(GL_NORMAL_ARRAY)
            
            X+=3

        except:
            pass
            
        finally:                
            self.lock=False


    def initkey(self,cl):   
    
        for c in cl:
            self.keydownevent(c.lower(),0,0)        
            self.keyupevent(c.lower(),0,0)

    def display(self):

        glLoadIdentity()
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #glClearDepth(1.0)
        #glEnable(GL_DEPTH_TEST)
        #glDepthFunc(GL_LEQUAL)

        #glLoadIdentity()
        
        gluLookAt(self.cxx,self.cyy,self.czz,
                  self.fxx,self.fyy,self.fzz,
                  0,1,0)
        
        self.draw()
        
        glutSwapBuffers()
        #glFinish()

    def keydownevent(self,c,x,y):
    
        self.keys[c.lower()]=True
        glutPostRedisplay()
        
    def keyupevent(self,c,x,y):
    
        if self.keys.has_key(c.lower()): self.keys[c.lower()]=False
        glutPostRedisplay()







fp=open("piece1.dat","rb")

fp.seek(0,2)
flength=int(fp.tell())/48 #length in triangles 48=2 lots of coords for vertices and colours  *3 for how many components for coord  *8 and for nunber of bytes to store a double
print (("file",flength))


z=array.array("d")
fp.seek(0)
z.fromfile(fp,flength*3)
n=z.tolist()
print ("hello",len(n),n[:10])

cc=array.array("d")
#fp.seek(0)
cc.fromfile(fp,flength*3)
cols=cc.tolist()
print ("hello",len(cols),cols[:10])

def norm(u0,v0):        
    
    mu=sqrt(u0[0]**2 + u0[1]**2 + u0[2]**2)    
    if mu==0: mu=1        
    u=[x/mu for x in u0]    
    mv=sqrt(v0[0]**2 + v0[1]**2 + v0[2]**2)    
    if mv==0: mv=1        
    v=[x/mv for x in v0]       
    
    n= [
        u[1]*v[2]-u[2]*v[1],
        u[2]*v[0]-u[0]*v[2],
        u[0]*v[1]-u[1]*v[0]
    ]
    
    mn=sqrt(n[0]**2 + n[1]**2 + n[2]**2)    
    if mn==0: mn=1  
      
    return [x/mn for x in n]   
    


nm=[]
tt=0

try:
            
    for nn in range(0,len(n),9):
        ax,ay,az,bx,by,bz,cx,cy,cz=n[nn:nn+9]
        tt+=1
        a=[bx-ax,by-ay,bz-az]
        b=[cx-ax,cy-ay,cz-az]   
        nh=norm(a,b)
        ##each vertex has a normal we are spanning 3 above to get those that make a triange
        ##we are giving the same normal to each vertex in the triangle
        nm+=nh
        nm+=nh
        nm+=nh

except:
    print((tt,nn))


'''
cols=[]
        
for nn in range(0,len(n),9):
    cols+=[0,1,0]
    cols+=[random.random()*0.1,1.0,random.random()*0.1]
    cols+=[0,1,0]

'''
            

print n[:10]
print
print nm[:10]
print
print cols[:10]
print




        
if __name__ == '__main__': Testing()
