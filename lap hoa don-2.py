from datetime import datetime
class HoaDon:
    def __init__(self, ma, ten, so, nhan, tra, phi):
        self.ma = 'KH{0:0>2}'.format(ma)
        self.ten = ten
        self.so = so
        self.nhan = nhan
        self.tra = tra
        self.phi = phi
    def ngay(self):
        nhan = datetime.strptime(self.nhan, "%d/%m/%Y")
        tra = datetime.strptime(self.tra, "%d/%m/%Y")
        if nhan == tra:
            return 1
        return (tra - nhan).days + 1
    def check(self):
        x = int(self.so[0:1])
        if x == 1:
            return 25
        elif x == 2:
            return 34
        elif x == 3:
            return 50
        else:
            return 80
    def tong(self):
        return self.ngay() * self.check() + self.phi
    def __str__(self):
        return f'{self.ma} {self.ten} {self.so} {self.ngay()} {self.tong()}'
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        ten = input()
        so = input()
        nhan = input().strip()
        tra = input().strip()
        phi = int(input())
        res = HoaDon(i+1, ten, so, nhan, tra, phi)
        a.append(res)
    a = sorted(a, key = lambda x : -x.tong())
    for x in a:
        print(x)