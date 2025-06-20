from math import *
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return n > 1
n = int(input())
a = list(map(int, input().split()))
cnt = {}
for x in a:
    if nt(x):
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1
for x in cnt:
    print(x, cnt[x])
