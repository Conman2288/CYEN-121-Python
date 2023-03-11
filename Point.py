class Point:
    def __init__(self, x=0, y=0):        
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x=0):
        if (x < -10):
            self._x = -10
        elif (x > 10):
            self._x = 10
        else:
            self._x = x
            
    @x.setter        
    def x(self, y=0):
        if (y < -10):
            self._y = -10
        elif (y > 10):
            self._y = 10
        else:
            self._y = y

    




p1 = Point()
p2 = Point(-50, 50)
print("p1 = ({},{})".format(p1.x, p1.y))
print("p2 = ({},{})".format(p2.x, p2.y))


p1.x = 2
p1.y = 3

print("p1 = ({},{})".format(p1.x, p1.y))
