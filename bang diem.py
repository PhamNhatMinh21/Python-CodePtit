from decimal import ROUND_HALF_UP, Decimal
class HocSinh:
    def __init__(self, ma, ten, diem):
        self.ma = 'HS{0:0>2}'.format(ma)
        self.ten = ten
        self.diem = diem
    def get_dtb(self):
        diem = self.diem
        dtb = (diem[0] * 2 + diem[1] * 2 + sum(diem[2:])) / 12
        return dtb.quantize(Decimal('0.1'), ROUND_HALF_UP)
    def get_ma(self):
        return self.ma
    def __str__(self):
        dtb = self.get_dtb()
        if dtb >= 9:
            loai = 'XUAT SAC'
        elif dtb >= 8:
            loai = 'GIOI'
        elif dtb >= 7:
            loai = 'KHA'
        elif dtb >= 5:
            loai = 'TB'
        else:
            loai = 'YEU'
        return f'{self.ma} {self.ten} {dtb} {loai}'
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        ten = input()
        diem = list(map(Decimal, input().split()))
        a.append(HocSinh(i+1, ten, diem))
    a = sorted(a, key = lambda x: (-x.get_dtb(), x.get_ma()))
    for x in a:
        print(x)
