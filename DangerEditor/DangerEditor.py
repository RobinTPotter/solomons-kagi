import sys, traceback

from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import random
import sys
from time import time,strftime
#import math
from Letters import lists, MakeLists

import re

name = "danger editor - pyopengl code manipulator"

colours={}

colours["dark_grey"]=[0.2,0.2,0.2,1.0]
colours["grey"]=[0.5,0.5,0.5,1.0]
colours["light_grey"]=[0.8,0.8,0.8,1.0]
colours["gold"]=[1.0,0.9,0.0,1.0]
colours["red"]=[1.0,0.0,0.0,1.0]
colours["dark_red"]=[0.4,0.0,0.0,1.0]
colours["green"]=[0.0,1.0,0.0,1.0]
colours["dark_green"]=[0.0,0.4,0.0,1.0]
colours["blue"]=[0.0,0.0,1.0,1.0]
colours["yellow"]=[1.0,1.0,0.0,1.0]
colours["cyan"]=[0.0,1.0,1.0,1.0]
colours["pink"]=[1.0,0.0,1.0,1.0]
colours["white"]=[1.0,1.0,1.0,1.0]
colours["brown"]=[0.24,0.007,0.0,1.0]
colours["black"]=[0,0,0,1.0]

file_name=""

try:
    file_name=sys.argv[1]
except:
    if file_name=="":
        file_name="DangerCode"+str(strftime("%Y%m%d_%H%M%S"))+".txt"


class Joystick:

    keys={}
    up,down,left,right,fire="","","","",""
    isPressed=False


    def __init__(self,up=101,down=103,left=100,right=102,fire="m"):

        self.isAlt=False
        self.isShift=False
        self.isControl=False
        self.up=up
        self.down=down
        self.left=left
        self.right=right
        self.fire=fire
        self.fire=fire
        self.keys[self.up]=False
        self.keys[self.down]=False
        self.keys[self.left]=False
        self.keys[self.right]=False
        self.keys[self.fire]=False

    def register(self,ch,down):
        #print "register "+str(ch)+str(type(ch))
        extra=""
        if type(ch) is str:
            extra=str(ord(ch))
            if extra in ["13","27","8"]: ch=int(extra)

        #if not self.keys.has_key(ch): print str(ch)+" "+extra
        self.keys[ch]=down

    def isKey(self,ch):
        if self.keys.has_key(ch):
            return self.keys[ch]
        else: return False

    def isUp(self):
        if self.keys.has_key(self.up):
            return self.keys[self.up]
        else: return False

    def isDown(self):
        if self.keys.has_key(self.down): return self.keys[self.down]
        else: return False

    def isLeft(self):
        if self.keys.has_key(self.left): return self.keys[self.left]
        else: return False

    def isRight(self):
        if self.keys.has_key(self.right): return self.keys[self.right]
        else: return False

    def isFire(self):
        if self.keys.has_key(self.fire): return self.keys[self.fire]
        else: return False


class Thing:

    lastFrameTime=0

    state="browse"

    xx,yy,zz=0,0,5
    cxx,cyy,czz=0,0,0
    X=0

    xRot=0
    yRot=0
    mPos=[0,0]
    speed=0.1

    menu=[]
    menuindex=0

    temp=[]
    editing=None
    edititem=None

    joystick=Joystick()

    zoom=5

    WIDTH=640.0
    HEIGHT=480.0

    lastMenu=""

    def logic(self):


        

        self.lock=True

        tmp=self.temp

        if self.joystick.isUp():
            #print "menu length: "+str(len(self.menu))
            if len(self.menu)>0: self.menuindex=( self.menuindex-1 ) % len(self.menu)
            #print self.menuindex

            #return

        elif self.joystick.isDown():
            #print "menu length: "+str(len(self.menu))
            if len(self.menu)>0: self.menuindex=( self.menuindex+1 ) % len(self.menu)
            #print self.menuindex
            #return

        elif self.joystick.isKey(27): ##escape edit mode
            self.state="browse"
            if self.state=="edit": self.menuindex=self.edititem
            print str(self.menuindex)
            #return

        elif self.state=="browse":




            if self.joystick.isKey("w"): ##write out

                try:
                    f=open(file_name,"w")
                    for ll in tmp:
                        f.write(ll+"\n")
                    f.write("\n")
                    f.close()
                    print "written out file "+str(file_name)
                    #return

                except Exception as ex:
                    print "bugger, "+str(file_name)+" not written out"

            elif self.joystick.isKey("l"): ##load in 

                try:
                    f=open(file_name,"r")
                    data=f.read()
                    for ll in data.split("\n"):
                        if not (len(ll)==0 or ll==""): tmp.append(ll)

                    f.close()
                    print "successfully read "+str(file_name)

                    ##had to to this wasn't updateing other wise
                    self.menuindex=0
                    self.temp=tmp
                    self.menu=self.temp


                except Exception as ex:
                    print "bugger, file "+str(file_name)+" not read"

                #return

            elif self.joystick.isKey("a"): ##add object
                self.state="add"
                self.menu=["COMMENT","PUSH-POP","TRANSLATE","SCALE","CUBE","SPHERE","POLYGON","LINES","POINT","CONE","DISC","CYLINDER","ROTATE"]
                for cc in colours.keys(): self.menu.append("COLOUR_"+cc.upper())
                self.edititem=self.menuindex
                self.menuindex=0
                self.lastMenu=" "
                #return

            elif self.joystick.isKey("u"): ##move up
                if len(tmp)>1: tmp.insert((self.menuindex-1)%(len(tmp)),tmp.pop(self.menuindex))
                if len(self.menu)>0: self.menuindex=( self.menuindex-1 ) % len(self.menu)
                self.lastMenu=" "
                #return

            elif self.joystick.isKey("d"): ##move down
                if len(tmp)>1: tmp.insert((self.menuindex+1)%(len(tmp)),tmp.pop(self.menuindex))
                if len(self.menu)>0: self.menuindex=( self.menuindex+1 ) % len(self.menu)
                self.lastMenu=" "
                #return

            elif self.joystick.isKey("c"): ##copy in place
                tmp.insert(self.menuindex,tmp[self.menuindex])
                self.lastMenu=" "
                #return

            elif self.joystick.isKey(13) and len(tmp)>0: ##edit mode

                self.state="edit"
                if self.menuindex>=len(self.menu): self.menuindex=0
                self.editing=self.menu[self.menuindex]

                self.edititem=self.menuindex
                commands=self.editing.split("###")[1:]
                for cc in range(0,len(commands)):
                    if commands[cc][0]=="I":
                        commands[cc]=commands[cc][1:]

                if len(commands)>0:
                    values=re.findall("-{0,1}[0-9\.]+",self.editing)
                    #print "commands "+str(commands)
                    #print "values "+str(values)
                    self.menu=[str(k)+" "+str(v) for k,v in zip(commands,values)]
                    self.menuindex=0
                    #return
                else:
                    self.state="browse"
                    #return


            elif self.joystick.isKey(8) and len(tmp)>0: ##delete
                print "delete! started"
                print "delete! "+str(self.menuindex)
                print "delete! "+str(self.menu[self.menuindex])
                print "delete! "+str(tmp[self.menuindex])
                
                
                if str(self.menu[self.menuindex])=="glPopMatrix()" or str(self.menu[self.menuindex])=="glEnd()": 
                    self.lastMenu=" "
                    #do nothing
                    return
                
                if str(self.menu[self.menuindex])=="glPushMatrix()":
                    #delete next pop then this
                    ii=self.menuindex+1
                    doneit=False
                    while doneit==False:
                        if self.menu[ii]=="glPopMatrix()":
                            tmp.pop(ii)
                            doneit=True
                        ii+=1
                    
                    
                
                if str(self.menu[self.menuindex])=="glBegin(GL_POLYGON)":
                    #delete next pop then this
                    ii=self.menuindex+1
                    doneit=False
                    while doneit==False:
                        if self.menu[ii]=="glEnd()":
                            tmp.pop(ii)
                            doneit=True
                        ii+=1
                    
                    
                    
  
                tmp.pop(self.menuindex)
                    
                if self.menuindex>=len(tmp): self.menuindex=len(tmp)-1 
                self.lastMenu=" "
                #return



        elif self.state=="add":

            if self.joystick.isKey(13):

                if self.menu[self.menuindex]=="CUBE":
                    tmp.insert(self.edititem,"glutSolidCube(0.5) ###size")  #+="glPushMatrix()\nglutSolidCube(0.5)\nglPopMatrix()\n"
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="COMMENT":
                    tmp.insert(self.edititem,"#COMMENT /*                  */")
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="PUSH-POP":
                    ##note there are two item to add so this is back to front
                    tmp.insert(self.edititem,"glPopMatrix()")
                    tmp.insert(self.edititem,"glPushMatrix()")
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="SPHERE":
                    tmp.insert(self.edititem,"glutSolidSphere(0.5,12,12) ###size###Isegments###Istacks")
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="POLYGON":
                    tmp.insert(self.edititem,"glEnd()")
                    tmp.insert(self.edititem,"glBegin(GL_POLYGON)")
                    tmp.insert(self.edititem,"glVertex3f(1.00,0.00,0.00) ###NO###XXX###YYY###ZZZ")
                    tmp.insert(self.edititem,"glVertex3f(0.00,1.00,0.00) ###NO###XXX###YYY###ZZZ")
                    tmp.insert(self.edititem,"glVertex3f(0.00,0.00,1.00) ###NO###XXX###YYY###ZZZ")    
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="LINES":
                    tmp.insert(self.edititem,"glEnd()")
                    tmp.insert(self.edititem,"glLineWidth(3.0) ###width")
                    tmp.insert(self.edititem,"glBegin(GL_LINES)")
                    tmp.insert(self.edititem,"glVertex3f(1.00,0.00,0.00) ###NO###XXX###YYY###ZZZ")
                    tmp.insert(self.edititem,"glVertex3f(-1.00,0.00,0.00) ###NO###XXX###YYY###ZZZ")
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="POINT":
                    tmp.insert(self.edititem,"glVertex3f(0.00,0.00,1.00) ###NO###XXX###YYY###ZZZ")   
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="CONE":
                    ##note there are two item to add so this is back to front
                    tmp.insert(self.edititem,"glutSolidCone(0.5,0.5,12,1) ###radius###size###Isegs###Istacks")
                    try:
                        test=tmp.index("q=gluNewQuadric()")
                    except:
                        tmp.insert(self.edititem,"q=gluNewQuadric()")
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="DISC":
                    ##note there are two item to add so this is back to front
                    tmp.insert(self.edititem,"gluDisk(q,0.05,0.2,12,12) ###xxx###yyy###Isegments###Istacks")
                    try:
                        test=tmp.index("q=gluNewQuadric()")
                    except:
                        tmp.insert(self.edititem,"q=gluNewQuadric()")
                    self.state="browse"
                elif self.menu[self.menuindex]=="CYLINDER":
                    tmp.insert(self.edititem,"gluCylinder(q,1,1,1,10,1) ###xxx###yyy###zzz###Isub###Istack")
                    #self.menuindex=0
                #lif self.menu[self.menuindex]=="COLOR":
                #    tmp.insert(self.edititem,"glColor(0.0,0.0,0.0) ###Icol_r###Icol_g###Icol_b")
                #    self.state="browse"
                #    #self.menuindex=0
                #
                elif self.menu[self.menuindex]=="ROTATE":
                    tmp.insert(self.edititem,"glRotate(0.0,0,1,0) ###value###axis_x###axis_y###axis_z")
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="TRANSLATE":
                    tmp.insert(self.edititem,"glTranslate(0.0,0.0,0.0) ###trans_x###trans_y###trans_z")
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex]=="SCALE":
                    tmp.insert(self.edititem,"glScale(1.0,1.0,1.0) ###scale_x###scale_y###scale_z")
                    self.state="browse"
                    #self.menuindex=0
                elif self.menu[self.menuindex].startswith("COLOUR_"):
                    col=self.menu[self.menuindex][7:].lower()
                    tmp.insert(self.edititem,"glMaterialfv(GL_FRONT,GL_DIFFUSE,colours[\""+str(col)+"\"])")
                    self.state="browse"
                    #self.menuindex=0



        elif self.state=="edit":

            if self.joystick.isLeft():
            
                tmp=self.gogoEdit(-1,tmp)        
                self.lastMenu=" "

                

            elif self.joystick.isRight():
            
                tmp=self.gogoEdit(1,tmp)        
                self.lastMenu=" "



        self.temp=tmp
        ##print str(self.temp)
        ##print "done tmp to temp"


        if self.menuindex>=len(self.menu): self.menuindex=len(self.menu)-1
        self.lock=False



    def gogoEdit(self,direction,tmp):
    


        #print "editting"
        #print str(self.editing)
        #print str(self.edititem)
        #print str(self.menuindex)
        #print "left"

        #if self.edititem>=len(self.menu): self.edititem=0


        
        commands=self.editing.split("###")[1:]
        if len(commands)>0:
            values=re.findall("-{0,1}[0-9\.]+",self.editing)
            
        editing_command=commands[self.menuindex]
        
        if editing_command=="NO": return tmp
        
        editing_value=float(values[self.menuindex])

        val=0.1
        if self.joystick.isShift and not self.joystick.isControl: val=1
        elif self.joystick.isControl and not self.joystick.isShift: val=0.01
        elif self.joystick.isControl and self.joystick.isShift: val=10
        editing_value+=val*direction

        old=self.editing
        m=None
        mit=re.finditer("-{0,1}[0-9\.]+",old)
        for i in range(0,self.menuindex+1):
            m=mit.next()

        #print "m: "+str(m)+" "+str(dir(m))+" "+str(m.group())+" ms:"+str(m.start())+ "me:"+str(m.end())

        if editing_command[0]=="I":
            neww=old[0:m.start()]+str(int(editing_value))+old[m.end():]
            editing_command=editing_command[1:]
        else: neww=old[0:m.start()]+str(editing_value)+old[m.end():]

        #print "swapping left "+str(tmp[self.edititem])+" for "+str(neww)
        tmp[self.edititem]=neww
        self.menu[self.menuindex]=str(editing_command)+" "+str(editing_value)
        self.editing=neww

        return tmp
        #print str(self.editing)
        #print str(self.edititem)
        #print str(self.menuindex)





    def animate(self,FPS=1):

        if self.lock==True: return

        currentTime=time()


        self.logic()



        self.X+=1
        if self.X>1000: self.X=0

        #print "posting redisplay"
        glutPostRedisplay()

        tt=int(1000/FPS)
        #print tt, FPS
        glutTimerFunc(tt, self.animate, FPS)
        drawTime=currentTime-self.lastFrameTime
        self.topFPS=int(1000/drawTime)

        #if int(100*time())%100==0: print "draw time "+str(drawTime)+" top FPS "+str(1000/drawTime)+str((self.temp))





    def draw(self):

        if self.lock==True: return

        try:



            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluPerspective(60.0,self.WIDTH/self.HEIGHT,1.,50.)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
                      
            glEnable(GL_DEPTH_TEST)  

            glPushMatrix()

            #tweaks to set up and a white wired cube for 1,1,1 scale help
            glTranslate(0,0,0-self.zoom)
            glTranslate(0,0,3)
            glRotate(-self.yRot*2,1,0,0)
            glRotate(-self.xRot*2,0,1,0)
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])
            glutWireCube(1)

            ##axes
            glBegin(GL_LINES)

            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["red"])
            for xxx in range(1,10):
                glVertex3f(0.5*(xxx-1), 0, 0)
                glVertex3f(0.5*(xxx), 0, 0)

            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["green"])
            for xxx in range(1,10):
                glVertex3f(0,0.5*(xxx-1), 0)
                glVertex3f(0,0.5*(xxx), 0)

            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["blue"])
            for xxx in range(1,10):
                glVertex3f(0,0,0.5*(xxx-1))
                glVertex3f(0,0,0.5*(xxx))

            glEnd()

            ##set colour to white
            glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["white"])

            try:
                ERROR_MESSAGE=""
                ##danger code! - literally dump python script into scene
                offset=0
                for t in self.temp:
                    if t=="glPopMatrix()": offset-=1
                    exec(t)
                    if t=="glPushMatrix()": offset+=1
                
            except Exception as e:                    
                ERROR_MESSAGE=str(e).upper()
                #print ERROR_MESSAGE
                while offset>0:
                    glPopMatrix()
                    offset-=1
                    
                
            
            glPopMatrix()
            
            
            

            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            gluOrtho2D(0,self.WIDTH,0,self.HEIGHT)
            glMatrixMode(GL_MODELVIEW)            
            glLoadIdentity()
            
            glDisable(GL_DEPTH_TEST)  
            
            #glScale(self.WIDTH/640.0,self.WIDTH/640.0,1)
            
            textOn=True
            #if self.X %2 == 0: textOn=False
            
            if textOn==True:

                #disable lights for the text etc
                glDisable(GL_LIGHTING)

                #for xxx in range(0,5): #int(self.WIDTH),10):
                #    for yyy in range(0,5): #int(self.HEIGHT),10):                
                #        glPushMatrix()
                #        glTranslate(xxx,yyy,0)
                #        #glutWireCube(.5)
                #        self.drawString("*")
                #        glPopMatrix()

                #glPushMatrix()
                #glTranslate(-0.7,0,0)
                #glScale(0.0028,0.003,0.003)
                #glTranslate(0,0,1255)

                #glTranslate(-100,0,0)


                #draw the editor state word top left
                glPushMatrix()
                glTranslate(20,self.HEIGHT-20,0)   
                self.drawString(self.state.upper())
                
                if not ERROR_MESSAGE=="":
                    #print "argrgrg"
                    glTranslate(0,-30,0)   
                    self.drawString(ERROR_MESSAGE,"red")
                
                glPopMatrix()

                mn=0


                glTranslate(20,self.HEIGHT/2,0)



                glTranslate(0,-15,0)
                if len(self.menu)>0: self.drawString("*")
                        
                glTranslate(0,15,0)

                
                ##shift everything so the cursor is always at the centre screen
                glTranslate(0,14*self.menuindex,0)


                temponly=False







                ##check to see if menu has anything in it - overwrite temporarily if so
                if self.state=="browse":
                    if len(self.menu)==0:
                        self.menu=["NO ITEMS"]
                        temponly=True
                    else:
                        self.menu=self.temp







                #this block is to compile or draw menu
                
                
                '''            
                lists["menu"] = glGenLists(1) 
                glNewList(lists["menu"],GL_COMPILE) 
                    #....
                glEndList()
                '''
                
                '''                
                if lists.has_key("menu"): glCallList(lists["menu"])
                '''



                
                if self.lastMenu==self.menu:
                    if lists.has_key("menu"): glCallList(lists["menu"])
                    #print("menu called")
                else:
                    #print("menu generated") 
                    
                    lists["menu"] = glGenLists(1) 
                    glNewList(lists["menu"],GL_COMPILE) 


                    ##draw the menu
                    ##push offset
                    offset=0

                    for mi in self.menu:

                        if mi=="glPopMatrix()": offset-=1

                        string=""
                        offsetspaces=""
                        for oo in range(0,offset):
                            offsetspaces+=" "

                        
                        #print mi
                        if mn==self.menuindex:
                            #print "yo!"
                            string=" "+offsetspaces+mi
                        else:
                            string=" "+offsetspaces+mi
                        
        
                        #glTranslate(10,0,0)
                        glTranslate(0,-14,0)
                        self.drawString(string)
                        mn+=1

                        if mi=="glPushMatrix()": offset+=1


                    glEndList()






                self.lastMenu=self.menu


                ##put back normal menu
                if temponly==True: self.menu=[]

                #glPopMatrix()

                glEnable(GL_LIGHTING)

        except Exception as e:

            print str(traceback.print_exc(file=sys.stdout))

            print "Bollocks! Dumping\n----------------------------\n\n"
            for f in self.temp:
                print f

            print "\n----------------------------\nBollocks! Dumped!\n\n"
            sys.exit(0)

        finally:
            pass


    def drawString(self,string,col="yellow"):
        glPushMatrix()

        for l in range(0,len(string)):
            
            if string[l].upper()=="#":
                if len(string[l:])>2:
                    if string[l:l+3]=="###": break
            
            glPushMatrix()
            glTranslate(0,0,0.5)
            glColor(colours["black"])
            glLineWidth(3.0)
            if lists.has_key(string[l].upper()): glCallList(lists[string[l].upper()])
            else:  glCallList(lists[" "])
            glPopMatrix()
            
            glPushMatrix()
            glTranslate(0,0,0)
            glColor(colours[col])
            glLineWidth(0.5)
            if lists.has_key(string[l].upper()): glCallList(lists[string[l].upper()])
            else:  glCallList(lists[" "])
            glPopMatrix()
            glTranslate(14,0,0)

        glPopMatrix()


    def __init__(self):


        self.lock=False
        self.mbutton=-1
        self.mstate=-1


        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(640,480)
        glutCreateWindow(name)

        glClearColor(0.,0.,0.,1.)
        glShadeModel(GL_FLAT)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)

        lightZeroPosition = [1,0,0]   #[10.,4.,10.,1.]
        lightZeroColor = [1,1,1] # [0.8,1.0,0.8,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)

        lightZeroPosition = [-1,0,0]   #[10.,4.,10.,1.]
        #lightZeroColor = [1,1,1] # [0.8,1.0,0.8,1.0] #green tinged
        glLightfv(GL_LIGHT1, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT1, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT1)

        lightZeroPosition = [0,0,1]   #[10.,4.,10.,1.]
        #lightZeroColor = [1,1,1] # [0.8,1.0,0.8,1.0] #green tinged
        glLightfv(GL_LIGHT2, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT2, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT2, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT2, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT2)

        '''
        lightZeroPosition = [0,0,-1]   #[10.,4.,10.,1.]
        #lightZeroColor = [1,1,1] # [0.8,1.0,0.8,1.0] #green tinged
        glLightfv(GL_LIGHT3, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT3, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT3, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT3, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT3)
        '''



        glutReshapeFunc(self.reshape)
        glutMotionFunc(self.mousedrag)
        glutMouseFunc(self.mouse)
        glutSpecialFunc(self.keydownevent)
        glutSpecialUpFunc(self.keyupevent)
        glutKeyboardFunc(self.keydownevent)
        glutKeyboardUpFunc(self.keyupevent)

        glutPassiveMotionFunc(self.mousedrag)

        glutDisplayFunc(self.display)
        #glutIdleFunc(self.display)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(60.0,self.WIDTH/self.HEIGHT,1.,50.)
        glMatrixMode(GL_MODELVIEW)
        #glPushMatrix()

        self.reshape(640,480)
        self.animate(FPS=15)

        MakeLists()
        glutMainLoop()


        return


    def reshape(self,width,height):
        print "hello reshape "+str((width,height))
        self.HEIGHT=float(height)
        self.WIDTH=float(width)
        glViewport(0,0,int(self.WIDTH),int(self.HEIGHT)        )
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0,self.WIDTH/self.HEIGHT,1.,50.)
        glMatrixMode(GL_MODELVIEW)
        #glPushMatrix()
        glLoadIdentity()



    def keydownevent(self,c,x,y):


        mod = glutGetModifiers()

        self.joystick.isControl=False
        self.joystick.isAlt=False
        self.joystick.isShift=False

        if mod&GLUT_ACTIVE_CTRL==GLUT_ACTIVE_CTRL: self.joystick.isControl=True
        if mod&GLUT_ACTIVE_ALT==GLUT_ACTIVE_ALT: self.joystick.isAlt=True
        if mod&GLUT_ACTIVE_SHIFT==GLUT_ACTIVE_SHIFT: self.joystick.isShift=True

        #print str(c)
        if type(c) is str: self.joystick.register(c.lower(),True)
        else: self.joystick.register(c,True)

        #self.logic()
        glutPostRedisplay()

    def keyupevent(self,c,x,y):

        mod = glutGetModifiers()

        self.joystick.isControl=False
        self.joystick.isAlt=False
        self.joystick.isShift=False

        if mod&GLUT_ACTIVE_CTRL==GLUT_ACTIVE_CTRL: self.joystick.isControl=True
        if mod&GLUT_ACTIVE_CTRL==GLUT_ACTIVE_ALT: self.joystick.isAlt=True
        if mod&GLUT_ACTIVE_CTRL==GLUT_ACTIVE_SHIFT: self.joystick.isShift=True

        if type(c) is str: self.joystick.register(c.lower(),False)
        else: self.joystick.register(c,False)

        self.logic()
        glutPostRedisplay()

    def mousedrag(self,x,y):
        #print ((x,y))
        if self.mbutton==0 and self.mstate==0:
            self.xRot+=(self.mPos[0]-x)*self.speed
            self.yRot+=(self.mPos[1]-y)*self.speed

        if self.mbutton==1 and self.mstate==0:
            self.zoom+=(self.mPos[0]-x)*self.speed
            if self.zoom<5: self.zoom=5

        self.mPos=[x,y]
        #print str(x)+"-"+str(y)+"  "+str(self.mbutton)+"-"+str(self.mstate)

    def mouse(self,button,state,x,y):
        #print ((button,state,x,y))
        #print "button"+str(button)
        #print "state"+str(state)
        self.mPos=[x,y]
        self.mbutton=button
        self.mstate=state



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
        #self.yRot+=0.5
        #self.xRot+=0.5


        glutSwapBuffers()
        #return


"""
Do this because if it gets put through pydoc or imported its automatically executed
"""
if __name__ == '__main__': Thing()
