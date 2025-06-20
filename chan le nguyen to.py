from math import *
def check(n):
    for i in range(0, len(n), 2):
        if int(n[i]) % 2 != 0:
            return False
    return True
def check1(n):
    for i in range(1, len(n), 2):
        if int(n[i]) % 2 != 1:
            return False
    return True
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return n > 1
t = int(input())
for i in range(t):
    a = input()
    x = sum(map(int, a))
    if nt(x) and check(a) and check1(a):
        print('YES')
    else:
        print('NO')


