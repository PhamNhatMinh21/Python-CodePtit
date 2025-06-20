class SinhVien:
    def __init__(self, ma, ten, diem, dantoc, khuvuc):
        self.ma = 'TS{0:0>2}'.format(ma)
        self.ten = ten 
        self.diem = diem
        self.dantoc = dantoc
        self.khuvuc = khuvuc
    def chuanhoa(self):
        return ' '.join(word.capitalize() for word in self.ten.strip().lower().split())
    def check(self):
        uu_tien = 0.0
        if self.khuvuc == '1':
            uu_tien += 1.5
        elif self.khuvuc == '2':
            uu_tien += 1.0
        if self.dantoc != 'Kinh':
            uu_tien += 1.5
        return self.diem + uu_tien
    def ok(self):
        res = self.check()
        if res >= 20.5:
            return 'Do'
        else:
            return 'Truot'
    def __str__(self):
        return f'{self.ma} {self.chuanhoa()} {self.check():.1f} {self.ok()}'
n = int(input())
a = []
for i in range(n):
    ten = input().strip()
    diem = float(input())
    dantoc = input().strip()
    khuvuc = input().strip()
    td = SinhVien(i+1, ten, diem, dantoc, khuvuc)
    a.append(td)
a = sorted(a, key = lambda x : (-x.check(), x.ma))
for x in a:
    print(x)
