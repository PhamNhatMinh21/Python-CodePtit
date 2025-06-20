from math import *
def nt(n):
    n = int(n)
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return n > 1
t = int(input())
for i in range(t):
    a = input()
    cnt = 0
    for i in range(len(a)):
        if nt(int(a[i])):
            cnt += 1
    cnt2 = len(a) - cnt
    if cnt > cnt2 and nt(len(a)): print('YES')
    else: print('NO')
