class Joystick:
    
    up,down,left,right,fire="","","","",""

    def __init__(self,up="q",down="a",left="o",right="p",fire="m"):
        self.up=up
        self.down=down
        self.left=left
        self.right=right
        self.fire=fire
        
    def isUp(self,keys):
        if self.up in keys: return keys[self.up]
        else: return False
         
    def isDown(self,keys):
        if self.down in keys: return keys[self.down]
        else: return False
         
    def isLeft(self,keys):
        if self.left in keys: return keys[self.left]
        else: return False
         
    def isRight(self,keys):
        if self.right in keys: return keys[self.right]
        else: return False
         
    def isFire(self,keys):
        if self.fire in keys: return keys[self.fire]
        else: return False
         