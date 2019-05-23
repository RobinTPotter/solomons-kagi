from OpenGL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import sqrt

lists={}
DIVS=2


def SubDivLineString(list_of_vectors,total_sub_divs=DIVS):

    final_list_of_vectors=[]

    divs=0

    while divs<total_sub_divs:
        divs+=1
        print divs
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




def DoLetter(letter,vector_list):

    print "doing "+letter
    lists[letter] = glGenLists(1) 
    list=SubDivLineString(vector_list)    
    glNewList(lists[letter],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)    
    for li in list:
        glVertex2f(li[0],li[1])     
    
    glEnd()
    glEndList()


def MakeLists():


    lists[" "] = glGenLists(1) 
    glNewList(lists[" "],GL_COMPILE) 
    glEndList()
    

    lists["."] = glGenLists(1) 
    glNewList(lists["."],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(4.0, 1.0)
    glVertex2f(6.0, 1.0)
    glVertex2f(6.0, 3.0)
    glVertex2f(4.0, 3.0)
    glVertex2f(4.0, 1.0)    
    glEnd()
    glEndList()



    lists["-"] = glGenLists(1) 
    glNewList(lists["-"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(1.0, 5.0)
    glVertex2f(9.0, 5.0)    
    glEnd()
    glEndList()




    lists["/"] = glGenLists(1) 
    glNewList(lists["/"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10, 10)
    glVertex2f(0.0, 0.0)    
    glEnd()
    glEndList()



    lists["*"] = glGenLists(1) 
    glNewList(lists["*"],GL_COMPILE) 
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


    DoLetter("A",[(0.0, 0.0),(0.0, 10.0),(10.0, 10.0),(10.0, 0.0),(10.0, 5.0),(0.0, 5.0)])
    DoLetter("B",[(0.0, 0.0)  ,(0.0, 10.0)    ,(8.0, 10.0)    ,(8.0, 5.0)    ,(0.0, 5.0)    ,(10.0, 5.0)    ,(10.0, 0.0)    ,(0.0, 0.0)])
    DoLetter("C",[(10.0, 0.0)    ,(0.0, 0.0)    ,(0.0, 10.0)    ,(10.0, 10.0)])    
    DoLetter("D",[(0.0, 0.0),   (0.0, 10.0),    (8.0, 10.0),    (10.0, 8.0),    (10.0, 2.0),    (8.0, 0.0),    (0.0, 0.0) ])
    

    lists["E"] = glGenLists(1) 
    glNewList(lists["E"],GL_COMPILE) 
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


    lists["F"] = glGenLists(1) 
    glNewList(lists["F"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(8.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()


    lists["G"] = glGenLists(1) 
    glNewList(lists["G"],GL_COMPILE) 
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


    lists["H"] = glGenLists(1) 
    glNewList(lists["H"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()


    lists["I"] = glGenLists(1) 
    glNewList(lists["I"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()


    lists["J"] = glGenLists(1) 
    glNewList(lists["J"],GL_COMPILE) 
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


    lists["K"] = glGenLists(1) 
    glNewList(lists["K"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["L"] = glGenLists(1) 
    glNewList(lists["L"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["M"] = glGenLists(1) 
    glNewList(lists["M"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["N"] = glGenLists(1) 
    glNewList(lists["N"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["O"] = glGenLists(1) 
    glNewList(lists["O"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()


    lists["P"] = glGenLists(1) 
    glNewList(lists["P"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["Q"] = glGenLists(1) 
    glNewList(lists["Q"],GL_COMPILE) 
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


    lists["R"] = glGenLists(1) 
    glNewList(lists["R"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["S"] = glGenLists(1) 
    glNewList(lists["S"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["T"] = glGenLists(1) 
    glNewList(lists["T"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(5.0, 0.0) 
    glEnd()
    glEndList()



    lists["U"] = glGenLists(1) 
    glNewList(lists["U"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()



    lists["V"] = glGenLists(1) 
    glNewList(lists["V"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(0.0, 10.0) 
    glEnd()
    glEndList()



    lists["W"] = glGenLists(1) 
    glNewList(lists["W"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["X"] = glGenLists(1) 
    glNewList(lists["X"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0) 
    glEnd()
    glEndList()



    lists["Y"] = glGenLists(1) 
    glNewList(lists["Y"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(5.0, 5.0)
    glVertex2f(5.0, 0.0) 
    glEnd()
    glEndList()



    lists["Z"] = glGenLists(1) 
    glNewList(lists["Z"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0) 
    glEnd()
    glEndList()



    lists["0"] = glGenLists(1) 
    glNewList(lists["0"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0) 
    glEnd()
    glEndList()



    lists["1"] = glGenLists(1) 
    glNewList(lists["1"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 0.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(5.0, 0.0)
    glVertex2f(5.0, 10.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["2"] = glGenLists(1) 
    glNewList(lists["2"],GL_COMPILE) 
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



    lists["3"] = glGenLists(1) 
    glNewList(lists["3"],GL_COMPILE) 
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



    lists["4"] = glGenLists(1) 
    glNewList(lists["4"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(8.0, 0.0)
    glVertex2f(8.0, 10.0)
    glVertex2f(0.0, 2.0)
    glVertex2f(10.0, 2.0) 
    glEnd()
    glEndList()



    lists["5"] = glGenLists(1) 
    glNewList(lists["5"],GL_COMPILE) 
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



    lists["6"] = glGenLists(1) 
    glNewList(lists["6"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 5.0)
    glVertex2f(0.0, 5.0) 
    glEnd()
    glEndList()



    lists["7"] = glGenLists(1) 
    glNewList(lists["7"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 10.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(2.0, 0.0) 
    glEnd()
    glEndList()



    lists["8"] = glGenLists(1) 
    glNewList(lists["8"],GL_COMPILE) 
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



    lists["9"] = glGenLists(1) 
    glNewList(lists["9"],GL_COMPILE) 
    glBegin(GL_LINE_STRIP)
    glVertex2f(0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(10.0, 10.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, 5.0)
    glVertex2f(10.0, 5.0) 
    glEnd()
    glEndList()
  
