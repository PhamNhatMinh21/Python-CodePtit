from math import *
def nt(n):
    n = int(n)
    for i in range(2, isqrt(n) +1):
        if n % i == 0:
            return False
    return n > 1
t = int(input())
for _ in range(t):
    n = input()
    a = n[-4:]
    print('YES' if nt(a) else 'NO')