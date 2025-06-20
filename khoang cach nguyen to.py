from math import *
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True
def check(n):
    a = []
    i = 2
    while len(a) < n:
        if nt(i):
            a.append(i)
        i += 1
    return a
n, x = list(map(int, input().split()))
a = check(n)
res = [x]
for i in a:
    res.append(res[-1] + i)
print(*res)