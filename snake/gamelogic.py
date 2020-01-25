class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Cell(Point):
    def __init__(self, x, y, speedX=0, speedY=0):
        super().__init__(x,y)
        self.speedX = speedX
        self.speedY = speedY

    def update(self):
        self.x += self.speedX
        self.y += self.speedY
