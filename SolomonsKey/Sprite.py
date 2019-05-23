from Action import Action, ActionGroup
from Models import lists, MakeLists, colours

from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


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
        #level.detect(self.x,self.y,collision_bound=2.0,callback=self.collision_action,ignoreDots=True,ignoreTheseSprites=[self])
        pass

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

    def run_collision_action(self):
        if self.collision_action!=None: self.collision_action()
        return self
            
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

