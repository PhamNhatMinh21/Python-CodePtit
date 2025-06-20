class KhachHang:
    def __init__(self, ma, ten, cu, moi):
        self.ma = 'KH{0:0>2}'.format(ma)
        self.ten = ten
        self.cu = cu
        self.moi = moi
    def luong_nuoc(self):
        return self.moi - self.cu
    def check(self):
        x = self.luong_nuoc()
        if 0 <= x <= 50:
            return x * 100 + (x * 100 * 0.02)
        elif 51 <= x <= 100:
            return (50 * 100 + (x - 50) * 150) + ((50 * 100 + (x - 50) * 150) * 0.03)
        else:
            return (50 * 100 + 50 * 150 + (x - 100) * 200) + ((50 * 100 + 50 * 150 + (x - 100) * 200) * 0.05)
    def __str__(self):
        return f'{self.ma} {self.ten} {round(self.check())}'
n = int(input())
a = []
for i in range(n):
    ten = input()
    cu = int(input())
    moi = int(input())
    res = KhachHang(i+1, ten, cu, moi)
    a.append(res)
a = sorted(a, key = lambda x : -x.check())
for x in a:
    print(x)