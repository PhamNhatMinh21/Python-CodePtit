from math import *
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def __add__(self, x):
        a = self.tu * x.mau + self.mau * x.tu
        b = self.mau * x.mau
        self.tu = a
        self.mau = b
        return PhanSo(a, b)
    def xuly(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
    def __str__(self):
        return(f'{self.tu}/{self.mau}')
a = list(map(int, input().split()))
x = PhanSo(a[0], a[1])
y = PhanSo(a[2], a[3])
s = x + y
s.xuly()
print(s)
