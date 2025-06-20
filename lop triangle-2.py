from math import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k):
        a = self.x - k.x
        b = self.y - k.y
        res = sqrt(a * a + b * b)
        return res
class Triangle :
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def check(self) :
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if(max(a, b, c) * 2 >= a + b + c):
            print('INVALID')
        else:
            x = sqrt((a + b + c) * (b - c + a) * (b + c - a) * (c + a - b))/4
            print('{:.2f}'.format(x))
if __name__ == '__main__':
    t = int(input())
    a = []
    for x in range(t):
        a += map(float, input().split())
        i = 0
    for z in range(t):
        res = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
        res.check()
        i += 6