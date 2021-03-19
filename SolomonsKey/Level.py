
from OpenGL.GLUT import glutSwapBuffers, glutSolidCube, glutKeyboardFunc, glutKeyboardUpFunc, glutDisplayFunc, \
glutIdleFunc, glutInit, glutInitDisplayMode, glutCreateWindow, glutMainLoop, \
glutInitWindowSize, glutIgnoreKeyRepeat, glutSpecialFunc, glutReshapeFunc, glutSpecialUpFunc, glutTimerFunc, \
glutPostRedisplay, GLUT_DOUBLE, GLUT_RGBA, GLUT_DEPTH, glutWireCube

from OpenGL.GLU import gluPerspective, gluLookAt

from OpenGL.GL import GL_PROJECTION,  GL_MODELVIEW, GL_DEPTH_TEST, GL_SMOOTH, \
GL_CULL_FACE, GL_LIGHTING, GL_POSITION, GL_LIGHT0, glLoadIdentity, \
glMatrixMode, glPushMatrix, glBlendFunc, glEnable, glClearColor, glShadeModel, glLightfv, \
GL_LINEAR_ATTENUATION, GL_CONSTANT_ATTENUATION, GL_DIFFUSE, \
glMaterialfv, glTranslate, glPopMatrix, glScale, GL_LIGHT1, GL_FRONT, glLightf, \
glViewport, GL_SRC_ALPHA, GL_ONE, GL_DEPTH_BUFFER_BIT, glClear, GL_COLOR_BUFFER_BIT

from Sprite import Sprite
from Models import lists, colours

'''
3 - solid s
2 - block b
6 - start @
7 - door d
8 - key k
1 - baddy??
5 - flying horizontal 
4 - bell 4
9 - flame 
TODO multiple layers
'''

def generateLevel(num):
    if num==0:
        return Level([
            "33333333333333333",
            "30000000000000003",
            "30000000700000003",
            "30500000000000003",
            "30000032223000003",
            "30000029492000003",
            "30000032223000003",
            "30000002220000003",
            "30009000000090003",
            "30003230003230003",
            "30002622222820003",
            "30003230003230003",
            "30000000000000003",
            "33333333333333333"])

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
                if c=="6":
                    self.solomon_start=[cc,rr]
                    self.grid[rr][cc]="."
                    #self.solomon.A_wandswish.callback=self.block_swap
                elif c=="7":
                    self.door=[cc,rr]
                    self.grid[rr][cc]="0"
                elif c=="8":
                    ns=Sprite(cc,rr+0.5)
                    ns.setDrawFuncToList(lists["green_key"])
                    #ns.collision_action=self.key_detected_something_test
                    self.sprites.append(ns)
                    self.grid[rr][cc]="0"
                elif not c in ["3","2","1"]:
                    self.grid[rr][cc]="0"

                cc+=1

            rr+=1
    
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
                    
                    if c in ["2","3"]:
                        if c!="3": color = [0.3,0.3,1.0,1.0]
                        else: color = [1.0,1.0,0.0,1.0]
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

                    elif c in ["1"]: ##i.e changed to half a block because recieved bash
                        color = [0.3,0.3,1.0,1.0]
                        glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
                        glCallList(lists["broken brick"])

                    glPopMatrix()

                cc+=1

            rr+=1

        #glPushMatrix()