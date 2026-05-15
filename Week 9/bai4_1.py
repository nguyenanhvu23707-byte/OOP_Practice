class TuLanh:
    def __init__(self, nhanhieu, maso, nuocsx, tkdien, dungtich, gia):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien if isinstance(tkdien, bool) else (tkdien == "True")
        self.__dungtich = int(dungtich)
        self.__gia = int(gia)

    def hienThi(self):
        print(f"Nhãn hiệu: {self.__nhanhieu}")
        print(f"Mã số: {self.__maso}")
        print(f"Nước SX: {self.__nuocsx}")
        print(f"T/K điện: {'Có' if self.__tkdien else 'Không'}")
        print(f"Dung tích: {self.__dungtich}L")
        print(f"Giá: {self.__gia}VNĐ")
        print("= = = = = = = =")

    def __str__(self):
        tk = "Có" if self.__tkdien else "Không"
        return (f"Nhãn hiệu: {self.__nhanhieu}\n"
                f"Mã số: {self.__maso}\n"
                f"Nước SX: {self.__nuocsx}\n"
                f"T/K điện: {tk}\n"
                f"Dung tích: {self.__dungtich}L\n"
                f"Giá: {self.__gia}VNĐ")
