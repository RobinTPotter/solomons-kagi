from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sqrt

DIVS=2

class Letters():
    
    lists = {}
       
     
    def __init__(self):
        self.MakeLists()
        
    def SubDivLineString(self,list_of_vectors,total_sub_divs=DIVS):
        final_list_of_vectors=[]
        divs=0
        while divs<total_sub_divs:
            divs+=1
            print (divs)
            i=1
            while i<len(list_of_vectors):
                ave=(0.5*(list_of_vectors[i][0]+list_of_vectors[i-1][0]),0.5*(list_of_vectors[i][1]+list_of_vectors[i-1][1]),)
                list_of_vectors.insert(i,ave)       
                i+=2
            
        list_of_vectors 
        #print "divs:"
        #print divs
        #print "len list_of_vectors"
        #print str(len(list_of_vectors))
        lln=0
        for ll in list_of_vectors:
            flag=""
            #print str(lln *  (0.5**total_sub_divs))
            if lln *  (0.5**total_sub_divs)==int(lln *  (0.5**total_sub_divs)): flag="*"
            #print str(lln)+": "+flag+str(ll)
            if flag=="" or lln==0 or lln==len(list_of_vectors)-1: final_list_of_vectors.append(ll)
            lln+=1
        
        return final_list_of_vectors
    
    def DoLetter(self,letter,vector_list):
    
        self.lists[letter] = glGenLists(1) 
        list=self.SubDivLineString(vector_list)    
        glNewList(self.lists[letter],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)    
        for li in list:
            glVertex2f(li[0],li[1])     
        
        glEnd()
        glEndList()
    
    def MakeLists(self):
        
        self.lists[" "] = glGenLists(1) 
        glNewList(self.lists[" "],GL_COMPILE) 
        glEndList()
        
        self.lists["."] = glGenLists(1) 
        glNewList(self.lists["."],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(4.0, 1.0)
        glVertex2f(6.0, 1.0)
        glVertex2f(6.0, 3.0)
        glVertex2f(4.0, 3.0)
        glVertex2f(4.0, 1.0)    
        glEnd()
        glEndList()
        
        self.lists[","] = glGenLists(1) 
        glNewList(self.lists[","],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(4.0, 1.0)
        glVertex2f(5.0, 1.0)
        glVertex2f(5.0, -1.0)
        glVertex2f(6.0, 1.0)
        glVertex2f(6.0, 3.0)
        glVertex2f(4.0, 3.0)
        glVertex2f(4.0, 1.0)    
        glEnd()
        glEndList()
        
        self.lists[":"] = glGenLists(1) 
        glNewList(self.lists[":"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(4.0, 1.0)
        glVertex2f(6.0, 1.0)
        glVertex2f(6.0, 3.0)
        glVertex2f(4.0, 3.0)
        glVertex2f(4.0, 1.0)    
        glEnd()
        glBegin(GL_LINE_STRIP)
        glVertex2f(4.0, 4.0)
        glVertex2f(6.0, 4.0)
        glVertex2f(6.0, 6.0)
        glVertex2f(4.0, 6.0)
        glVertex2f(4.0, 4.0)    
        glEnd()
        glEndList()
        
        self.lists["-"] = glGenLists(1) 
        glNewList(self.lists["-"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(1.0, 5.0)
        glVertex2f(9.0, 5.0)    
        glEnd()
        glEndList()
        
        self.lists["/"] = glGenLists(1) 
        glNewList(self.lists["/"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10, 10)
        glVertex2f(0.0, 0.0)    
        glEnd()
        glEndList()
        
        self.lists["*"] = glGenLists(1) 
        glNewList(self.lists["*"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(5.0, 5.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(10.0, 5.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(5.0, 0.0)
        glVertex2f(5.0, 10.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(0.0, 10.0)
        glEnd()
        glEndList()
        
        self.DoLetter("A",[(0.0, 0.0),(0.0, 10.0),(10.0, 10.0),(10.0, 0.0),(10.0, 5.0),(0.0, 5.0)])
        self.DoLetter("B",[(0.0, 0.0)  ,(0.0, 10.0)    ,(8.0, 10.0)    ,(8.0, 5.0)    ,(0.0, 5.0)    ,(10.0, 5.0)    ,(10.0, 0.0)    ,(0.0, 0.0)])
        self.DoLetter("C",[(10.0, 0.0)    ,(0.0, 0.0)    ,(0.0, 10.0)    ,(10.0, 10.0)])    
        self.DoLetter("D",[(0.0, 0.0),   (0.0, 10.0),    (8.0, 10.0),    (10.0, 8.0),    (10.0, 2.0),    (8.0, 0.0),    (0.0, 0.0) ])
        
        self.lists["E"] = glGenLists(1) 
        glNewList(self.lists["E"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 0.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(8.0, 5.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["F"] = glGenLists(1) 
        glNewList(self.lists["F"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(8.0, 5.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["G"] = glGenLists(1) 
        glNewList(self.lists["G"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(5.0, 5.0)
        glVertex2f(10.0, 5.0)
        glVertex2f(8.0, 5.0)
        glVertex2f(8.0, 0.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(8.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["H"] = glGenLists(1) 
        glNewList(self.lists["H"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(10.0, 5.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(10.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["I"] = glGenLists(1) 
        glNewList(self.lists["I"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(5.0, 0.0)
        glVertex2f(5.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["J"] = glGenLists(1) 
        glNewList(self.lists["J"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 2.0)
        glVertex2f(2.0, 0.0)
        glVertex2f(3.0, 0.0)
        glVertex2f(5.0, 2.0)
        glVertex2f(5.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["K"] = glGenLists(1) 
        glNewList(self.lists["K"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(10.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["L"] = glGenLists(1) 
        glNewList(self.lists["L"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 10.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(10.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["M"] = glGenLists(1) 
        glNewList(self.lists["M"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(10.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["N"] = glGenLists(1) 
        glNewList(self.lists["N"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(10.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["O"] = glGenLists(1) 
        glNewList(self.lists["O"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(0.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["P"] = glGenLists(1) 
        glNewList(self.lists["P"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(10.0, 5.0)
        glVertex2f(0.0, 5.0) 
        glEnd()
        glEndList()
        
        self.lists["Q"] = glGenLists(1) 
        glNewList(self.lists["Q"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(0.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["R"] = glGenLists(1) 
        glNewList(self.lists["R"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(10.0, 5.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(10.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["S"] = glGenLists(1) 
        glNewList(self.lists["S"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(10.0, 5.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["T"] = glGenLists(1) 
        glNewList(self.lists["T"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(5.0, 10.0)
        glVertex2f(5.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["U"] = glGenLists(1) 
        glNewList(self.lists["U"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 10.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["V"] = glGenLists(1) 
        glNewList(self.lists["V"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 10.0)
        glVertex2f(5.0, 0.0)
        glVertex2f(0.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["W"] = glGenLists(1) 
        glNewList(self.lists["W"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 10.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(10.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["X"] = glGenLists(1) 
        glNewList(self.lists["X"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["Y"] = glGenLists(1) 
        glNewList(self.lists["Y"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 10.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(5.0, 5.0)
        glVertex2f(5.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["Z"] = glGenLists(1) 
        glNewList(self.lists["Z"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(10.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["0"] = glGenLists(1) 
        glNewList(self.lists["0"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(10.0, 10.0) 
        glEnd()
        glEndList()
        
        self.lists["1"] = glGenLists(1) 
        glNewList(self.lists["1"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 0.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(5.0, 0.0)
        glVertex2f(5.0, 10.0)
        glVertex2f(0.0, 5.0) 
        glEnd()
        glEndList()
        
        self.lists["2"] = glGenLists(1) 
        glNewList(self.lists["2"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 0.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(7.0, 5.0)
        glVertex2f(10.0, 8.0)
        glVertex2f(8.0, 10.0)
        glVertex2f(2.0, 10.0)
        glVertex2f(0.0, 8.0) 
        glEnd()
        glEndList()
        
        self.lists["3"] = glGenLists(1) 
        glNewList(self.lists["3"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(3.0, 5.0)
        glVertex2f(8.0, 5.0)
        glVertex2f(10.0, 3.0)
        glVertex2f(10.0, 2.0)
        glVertex2f(8.0, 0.0)
        glVertex2f(2.0, 0.0)
        glVertex2f(0.0, 2.0) 
        glEnd()
        glEndList()
        
        self.lists["4"] = glGenLists(1) 
        glNewList(self.lists["4"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(8.0, 0.0)
        glVertex2f(8.0, 10.0)
        glVertex2f(0.0, 2.0)
        glVertex2f(10.0, 2.0) 
        glEnd()
        glEndList()
        
        self.lists["5"] = glGenLists(1) 
        glNewList(self.lists["5"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(8.0, 5.0)
        glVertex2f(10.0, 2.0)
        glVertex2f(8.0, 0.0)
        glVertex2f(2.0, 0.0)
        glVertex2f(0.0, 2.0) 
        glEnd()
        glEndList()
        
        self.lists["6"] = glGenLists(1) 
        glNewList(self.lists["6"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(10.0, 5.0)
        glVertex2f(0.0, 5.0) 
        glEnd()
        glEndList()
        
        self.lists["7"] = glGenLists(1) 
        glNewList(self.lists["7"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(2.0, 0.0) 
        glEnd()
        glEndList()
        
        self.lists["8"] = glGenLists(1) 
        glNewList(self.lists["8"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(10.0, 0.0)
        glVertex2f(0.0, 0.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(10.0, 5.0)
        glVertex2f(0.0, 5.0) 
        glEnd()
        glEndList()
        
        self.lists["9"] = glGenLists(1) 
        glNewList(self.lists["9"],GL_COMPILE) 
        glBegin(GL_LINE_STRIP)
        glVertex2f(0.0, 0.0)
        glVertex2f(10.0, 0.0)
        glVertex2f(10.0, 10.0)
        glVertex2f(0.0, 10.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(10.0, 5.0) 
        glEnd()
        glEndList()
      
    def drawString(self,string,col=[1.0,1.0,0.0,1.0]):
        glPushMatrix()
        glDisable(GL_LIGHTING)
        
        for l in range(0,len(string)):
            
            if string[l].upper()=="#":
                if len(string[l:])>2:
                    if string[l:l+3]=="###": break
            
            glPushMatrix()
            glTranslate(0,0,0.5)
            glColor([0.0,0.0,0.0,1.0])
            glLineWidth(4.0)
            if string[l].upper() in self.lists: glCallList(self.lists[string[l].upper()])
            else:  glCallList(self.lists[" "])
            glPopMatrix()
            
            glPushMatrix()
            glTranslate(0,0,0)
            glColor(col)
            glLineWidth(1.5)
            if string[l].upper() in self.lists: glCallList(self.lists[string[l].upper()])
            else:  glCallList(self.lists[" "])
            glPopMatrix()
            glTranslate(14,0,0)

        
        glEnable(GL_LIGHTING)
        glPopMatrix()
