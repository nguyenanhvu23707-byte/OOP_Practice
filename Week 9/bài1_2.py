class PointTest:
    def testCase(self):
        p1 = Point()
        print(p1)

        p2 = Point()
        p2.read()
        print(p2)

        p2.move(1, 1)
        print(p2)

        print(p2.distance())
