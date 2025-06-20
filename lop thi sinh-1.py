class ThiSinh:
    def __init__(self, ten, ns, d1, d2, d3):
        self.ten = ten
        self.ns = ns
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def __str__(self):
        tongdiem = self.d1 + self.d2 + self.d3
        return f'{self.ten} {self.ns} {tongdiem:.1f}'
if __name__ == '__main__':
    ten = input()
    ns = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    t = ThiSinh(ten, ns, d1, d2, d3)
    print(t)