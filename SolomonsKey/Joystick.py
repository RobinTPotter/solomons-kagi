class Joystick:
    
    up,down,left,right,fire="","","","",""
    keys_last = None
    callback_up=None
    callback_down=None
    
    def __init__(self,up=b'q',down=b'a',left=b'o',right=b'p',fire=b'm'):
        self.up=up
        self.down=down
        self.left=left
        self.right=right
        self.fire=fire
        
    def isUp(self,keys):
        self.keys_last=keys
        if self.up in keys: return keys[self.up]
        else: return False
         
    def isDown(self,keys):
        self.keys_last=keys
        if self.down in keys: return keys[self.down]
        else: return False
         
    def isLeft(self,keys):
        self.keys_last=keys
        if self.left in keys: return keys[self.left]
        else: return False
         
    def isRight(self,keys):
        self.keys_last=keys
        if self.right in keys: return keys[self.right]
        else: return False
         
    def isFire(self,keys):
        self.keys_last=keys        
        if self.fire in keys:
            return keys[self.fire]
        else: return False
        
    def __repr__(self):
        if self.keys_last is None: return "No values yet"
        return 'Up: {}, Down: {}, Left: {}, Right: {}, Fire: {}'.format(self.isUp(self.keys_last),self.isDown(self.keys_last),self.isLeft(self.keys_last),self.isRight(self.keys_last),self.isFire(self.keys_last))
         