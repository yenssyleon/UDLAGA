from Ship import Ship


class Bullet:

    def __init__(self):

        self.myShip=Ship()

        self.condition = "FIRED" #Dirección de la nave
        self.ymyBullet=self.myShip.y
    
    
        

    def shoot (self):

        if self.condition == "FIRED": 
            self.ymyBullet -= 5

        elif self.myShip.direction == "STOP": #Si la nave no se mueve no hacer nada
            pass   
    