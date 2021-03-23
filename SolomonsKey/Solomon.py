from Action import *
from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Models import lists, MakeLists, colours
from math import *

class Solomon:

    drawSolProperly=True
    solx,soly=None,None    
    sol_crouch=0
    sol_walking=0
    sol_wand=0
    sol_size = 6
    sol_dir = 1
    sol_jump = 0
    sol_crouch = 0
    sol_step = 1
    sol_jump_inc = 2
    sol_jump_limit = 6 ##floor((tile+4) /sol_jump_inc)
    sol_jump_rest = 0 
    sol_jump_rest_limit = 3
    sol_fall_inc = 2
    sol_wand = 0
    sol_wand_limit = 5
    AG_walk=None
    AG_jump=None
    A_wandswish=None
    tile =10

    def wobble(self,tvmm):
        t,v,mi,ma=tvmm
        v=t
        #print (t,v,mi,ma)
        return v

    def footR(self,tvsl):
        t,v,s,l=tvsl
        if t<7: v+=1
        elif t<10: v-=2
        else: v=0
        #print ('footR',t,v,s,l)
        return v

    def footL(self,tvsl):
        t,v,s,l=tvsl
        if t<7: v+=1
        elif t<10: v-=2
        else: v=0
        #print ('footL' ,t,v,s,l)
        return v

    def swish(self,tvmm):
        t,v,min,max=tvmm
        v=t
        print ('swish', t,v)
        return v

    def __init__(self,sx_sy):

        sx = sx_sy[0]
        sy = sx_sy[1]
        print ('init solomon {0},{1}'.format(sx,sy))
        
     
        self.solx=sx*self.tile
        self.soly=sy*self.tile

        ##self.startx=sx
        ##self.starty=sy

        self.AG_walk=ActionGroup()
        self.AG_walk.append("wobble",Action(func=self.wobble,max=5,cycle=True,min=-5,reverseloop=True,init_tick=0))
        self.AG_walk.append("footR",Action(func=self.footR,max=13,cycle=True,min=-1))
        self.AG_walk.append("footL",Action(func=self.footL,max=13,cycle=True,min=-1,init_tick=7))

        ##self.AG_jump=ActionGroup()
        ##self.AG_jump.append("jump_displacement",Action(func=self.jump_displacement,max=10,min=0))
        ##self.AG_jump.action("jump_displacement").callback=self.end_jump

        self.AG_walk.speed_scale(2)

        self.A_wandswish=Action(func=self.swish,min=-8,max=-1,cycle=False,reverseloop=False,init_tick=-6)


    def sol_tile_at_left_head(self,level):
        return int(level[floor((self.soly+self.sol_size)/self.tile)][(floor((self.solx-self.sol_step)/self.tile))])


    def sol_tile_at_left_foot(self,level):
        return int(level[floor((self.soly)/self.tile)][(floor((self.solx-self.sol_step)/self.tile))])


    def sol_tile_at_right_head(self,level):
        return int(level[floor((self.soly+self.sol_size)/self.tile)][(floor((self.solx+self.sol_size)/self.tile))])


    def sol_tile_at_right_foot(self,level):
        return int(level[floor((self.soly)/self.tile)][(floor((self.solx+self.sol_size)/self.tile))])


    def sol_tile_at_left_foot_floor(self,level):
        return int(level[floor((self.soly/self.tile))-1][(floor(self.solx/self.tile))])


    def sol_tile_at_right_foot_floor(self,level):
        return int(level[floor((self.soly/self.tile))-1][(floor((self.solx+self.sol_size-self.sol_step)/self.tile))])


    def sol_tile_at_left_head_ceiling(self,level):
        return int(level[floor((self.soly+self.sol_size)/self.tile)][(floor(self.solx/self.tile))])


    def sol_tile_at_right_head_ceiling(self,level):
        return int(level[floor((self.soly+self.sol_size)/self.tile)][(floor((self.solx+self.sol_size-self.sol_step)/self.tile))])


    def sol_block(self,level):
        return [floor((self.soly+self.sol_size/2)/self.tile)
        ,(floor((self.solx)/self.tile))]


    def sol_tile_dist_right_head(self,level):
        d = self.sol_size - ((self.solx+self.sol_size) % self.tile)
        if d==self.sol_size: d=0
        return d


    def sol_tile_dist_left_head(self,level):
        return (self.solx) % self.tile



    def draw(self):

        glTranslate(self.solx-2,self.soly-1.5,2)
        glScale(self.tile,self.tile,self.tile)

        if self.drawSolProperly==False:
            #size box for edge/falling etc
            glPushMatrix()
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["yellow"])
            #glTranslate(0,self.size_y/2,0)
            glScale(self.size_x, self.size_y,1.0)
            glutWireCube(1)
            glPopMatrix()

            #detection box for enemies/items
            glPushMatrix()
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["yellow"])
            glTranslate(0,self.det_size_y/2,0)
            glScale(self.det_size_x, self.det_size_y,1.0)
            glutWireCube(1)
            glPopMatrix()
        else:
            #offset model
            #glTranslate(0,0.35,0)
            #scale down character
            glScale(0.3,0.3,0.3)

        #rotate to direction sol_dir
        if self.sol_dir==-1: glRotatef(180,0,1,0)

        #correction for drawing character
        glRotatef(-90.0,1.0,0,0)

        #if not self.drawSolProperly:
        #    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
        #    glutSolidCube(0.2)

        #############################entering crouch section###############################
        glPushMatrix()

        if self.sol_crouch==1: glTranslate(0,0,-0.4)
        if self.sol_walking==1: glRotatef(-8.0*float(self.AG_walk.value("wobble")),0.0,0.0,1.0)

        draw_body=True

        if draw_body:

            #hat
            glPushMatrix()
            if self.sol_walking==1: glRotatef(-float(self.AG_walk.value("wobble")),1.0,0,0)
            glTranslate(0,0,0.5)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["hat"])
            if self.drawSolProperly: glutSolidCone(1,2,12,6)
            glPopMatrix()

            #head/body
            glPushMatrix()
            glTranslate(0,0,0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["body"])
            if self.drawSolProperly: glutSolidSphere(1,12,12)
            glPopMatrix()

            #left arm
            glPushMatrix()
            if self.sol_walking==1: glTranslate(0-float(self.AG_walk.value("footR"))/10,0.9,0)
            else: glTranslate(0,0.9,0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["arm"])
            if self.drawSolProperly: glutSolidSphere(0.5,24,12)
            glPopMatrix()

        #right arm
        glPushMatrix()
        #glTranslate(0,-0.9,0)
        if self.sol_wand>0:
            res=self.A_wandswish.do()
            if res==None: poo=0.0
            else: poo=float(res/0.05)
            #print poo
            glTranslate(0,-0.9,0)
            glRotatef(poo,1,1,0)

        elif self.sol_walking==1: glTranslate(float(self.AG_walk.value("footL"))/10,-0.9,0)
        else: glTranslate(0,-0.9,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["arm"])
        if self.drawSolProperly: glutSolidSphere(0.5,24,12)
        #move pop to end to keep arm local system

        #wand
        q=gluNewQuadric()

        glPushMatrix()
        glTranslate(1.1,0,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["wandtip"])
        glRotatef(90,0,1,0)
        if self.drawSolProperly: gluCylinder(q,0.1,0.1,0.2,12,1)
        glPopMatrix()

        glPushMatrix()
        glTranslate(0.5,0,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["wand"])
        glRotatef(90,0,1,0)
        if self.drawSolProperly: gluCylinder(q,0.1,0.1,0.6,12,1)
        glPopMatrix()

        #from arm
        glPopMatrix()

        #eyes
        glPushMatrix()
        glTranslate(1,.2,.1)
        glRotatef(90,0,1,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["wandtip"])
        if self.drawSolProperly: gluDisk(q,0.05,0.2,12,12)
        glPopMatrix()

        glPushMatrix()
        glTranslate(1,-.2,.1)
        glRotatef(90,0,1,0)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["wandtip"])
        if self.drawSolProperly: gluDisk(q,0.05,0.2,12,12)
        glPopMatrix()

        #nose
        glPushMatrix()
        glTranslate(1,0,-.1)
        glScale(1,1,0.5)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["arm"])
        if self.drawSolProperly: glutSolidSphere(0.3,24,12)
        glPopMatrix()

        ##########################left crouch section##################################
        glPopMatrix() #end of crouch

        #drawing rest of body (feet)
        #left foot
        glPushMatrix()
        glTranslate(-0.5,0,0)
        #apply rotation if walking
        if self.sol_walking==1: glRotatef(-15*float(self.AG_walk.value("footL")),0,1,0)
        else: glRotatef(0,0,1,0)
        glTranslate(0.5,0,0)
        glScale(1.7,1,.5)
        glTranslate(0,0.5,-2)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["shoe"])
        if self.drawSolProperly: glutSolidSphere(0.5,24,12)
        glPopMatrix()

        #right foot
        glPushMatrix()
        glTranslate(-0.5,0,0)
        #apply rotation if walking
        if self.sol_walking==1: glRotatef(-15*float(self.AG_walk.value("footR")),0,1,0)
        else: glRotatef(0,0,1,0)
        glTranslate(0.5,0,0)
        glScale(1.7,1,.5)
        glTranslate(0,-0.5,-2)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["shoe"])
        if self.drawSolProperly: glutSolidSphere(0.5,24,12)
        glPopMatrix()
        



