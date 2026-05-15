class TuLanhTest:
    def testCase(self):
        def parse(line):
            nh, ms, nsx, tk, dt, gia = line.split("|")
            return TuLanh(nh, ms, nsx, tk == "True", int(dt), int(gia))

        tu1 = parse(input().strip())
        tu2 = parse(input().strip())

        SEP = "= = = = = = = ="

        print(SEP)
        tu1.hienThi()
        tu2.hienThi()
