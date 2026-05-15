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

    def distance(self, P=None):
        if P is None:
            return math.sqrt(self.__x**2 + self.__y**2)
        else:
            return math.sqrt((self.__x - P.getX())**2 + (self.__y - P.getY())**2)


class LineSegment:
    def __init__(self, *args):
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)
        elif len(args) == 2 and isinstance(args[0], Point) and isinstance(args[1], Point):
            self.__d1, self.__d2 = args[0], args[1]
        elif len(args) == 4:  
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])
        elif len(args) == 1 and isinstance(args[0], LineSegment):  # copy constructor
            self.__d1 = Point(args[0].__d1.getX(), args[0].__d1.getY())
            self.__d2 = Point(args[0].__d2.getX(), args[0].__d2.getY())

    def read(self):
        x1, y1, x2, y2 = map(int, input().split())
        self.__d1 = Point(x1, y1)
        self.__d2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.__d1.getX()}, {self.__d1.getY()}); ({self.__d2.getX()}, {self.__d2.getY()})]"

    def move(self, dx, dy):
        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    def length(self):
        return self.__d1.distance(self.__d2)

    def angle(self):
        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()
        ang = round(math.degrees(math.atan2(dy, dx)))
        return (ang + 360) % 360
