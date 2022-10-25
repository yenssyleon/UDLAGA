from Sky import Sky
from Ship import Ship
import pygame
import random

class Game:
    
    def __init__(self):
        
        self.myShip=Ship()
        self.width=600
        self.height=400       
        self.mySky=Sky(self.width, self.height, 50)        
        self.screen= pygame.display.set_mode((self.width, self.height))
        self.clock=pygame.time.Clock()
        self.fps=60
        #Cargar la hoja de imágenes        
        self.sprites= pygame.image.load("sprites.png")        
        self.shipsprite= pygame.Surface((64,64)).convert()
        self.shipsprite.blit(self.sprites,(0,0), (252,436, 64,64)) 
            
# -------------------------------------------------------------------------------        
        
    def run(self):
        
        pygame.init()
        
        control=True
        while control:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    return True
                    
            self.screen.fill((0,0,0))
            
            #Show the Sky
            
            for star in self.mySky.stars:
                r=random.randint(0,255)
                g=random.randint(0,255)
                b=random.randint(0,255)
                pygame.draw.circle(self.screen,(r,g,b), star, 1)
            
            self.mySky.move()
            
            self.myShip.move(self.checkKeys())
            
            x=self.myShip.x
            y=330
            self.screen.blit(self.shipsprite, (x,y))
            
            pygame.display.flip()
            
            self.clock.tick(self.fps)
            
    def checkKeys(self):
            
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: return "RIGHT"
        elif keys[pygame.K_LEFT]: return "LEFT"     
                    

myGame=Game()
myGame.run()
        
