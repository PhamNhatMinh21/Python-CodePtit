class ThiSinh:
    def __init__(self, ten, lop, ns, gpa):
        self.ten = ten
        self.lop = lop
        self.ns = ns
        self.gpa = gpa
    def chuanHoa(self):
        if self.ns[1] == '/':
            self.ns = '0' + self.ns
        if self.ns[4] == '/':
            self.ns = self.ns[0:3] + '0' + self.ns[3:]
        tmp = self.ten.split()
        res = ' '.join(tmp)
        res = res.title()
        self.ten = res
    def __str__(self):
        return f'{'SV001'} {self.ten} {self.lop} {self.ns} {self.gpa:.1f}'
if __name__ == '__main__':
    ten = input()
    lop = input()
    ns = input()
    gpa = float(input())
    t = ThiSinh(ten, lop, ns, gpa)
    t.chuanHoa()
    print(t)