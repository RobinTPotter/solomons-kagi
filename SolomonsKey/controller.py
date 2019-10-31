from charSolomon import Solomon
from charSolomon import Solomon
from Action import Action, ActionGroup
from charBurst import Burst
from Joystick import Joystick
from Sprite import Sprite
from Models import lists, MakeLists, colours
from math import sin, cos, pi, floor, ceil, sqrt
from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

from config import *

def generateLevel(num):
    if num==0:
        return Level(["sssssssssssssssss",
            "s...............s",
            "s.......d.......s",
            "s.5.............s",
            "s.....sbbbs.....s",
            "s.....b343b.....s",
            "s..g..sbbbs..g..s",
            "s..g..sbbbs..g..s",
            "s......bbb......s",
            "s...2.......2...s",
            "s...sbs.1.sbs...s",
            "s...b@bbbbbkb...s",
            "s...sbs...sbs...s",
            "s...............s",
            "sssssssssssssssss"])

    if num==1:
        return Level([
            "sssssssssssssssss",
            "s...............s",
            "s.6.6...........s",
            "s.......4.....k.s",
            "s.ss.........bb.s",
            "s...ss.....bb...s",
            "s.....ss.bb.....s",
            "s...............s",
            "s.....bbbss.....s",
            "s.@.bbbbbbbss.d.s",
            "s.bb.........ss.s",
            "s...............s",
            "s...............s",
            "sssssssssssssssss"])


class Level:

    counter=0
    grid=None
    baddies=[]
    solomon=None
    sprites=[]
    bursts=[]
    door=None
    target_z=6
    proper_z=6

    AG_twinklers=None

    def sin_gen_1(self,tvsl):
        t,v,s,l=tvsl
        v=0.5*(1+sin(2*pi*t/(l)))
        #print (t,v)
        return v

    def sin_gen_2(self,tvsl):
        t,v,s,l=tvsl
        v=0.5*(1+sin(4*pi*t/(l)))
        #print (t,v)
        return v

    def __init__(self,griddata):

        griddata.reverse()

        #self.grid=griddata
        self.grid=[]
        for line in griddata:
            self.grid.append(list(line))

        rr=0
        for r in self.grid:
            cc=0
            for c in r:
                if c=="@":
                    self.solomon=Solomon(cc,rr,self)
                    self.grid[rr][cc]="."
                    self.solomon.A_wandswish.callback=self.block_swap
                    
                elif c=="4":
                    self.door=[cc,rr]
                    self.grid[rr][cc]="."

                elif c=="k":
                    ns=Sprite(cc,rr+0.5)
                    ns.setDrawFuncToList(lists["green_key"])
                    ns.collision_action=self.key_detected_something_test
                    self.sprites.append(ns)
                    self.grid[rr][cc]="."

                elif not c in ["b","B","s"]:
                    self.grid[rr][cc]="."

                cc+=1

            rr+=1

        self.AG_twinklers=ActionGroup()
        self.AG_twinklers.append("twinkle1",Action(func=self.sin_gen_1,max=200,cycle=True,min=0,reverseloop=False,init_tick=0))
        self.AG_twinklers.append("twinkle2",Action(func=self.sin_gen_2,max=100,cycle=True,min=0,reverseloop=False,init_tick=10))

    def eval_grid(self,coords):
        return self.grid[coords[1]][coords[0]]

    def key_detected_something_test(self):
        print ("KEY GOT!")

    def block_swap(self,bump_only=False):

        self.solomon.current_state["wandswish"]=False
        print("hi from block swap "+str(self.solomon))
        takeoff_for_crouching=0
        if self.solomon.state_test(["crouching"])>0 : takeoff_for_crouching=-0.5

        ##if res=="OK": return

        yy = self.block_to_action[1]
        xx = self.block_to_action[0]
        ch = self.grid[yy][xx]
        
        print('yy {} xx {} ch {} '.format(yy,xx,ch))
        
        
        if not bump_only:
            #wand flare!
            crouch=0.5
            if self.solomon.current_state["crouching"]==True: crouch=0
            self.bursts.append(Burst(x=self.solomon.x+self.solomon.facing*0.5,y=self.solomon.y+crouch,z=0))

        #must be in correct place first
        distanceLeft = 0.5 + (self.solomon.x)-(int(self.solomon.x))
        distanceRight = 0.5 + (int(self.solomon.x+1))-(self.solomon.x)
        distance = 0
        if self.solomon.facing==-1: distance=distanceLeft
        elif self.solomon.facing==1: distance=distanceRight
        
        print('distance {}'.format(distance))
        #check not in block space when casting
        
        if distance > 1.1:
            if bump_only:
                if ch=="b":
                    print("destroy block")
                    self.grid[yy][xx]="B"
                elif ch=="B":
                    print("destroy block")
                    self.grid[yy][xx]="."
                elif ch==".":
                    print("create")
                    self.grid[yy][xx]="b"
            else:
                if ch=="b":
                    print("destroy block")
                    self.grid[yy][xx]="."
                elif ch==".":
                    print("create")
                    self.grid[yy][xx]="b"
                elif ch=="k" and not bump_only:
                    print ("*****KEY STRUCK!*****")

    def grid_cell(self,coords):
        x=coords[0]
        y=int(coords[1])        
        dx = round(x - int(x),3)
        #print('in {} {} dx {}'.format(x,y,dx))
        if dx>0.5: x = int(x) + int(1)
        else: x = int(x)
        return [x,y]

    def evaluate(self,joystick,keys):

        self.counter+=1
        if self.counter>100000: self.counter=0

        self.solomon.stickers=[]

        self.solomon.stickers.append([self.solomon.x,self.solomon.y,0,"white"])
        """ TODO redo current_state was rubbish anyway """
        
        if  False:
            print('solomon x,y: {0},{1}'.format(self.solomon.x,self.solomon.y))  
            gx,gy=int(self.solomon.x),int(self.solomon.y)
            print('solomon gx,gy: {0},{1}'.format(gx,gy))            
            print('grid on: {0}'.format(self.grid[gy][gx]))
            print('grid below: {0}'.format(self.grid[gy-1][gx]))
        
        self.solomon.drawSolProperly=int((self.counter)/20)%2==0
        
        #under box
        twitch_left = 0.01
        # so the box presses to right edge flush
        sol_bottom_edge_x1 = self.solomon.x  - self.solomon.size_x/2 + twitch_left
        sol_bottom_edge_x2 = self.solomon.x  + self.solomon.size_x/2
        sol_bottom_edge_y2 = self.solomon.y - self.solomon.fall_detect    
        sol_top_edge_y2 = self.solomon.y + self.solomon.size_y       
        sol_top_edge_y2_jumping = self.solomon.y + self.solomon.size_y + 0.5
        
        #grid cell for below left and right
        sol_blockbelow_coord_x1 = self.grid_cell([sol_bottom_edge_x1,sol_bottom_edge_y2])
        sol_blockbelow_coord_x2 = self.grid_cell([sol_bottom_edge_x2,sol_bottom_edge_y2])
        
        #grid cell for above left and right
        sol_blockabove_coord_x1 = self.grid_cell([sol_bottom_edge_x1,sol_top_edge_y2_jumping])
        sol_blockabove_coord_x2 = self.grid_cell([sol_bottom_edge_x2,sol_top_edge_y2_jumping])
        
        #grid cell for right top and bottom
        sol_blockright_coord_y1 = self.grid_cell([sol_bottom_edge_x2+self.solomon.step_inc,sol_top_edge_y2])
        sol_blockright_coord_y2 = self.grid_cell([sol_bottom_edge_x2+self.solomon.step_inc,self.solomon.y])
        
        #grid cell for left top and bottom
        sol_blockleft_coord_y1 = self.grid_cell([sol_bottom_edge_x1-self.solomon.step_inc,sol_top_edge_y2])
        sol_blockleft_coord_y2 = self.grid_cell([sol_bottom_edge_x1-self.solomon.step_inc,self.solomon.y])
        
        #print ('{} {}'.format(sol_blockbelow_coord_x1,sol_blockbelow_coord_x2))
        
        
        #set state on behalf of block below
        if  self.grid[sol_blockbelow_coord_x1[1]][sol_blockbelow_coord_x1[0]]=='.' and \
            self.grid[sol_blockbelow_coord_x2[1]][sol_blockbelow_coord_x2[0]]=='.':
            self.solomon.current_state["canfall"]=True
        else:
            self.solomon.current_state["canfall"]=False
        
        
        #set state on behalf of block above
        if  self.grid[sol_blockabove_coord_x1[1]][sol_blockabove_coord_x1[0]]=='.' and \
            self.grid[sol_blockabove_coord_x2[1]][sol_blockabove_coord_x2[0]]=='.':
            self.solomon.current_state["headhurt"]=False
        else:
            self.solomon.current_state["headhurt"]=True
            print ("                            head hurt is true")
        
        
        #set state on behalf of right top and bottom
        if  self.grid[sol_blockright_coord_y1[1]][sol_blockright_coord_y1[0]]=='.' and \
            self.grid[sol_blockright_coord_y2[1]][sol_blockright_coord_y2[0]]=='.':
            self.solomon.current_state["cwright"]=True
        else:
            self.solomon.current_state["cwright"]=False
        
        #set state on behalf of left top and bottom
        if  self.grid[sol_blockleft_coord_y1[1]][sol_blockleft_coord_y1[0]]=='.' and \
            self.grid[sol_blockleft_coord_y2[1]][sol_blockleft_coord_y2[0]]=='.':
            self.solomon.current_state["cwleft"]=True
        else:
            self.solomon.current_state["cwleft"]=False
        
        #stickers for underneath (floor) detection
        #self.solomon.stickers.append([sol_bottom_edge_x1,sol_bottom_edge_y2,0,'green'])
        #self.solomon.stickers.append([sol_bottom_edge_x2,sol_bottom_edge_y2,0,'blue'])


        #stickers for underneath (head crash) detection
        self.solomon.stickers.append([sol_bottom_edge_x1,sol_top_edge_y2,0,'green'])
        self.solomon.stickers.append([sol_bottom_edge_x2,sol_top_edge_y2,0,'blue'])
        
        #stickers for right side solomon (wall) detect
        #self.solomon.stickers.append([sol_bottom_edge_x2,sol_top_edge_y2,0,'green'])
        #self.solomon.stickers.append([sol_bottom_edge_x2,self.solomon.y,0,'blue'])
        
        #stickers for left side solomon (wall) detect
        #self.solomon.stickers.append([sol_bottom_edge_x1,sol_top_edge_y2,0,'green'])
        #self.solomon.stickers.append([sol_bottom_edge_x1,self.solomon.y,0,'blue'])
        
        #stickers for showing which block is investigating
        #self.solomon.stickers.append(sol_blockbelow_coord_x1+[0.1,'green'])
        #self.solomon.stickers.append(sol_blockbelow_coord_x2+[0,'blue'])

        #wand is used to hover, so comes before fall and walk
        if joystick.isFire(keys):
            print('                            fire')
            if self.solomon.current_state["wandswish"]==False:
                print('                            swish is false')
                print('self.solomon.wand_rest {}'.format(self.solomon.wand_rest))
                if self.solomon.wand_rest==0:
                    self.solomon.wand_rest=self.solomon.wand_rest_start
                    #start swish
                    self.solomon.current_state["wandswish"]=True   
                    print ("                          swish")
                    if self.solomon.facing==-1: self.block_to_action = self.grid_cell([self.solomon.x-1,self.solomon.y])
                    elif self.solomon.facing==1:
                        if round((self.solomon.x-int(self.solomon.x)),3)==0.45: print (' booh! {}'.format(self.grid_cell([self.solomon.x+1,self.solomon.y])))
                        print ('                      plop')
                        self.block_to_action = self.grid_cell([self.solomon.x+1,self.solomon.y])
                    if self.solomon.current_state["crouching"]==True:
                        self.block_to_action=[self.block_to_action[0],self.block_to_action[1]-1]
                    
            else:
                #continue swish
                print ("                        blah")
                pass
        
        # decrease wand swish counter
        if self.solomon.wand_rest>0:
            self.solomon.wand_rest-=1

        # can fall state true and not swishing wand means can fall
        if self.solomon.current_state["canfall"] and self.solomon.current_state["wandswish"]==False:
            self.solomon.set_y(self.solomon.y-self.solomon.fall_inc)

        if self.solomon.current_state["canfall"]==False:
            if not int(self.solomon.y)==self.solomon.y:
                self.solomon.set_y(round(self.solomon.y ,1))
        
        # defaults to can't walk
        self.solomon.current_state["walking"]=False
        
        # crouch, does nothing to collision detection
        # only offsets the wand target
        self.solomon.current_state["crouching"]=False
        if joystick.isDown(keys):
            self.solomon.current_state["crouching"]=True            
            
        # if not crouching and keys pressed try walking right, animate but move only if can    
        if joystick.isRight(keys):
            self.solomon.facing=1
            if self.solomon.current_state["crouching"]==False:
                self.solomon.current_state["walking"]=True
                if self.solomon.current_state["cwright"]:
                    self.solomon.set_x(self.solomon.x+self.solomon.step_inc)
        
        # if not crouching and keys pressed try walking left, animate but move only if can
        if joystick.isLeft(keys):
            self.solomon.facing=-1
            if self.solomon.current_state["crouching"]==False:
                self.solomon.current_state["walking"]=True
                if self.solomon.current_state["cwleft"]:
                    self.solomon.set_x(self.solomon.x-self.solomon.step_inc)
 
 
 
 
 
        
        if self.solomon.current_state["jumping"]==False and \
            self.solomon.current_state["crouching"]==False and \
            self.solomon.current_state["falling"]==False and \
            self.solomon.current_state["canfall"]==False and \
            self.solomon.current_state["headhurt"]==False:
            if joystick.isUp(keys):
                print ('                      jumping rest (pressed) {}'.format(self.solomon.jumping_rest))
                if self.solomon.jumping_rest==0:
                    print ('                      jump rest is zero')
                    self.solomon.jumping_rest=self.solomon.jumping_rest_start
                    self.solomon.current_state["jumping"]=True
                    self.solomon.jumping_counter=0                
                    if joystick.isLeft(keys): self.solomon.jumping_dir=-1
                    elif joystick.isRight(keys): self.solomon.jumping_dir=1
                    else: self.solomon.jumping_dir=0
                    self.solomon.jump_inc = self.solomon.jump_inc_start
                    print ("                      start jump "+str(self.solomon.jumping_dir)+" "+str(self.solomon.state_test_on()))
                else:
                    print ('                      jump rest is NOT zero')
                    self.solomon.jumping_rest-=1
                    self.solomon.current_state["jumping"]=False
                    print ('                      jumping rest {}'.format(self.solomon.jumping_rest))

        if self.solomon.current_state["jumping"]==True and self.solomon.jumping_rest==0:            
            print ('                      jumping is true and jump rest is zero')
            if self.solomon.jumping_counter>self.solomon.jumping_counter_max:            
                print ('                      jumping_counter is > jumping_counter max')
                self.solomon.current_state["jumping"]=False
                self.solomon.jumping_counter=0
                print ("                      stop upward jump ")
            else:            
                print ('                      jumping_counter increased')
                self.solomon.jumping_counter+=1
            
        if self.solomon.current_state["jumping"]==True:
            if (self.solomon.jumping_dir==1 and (self.solomon.current_state["cwright"]==True)) \
            or (self.solomon.jumping_dir==-1 and (self.solomon.current_state["cwleft"]==True)):
                print ("                      jumping to the side")
                self.solomon.set_x(self.solomon.x+self.solomon.jumping_dir*self.solomon.step_inc)

            print ("                      jumping nonetheless")
            self.solomon.set_y(self.solomon.y+round(self.solomon.jump_inc,2))
            self.solomon.jump_inc*=self.solomon.jump_inc_falloff
        
        if self.solomon.current_state["jumping"]==True and self.solomon.current_state["headhurt"]==True:
            print ("                      stop jump")
            self.solomon.current_state["jumping"]=False
            self.solomon.jumping_counter=0
            self.solomon.jump_inc=0
            self.solomon.jumping_rest=0
            
        ##if self.solomon.current_state["jumping"]==True:
        ##    if (self.solomon.jumping_dir==1 and (distanceRight>0.4 or self.solomon.current_state["cwright"]==True)) \
        ##    or (self.solomon.jumping_dir==-1 and (distanceLeft>0.4 or self.solomon.current_state["cwleft"]==True)):
        ##        self.solomon.x+=self.solomon.jumping_dir*self.solomon.step_inc
        ##        print ("jumping and moving jumping dir: {0}, distanceRight {1}, distanceLeft {2}, grid left {3}, grid right {4}".format(self.solomon.jumping_dir,distanceRight,distanceLeft,left_grid_is,right_grid_is))
        ##    self.solomon.y+=round(self.solomon.jump_inc,2)
        ##    self.solomon.jump_inc*=self.solomon.jump_inc_falloff
            
        ##above = self.eval_grid(self.solomon_block_above)
        ##distance_above = 1+(int(self.solomon.y-1+0.5))-(self.solomon.y-1+0.5)
        ##
        ##if self.solomon.current_state["jumping"]==True and \
        ##    ( above in [ 'B','b','s' ] and distance_above>0.88): ##and ((distanceLeft<0.8 and self.solomon.facing==-1) or (distanceRight<0.8 and self.solomon.facing==1)) ):
        ##    self.solomon.current_state["jumping"]=False
        ##    print ("OUCH")
        ##    if not above=='s':
        ##        self.block_to_action=self.solomon_block_above
        ##        self.block_swap(bump_only=True)
        ##        
        ##
        ##
        ##
        ##
        ##
        ##
        ##
        
        
        # animate the walk cycle
        if self.solomon.current_state["walking"]:
            self.solomon.AG_walk.do()
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.AG_twinklers.do()
        
        return
        
        
        
        
            
    def reset_z(self):
        self.target_z=self.proper_z
        print ("reset z called")
        
    def detect(self):
        pass

    def draw(self):

        #global X
        #glRotate(X,1,0,0)

        glPushMatrix()
        glTranslate(8,6.5,-0.55)
        glScale(15,12,0.1)
        glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["red"])
        glutSolidCube(1)
        glPopMatrix()

        rr=0
        for r in self.grid:
            cc=0
            for c in r:
                #if True:
                if rr>=0 and rr<=13 and cc>=0 and cc<=16:
                    glPushMatrix()
                    glTranslate(cc,rr+0.5,0)
                    
                    if c in ["b","s"]:
                        if c=="b": color = [0.3,0.3,1.0,1.0]
                        elif c=="s": color = [1.0,1.0,0.0,1.0]
                        glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
                        if True: glutSolidCube(1)

                    elif c in ["d","6"]:
                        glEnable(GL_BLEND)
                        glBlendFunc(GL_SRC_ALPHA, GL_SRC_ALPHA);
                        if c=="d": color = [0.8,0.5,0.0, 0.1+0.2*float(self.AG_twinklers.value("twinkle1")) ]
                        elif c=="6": color = [10,0.5,0.0, 0.1+0.2*float(self.AG_twinklers.value("twinkle1")) ]
                        glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
                        glutSolidCube( float(self.AG_twinklers.value("twinkle2"))*0.3+0.7)
                        glBlendFunc(GL_SRC_ALPHA, GL_ONE)
                        glDisable(GL_BLEND)

                    elif c in ["B"]: ##i.e changed to half a block because recieved bash
                        color = [0.3,0.3,1.0,1.0]
                        glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
                        glCallList(lists["broken brick"])

                    glPopMatrix()

                cc+=1

            rr+=1

        glPushMatrix()
        self.solomon.draw(self.solomon.stickers)
        glPopMatrix()

        if debug==True:
            '''
            glPushMatrix()
            glTranslate(self.solomon_block_below[0],self.solomon_block_below[1],0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
            glutWireCube(0.85)
            glPopMatrix()

            glPushMatrix()
            glTranslate(self.solomon_block_above[0],self.solomon_block_above[1],0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
            glutWireCube(0.85)
            glPopMatrix()
            
            glPushMatrix()
            glTranslate(self.solomon_block_above_brow1[0],self.solomon_block_above_brow1[1],0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["green"])
            glutWireCube(0.85)
            glPopMatrix()
            
            glPushMatrix()
            glTranslate(self.solomon_block_above_brow2[0],self.solomon_block_above_brow2[1],0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["green"])
            glutWireCube(0.85)
            glPopMatrix()

            glPushMatrix()
            glTranslate(self.solomon_block_left[0],self.solomon_block_left[1],0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
            glutWireCube(0.85)
            glPopMatrix()

            glPushMatrix()
            glTranslate(self.solomon_block_right[0],self.solomon_block_right[1],0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
            glutWireCube(0.85)
            glPopMatrix()
            '''            
            #centre spot
            ##glPushMatrix()
            ##glTranslate(self.solomon.x,self.solomon.y,0)
            ##glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
            ##glScale(0.4, 0.4,0.4)
            ##glutSolidCube(1)
            ##glPopMatrix()
            
            #####size box for edge/falling etc
            ####glPushMatrix()
            ####glTranslate(self.solomon.x,self.solomon.y,0)
            ####glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["yellow"])
            ####glTranslate(0,self.solomon.size_y/2,0)
            ####glScale(self.solomon.size_x, self.solomon.size_y,1.0)
            ####glutWireCube(1)
            ####glPopMatrix()
            ####
            #####detection box for enemies/items
            ####glPushMatrix()
            ####glTranslate(self.solomon.x,self.solomon.y,0)
            ####glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["yellow"])
            ####glTranslate(0,self.solomon.det_size_y/2,0)
            ####glScale(self.solomon.det_size_x, self.solomon.det_size_y,1.0)
            ####glutWireCube(1)
            ####glPopMatrix()

        for s in self.sprites:
            glPushMatrix()
            s.runDetection(self)
            s.draw()
            glPopMatrix()
            s.do()
        
        for b in self.bursts:
            if b.draw():
                self.bursts.remove(b)
        
        
            




