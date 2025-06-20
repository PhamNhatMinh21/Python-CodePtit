from math import *
t = int(input())
for i in range(t):
    x, y, z = list(map(float, input().split()))
    y /= 100
    tmp = log(z / x, 1 + y).real
    if tmp == int(tmp):
        print(int(tmp))
    else:
        print(int(tmp) + 1)