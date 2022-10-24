"""
SHIP
---------------
x ----> Cambia
y
Bullet
---------------
move()    
"""
class Ship:
    def __init__(self):
        
        self.direction="RIGHT"
        self.x=300
        self.y=200
               
    
    def move(self, direction):
        
        if direction=="LEFT":
            self.x==1
            
        elif direction=="RIGHT":
            self.x+=1
            
