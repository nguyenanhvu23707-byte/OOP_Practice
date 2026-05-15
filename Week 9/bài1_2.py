import math

class Point:
    # Hàm khởi tạo mặc định
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    # Nhập tọa độ
    def read(self):
        self.__x, self.__y = map(int, input().split())

    # Hiển thị tọa độ
    def print(self):
        print(f"({self.__x}, {self.__y})")

    # Dời điểm
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Lấy hoành độ
    def getX(self):
        return self.__x

    # Lấy tung độ
    def getY(self):
        return self.__y

    # Khoảng cách đến gốc tọa độ hoặc điểm khác
    def distance(self, P=None):
        if P is None:
            return math.sqrt(self.__x ** 2 + self.__y ** 2)
        else:
            dx = self.__x - P.__x
            dy = self.__y - P.__y
            return math.sqrt(dx ** 2 + dy ** 2)
