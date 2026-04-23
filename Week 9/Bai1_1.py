import math

class Point:
    def __init__(self, x=0, y=1):
        self.x= x
        self.y= y

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)
    
    def read(self):
        self.x=int(input("Nhập x: "))
        self.y=int(input("Nhập y: "))
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def distance(self, point):
        d = math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
        return d
diemA=Point(3,4)    
print(diemA)
diemA.move(1,2)
print(diemA)
x=diemA.getX()
y=diemA.getY()
print(x)
print(y)
diem0=Point(0,0)
diemB=Point(5,7)
print(diemA.distance(diemB))
print(diemA.distance(diem0))
