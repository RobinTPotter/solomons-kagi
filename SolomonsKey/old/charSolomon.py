from Action import *
from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from Models import lists, MakeLists, colours

class Solomon:

    drawSolProperly=True
    x,y=None,None
    startx,starty=None,None
    #st_a=None
    AG_walk=None
    AG_jump=None
    A_wandswish=None
    current_state={}
    size_x=0.6
    size_y=0.8
    det_size_x=0.4
    det_size_y=0.6
    jumping_counter = 0
    jumping_counter_max = 6
    jump_inc_start = 0.1
    jump_inc = 0.1
    jump_inc_falloff = -0.1
    step_inc = 0.050
    jumping_dir=0
    jumping_rest=0
    jumping_rest_start=4 ##cycles to rest before jump
    fall_inc=0.2
    fall_detect=0.01
    wand_rest=0
    wand_rest_start=8 ##cycles to rest before jump

    bound=0.3 #this is his bounding sphere
    step=0.100
    facing=1 #or -1

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
        #print (t,v)
        return v

    def jump_displacement(self,tvmm):
        print("jump disp called")
        t,v,min,max=tvmm
        if t<4: v+=2
        else: v+=1
        return v


    def end_jump(self):
        print("jump complete")
        self.current_state["jumping"]=False

    def __init__(self,sx,sy):

        print ('init solomon {0},{1}'.format(sx,sy))

        self.current_state["standing"]=True
        self.current_state["crouching"]=False
        self.current_state["walking"]=False
        self.current_state["jumping"]=False
        self.current_state["wandswish"]=False
        self.current_state["falling"]=False
        self.current_state["cwleft"]=False
        self.current_state["cwright"]=False
        self.current_state["canfall"]=False
        self.current_state["headhurt"]=False

        self.x=sx
        self.y=sy

        self.startx=sx
        self.starty=sy

        self.AG_walk=ActionGroup()
        self.AG_walk.append("wobble",Action(func=self.wobble,max=5,cycle=True,min=-5,reverseloop=True,init_tick=0))
        self.AG_walk.append("footR",Action(func=self.footR,max=13,cycle=True,min=-1))
        self.AG_walk.append("footL",Action(func=self.footL,max=13,cycle=True,min=-1,init_tick=7))

        self.AG_jump=ActionGroup()
        self.AG_jump.append("jump_displacement",Action(func=self.jump_displacement,max=10,min=0))
        self.AG_jump.action("jump_displacement").callback=self.end_jump



        self.AG_walk.speed_scale(2)

        self.A_wandswish=Action(func=self.swish,min=-8,max=-1,cycle=False,reverseloop=False,init_tick=-6)


    def set_x(self,x):
        self.x=round(x,2)
        print('set x {}'.format(self.x))##+" "+str(self.state_test_on()))

    def set_y(self,y):
        self.y=round(y,2)
        print('set y {}'.format(self.y))##+" "+str(self.state_test_on())+" "+str(self.jumping_rest))

    def state_test_on(self):
        return [k for k in self.current_state if self.current_state[k]==True]

    def state_test(self,list):
        return len([l for l in list if self.current_state[l]==True])


    def draw0(self,stickers=None):
        glTranslate(self.x,self.y,0)
        glutSolidCube(0.5)


    def draw(self,stickers=None):


        if stickers!=None:
            for st in stickers:
                glPushMatrix()
                ##glLoadIdentity()
                #print((st))   
                glMaterialfv(GL_FRONT,GL_DIFFUSE,colours[st[3]])
                glTranslate(st[0],st[1],st[2])
                glutSolidCube(0.05)
                glPopMatrix()



        #if self.drawSolProperly:
        #    #correction
        #    glTranslate(0,-0.15,0)

        #main displacement
        glTranslate(self.x,self.y,0)

        if self.drawSolProperly==False:
            #size box for edge/falling etc
            glPushMatrix()
            #glTranslate(self.x,self.y,0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["yellow"])
            glTranslate(0,self.size_y/2,0)
            glScale(self.size_x, self.size_y,1.0)
            glutWireCube(1)
            glPopMatrix()

            #detection box for enemies/items
            glPushMatrix()
            #glTranslate(self.x,self.y,0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["yellow"])
            glTranslate(0,self.det_size_y/2,0)
            glScale(self.det_size_x, self.det_size_y,1.0)
            glutWireCube(1)
            glPopMatrix()
        else:
            #offset model
            glTranslate(0,0.35,0)
            #scale down character
            glScale(0.3,0.3,0.3)

        #rotate to direction facing
        if self.facing==-1: glRotatef(180,0,1,0)

        #correction for drawing character
        glRotatef(-90.0,1.0,0,0)

        #if not self.drawSolProperly:
        #    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
        #    glutSolidCube(0.2)

        #############################entering crouch section###############################
        glPushMatrix()

        if "crouching" in self.state_test_on(): glTranslate(0,0,-0.4)
        if "walking" in self.state_test_on(): glRotatef(-8.0*float(self.AG_walk.value("wobble")),0.0,0.0,1.0)

        draw_body=True

        if draw_body:

            #hat
            glPushMatrix()
            if "walking" in self.state_test_on(): glRotatef(-float(self.AG_walk.value("wobble")),1.0,0,0)
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
            if self.state_test(["walking"])>0: glTranslate(0-float(self.AG_walk.value("footR"))/10,0.9,0)
            elif self.state_test(["standing","crouching","wandswish"])>0: glTranslate(0,0.9,0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["arm"])
            if self.drawSolProperly: glutSolidSphere(0.5,24,12)
            glPopMatrix()

        #right arm
        glPushMatrix()
        #glTranslate(0,-0.9,0)
        if self.state_test(["wandswish"])>0:
            res=self.A_wandswish.do()
            if res==None: poo=0.0
            else: poo=float(res/0.05)
            #print poo
            glTranslate(0,-0.9,0)
            glRotatef(poo,1,1,0)

        elif self.state_test(["walking"])>0: glTranslate(float(self.AG_walk.value("footL"))/10,-0.9,0)
        elif self.state_test(["standing","crouching"])>0: glTranslate(0,-0.9,0)
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
        if self.state_test(["walking"])>0: glRotatef(-15*float(self.AG_walk.value("footL")),0,1,0)
        elif self.state_test(["standing","crouching","wandswish"])>0: glRotatef(0,0,1,0)
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
        if self.state_test(["walking"])>0: glRotatef(-15*float(self.AG_walk.value("footR")),0,1,0)
        elif self.state_test(["standing","crouching","wandswish"])>0: glRotatef(0,0,1,0)
        glTranslate(0.5,0,0)
        glScale(1.7,1,.5)
        glTranslate(0,-0.5,-2)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["shoe"])
        if self.drawSolProperly: glutSolidSphere(0.5,24,12)
        glPopMatrix()



