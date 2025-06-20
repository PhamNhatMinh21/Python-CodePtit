class HoaDon:
    def __init__(self, ma, ten, luong, don, chiet):
        self.ma = ma
        self.ten = ten
        self.luong = luong
        self.don = don
        self.chiet = chiet
    def check(self):
        return self.don * self.luong - self.chiet
    def __str__(self):
        return f'{self.ma} {self.ten} {self.luong} {self.don} {self.chiet} {self.check()}'
n = int(input())
a = []
for _ in range(n):
    ma = input()
    ten = input()
    luong = int(input())
    don = int(input())
    tong = int(input())
    a.append(HoaDon(ma, ten, luong, don, tong))
a = sorted(a, key = lambda x : -x.check())
for x in a:
    print(x)