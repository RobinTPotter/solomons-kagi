from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


colours={}

colours["gold"]=[1.0,0.9,0.0,1.0]
colours["black"]=[0.0,0.0,0.0,1.0]
colours["red"]=[1.0,0.0,0.0,1.0]
colours["green"]=[0.0,1.0,0.0,1.0]
colours["blue"]=[0.0,0.0,1.0,1.0]
colours["yellow"]=[1.0,1.0,0.0,1.0]
colours["cyan"]=[0.0,1.0,1.0,1.0]
colours["pink"]=[1.0,0.0,1.0,1.0]
colours["white"]=[1.0,1.0,1.0,1.0]    
colours["gold"]=[1.0,0.9,0.0,1.0]
colours["hat"]=[0.105,0.097,0.207,1.0]
colours["body"]=[0.193,0.05,0.0012071,1.0]
colours["arm"]=[0.34,0.014,0.0,1.0]
colours["shoe"]=[0.096,0.3,1.0]
colours["wand"]=[0,0,0,1.0]
colours["wandtip"]=[1,1,1,1.0]



lists={}

def MakeLists():

    #global lists
    lists["broken brick"] = glGenLists(1)
    print  ("about to compile list"+str(lists["broken brick"]))
    glNewList(lists["broken brick"],GL_COMPILE)

    glPushMatrix()
    glTranslate(0.25,0.25,0.25)
    glScale(0.4,0.44,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.25,0.25,0.25)
    glScale(0.44,0.44,0.34)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.25,-0.25,0.25)
    glScale(0.44,0.44,0.34)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.25,-0.25,0.25)
    glScale(0.44,0.44,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.25,0.25,-0.25)
    glScale(0.34,0.34,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.25,0.25,-0.25)
    glScale(0.44,0.34,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(0.25,-0.25,-0.25)
    glScale(0.24,0.44,0.44)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslate(-0.25,-0.25,-0.25)
    glScale(0.24,0.5,0.44)
    glutSolidCube(1)
    glPopMatrix()
    
    glEndList()

  
  
    lists["blue_key"] = glGenLists(1) 
    glNewList(lists["blue_key"],GL_COMPILE) 
  
      
    q=gluNewQuadric()

    glPushMatrix()


    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["blue"])


    #blue edge 1
    glPushMatrix()
    glScale(0.25,0.25,0.01)
    glTranslate(0.7,-0.75,7.5)
    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,1,1,1,10,1)  
    glTranslate(0,0,1)  
    gluDisk(q, 0.0, 1, 10, 1)  
    #glTranslate(0,0,-1)  
    #glRotate(180,1,0,0)
    #gluDisk(q, 0.0,1, 10, 1) 
    glPopMatrix()




    #blue edge 2
    glPushMatrix()
    glScale(0.25,0.25,0.01)
    glTranslate(0.7,-0.75,-9.5)
    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,1,1,1,10,1)  
    glTranslate(0,0,1)  
    #gluDisk(q, 0.0, 1, 10, 1) 
    glTranslate(0,0,-1)  
    glRotate(180,1,0,0)
    gluDisk(q, 0.0,1, 10, 1)    
    glPopMatrix()





    glPushMatrix()
    glTranslate(0.17,-0.17,-0.013)
    glRotate(45,1,0,0)
    glRotate(45,0,1,0)
    glutSolidCube(0.2)
    glPopMatrix()



    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["gold"])

    glPushMatrix()


    glScale(0.35,0.35,0.15)
    glTranslate(0.5,-0.55,-0.5)

    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,1,1,1,10,1)  

    glTranslate(0,0,1)  
    gluDisk(q, 0.0, 1, 10, 1)   

    glTranslate(0,0,-1)  
    glRotate(180,1,0,0)
    gluDisk(q, 0.0,1, 10, 1) 

    glPopMatrix()






    glPushMatrix()
    glRotatef(90,-1,0,0) 
    glRotatef(-45,0,1,0) 

    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,0.15,0.15,0.5,10,1)  

    glTranslate(0,0,0.5)  
    gluDisk(q, 0.0, 0.15, 10, 1)  

    glTranslate(0,0,-0.5)  
    glRotate(180,1,0,0)
    gluDisk(q, 0.0, 0.15, 10, 1)  
            
    glPushMatrix()
    glTranslate(-0.20,0,0)
    glTranslate(0,0,-0.4)
    glutSolidCube(0.1)
    glPopMatrix()
        
    glPushMatrix()
    glTranslate(-0.20,0,0)
    glTranslate(0,0,-0.2)
    glutSolidCube(0.1)
    glPopMatrix()

        
    glPopMatrix()


    glPopMatrix()
  
    glEndList()
  
  
  
  
  
      
      
    lists["green_key"] = glGenLists(1)
    glNewList(lists["green_key"],GL_COMPILE)    
      
    glPushMatrix()
    

    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["green"])



    glPushMatrix()
    glScale(.45,.45,0.01)
    glTranslate(0.5,-0.5,5.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glScale(.45,.45,0.01)
    glTranslate(0.5,-0.5,-5.5)
    glutSolidCube(1)
    glPopMatrix()




    glPushMatrix()
    glTranslate(0.25,-0.25,-0.0)
    glRotate(45,1,0,0)
    glRotate(45,0,1,0)
    glutSolidCube(0.15)
    glPopMatrix()




    glMaterialfv(GL_FRONT,GL_DIFFUSE,colours["gold"])

    glPushMatrix()
    glScale(.55,.55,0.1)
    glTranslate(0.4,-0.4,0)
    glutSolidCube(1)
    glPopMatrix()

    q=gluNewQuadric()
    glPushMatrix()
    glRotatef(90,-1,0,0) 
    glRotatef(-45,0,1,0) 

    # q, radius 1, radius 2, length, sub-div, sub div stacks
    gluCylinder(q,0.15,0.15,0.5,10,1)  

    glTranslate(0,0,0.5)  
    gluDisk(q, 0.0, 0.15, 10, 1)   

    glTranslate(0,0,-0.5)  
    glRotate(180,1,0,0)
    gluDisk(q, 0.0, 0.15, 10, 1)  
            
    glPushMatrix()
    glTranslate(-0.20,0,0)
    glTranslate(0,0,-0.4)
    glutSolidCube(0.1)
    glPopMatrix()
        
    glPushMatrix()
    glTranslate(-0.20,0,0)
    glTranslate(0,0,-0.2)
    glutSolidCube(0.1)
    glPopMatrix()

        
    glPopMatrix()


    glPopMatrix()

  
  
    glEndList()
