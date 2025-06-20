from math import *
from decimal import Decimal
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k):
        a = self.x - k.x
        b = self.y - k.y
        res = sqrt(a *a + b * b)
        return '{:.4f}'.format(res)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1