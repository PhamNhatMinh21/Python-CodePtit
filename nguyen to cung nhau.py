from math import *
n, m = list(map(int, input().split()))
a = 10 ** (m-1)
b = 10 ** m
cnt1 = 0
for i in range(a, b):
    if gcd(i, n) == 1:
        print(i, end = ' ')
        cnt1 += 1
        if cnt1 % 10 == 0:
            print()
