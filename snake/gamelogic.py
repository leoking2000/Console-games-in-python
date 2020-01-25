class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Cell(Point):

    def __init__(self, x, y, speed):
        super().__init__(x,y)
        self.speed = speed
        self.speedX = self.speed
        self.speedY = 0

    def update(self):
        self.x += self.speedX
        self.y += self.speedY

    def go_down(self):
        if self.speedY == 0:
            self.speedY = self.speed
            self.speedX = 0
    def go_up(self):
        if self.speedY == 0:
            self.speedY = -self.speed
            self.speedX = 0
    def go_right(self):
        if self.speedX == 0:
            self.speedX = self.speed
            self.speedY = 0
    def go_left(self):
        if self.speedX == 0:
            self.speedX = -self.speed
            self.speedY = 0
