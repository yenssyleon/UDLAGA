"""
BULLET 
---------------
x
y
Velocity
---------------
move()    
"""
class Ship:
    def __init__(self):
        self.direction="RIGHT"
        
    def updateCoordinates(self, x, y):
            
        if self.direction=="LEFT":
            x=x-1
            
        elif self.direction=="RIGHT":
            x=x+1
            
        return(x,y)
    
    def move(self):
        
        (x,y)=self.updateCoordinates(x,y)
        (x,y)=self.screen.blit
