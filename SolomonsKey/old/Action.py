class Action:
    
    tick=0
    min=-5.0
    max=5.0
    value=0.0
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
                if self.callback is not None:
                    self.callback.__call__()  #for pylint                   
                    #print(dir(self))
                    print("callback called")
                    self.kick()
                    
                     
        if not self.value==None: return self.value
        else: return 0.0
        
#defines a set of actions to be done as one.
class ActionGroup:

    actions={}

    def __init__(self):
        self.actions={}
        
    def append(self,action_name,action):
        if action_name in self.actions:
            raise Exception("action defined "+action_name)
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
        if action_name in self.actions:
            #print "action "+str(action_name)+" "+str(self.actions[action_name].value)
            return self.actions[action_name].value
        else:
            raise Exception("no such action registered "+action_name)
            
    def action(self,action_name):
        if action_name in self.actions:
            return self.actions[action_name]
        else:
            raise Exception("no such action registered "+action_name)
            
