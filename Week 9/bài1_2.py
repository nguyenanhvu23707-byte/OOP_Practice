import math

class PointTest:
    def main(self):
        diema=(3,4)
        print(diema)
        
        xb=float(input("hoành độ điểm b: "))
        yb=float(input("tung độ điểm b: "))
        print("b= ",(xb, yb))
        
        c=(-xb, -yb)
        print(c)
        
        distance_bo=math.sqrt(xb**2+yb**2)
        print(f"khoảng cách từ b đến gốc:{distance_bo}")
        
        distance_ab=math.sqrt((xb-3)**2+(yb-4)**2)
        print(f"khoảng cách từ a đến b:{distance_ab}")
        
if __name__ == "__main__":
    snu=PointTest()
    snu.main()
