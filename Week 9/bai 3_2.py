import math

class Point:
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    def read(self):
        x, y = map(int, input().split())
        self.__x, self.__y = x, y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setXY(self, x, y):
        self.__x, self.__y = x, y

    def distance(self, P=None):
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            return math.sqrt((self.__x - P.getX())**2 + (self.__y - P.getY())**2)


class ColorPoint(Point):
    def __init__(self, *args):
        if len(args) == 0: 
            super().__init__()
            self.__color = "xanh"
        elif len(args) == 3: 
            super().__init__(args[0], args[1])
            self.__color = args[2]
        elif len(args) == 1 and isinstance(args[0], ColorPoint):  
            super().__init__(args[0].getX(), args[0].getY())
            self.__color = args[0].__color

    def read(self):
        x, y, color = input().split()
        super().setXY(int(x), int(y))
        self.__color = color

    def __str__(self):
        return f"({self.getX()}, {self.getY()}): {self.__color}"

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color


class ColorPointTest:
    @staticmethod
    def testCase():

        cp_default = ColorPoint()
        print(cp_default)

        cp_read = ColorPoint()
        cp_read.read()
        print(cp_read)

        cp_copy = ColorPoint(cp_read)

        cp_read.move(5, 5)
        print(cp_read)

        print(cp_copy)
