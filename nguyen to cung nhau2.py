from math import *
def nt(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return n > 1
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if gcd(a[i], a[j]) == 1:
            print(a[i], a[j])