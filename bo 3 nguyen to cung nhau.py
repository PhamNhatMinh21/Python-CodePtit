from math import *
def check(a, b):
    if gcd(a, b) == 1:
        return True
    return False
a, b = map(int, input().split())
for i in range(a, b+1):
    for j in range(i+1, b+1):
        for k in range(j+1, b+1):
            if check(i, j) and check(j, k) and check(i, k):
                print(f'({i}, {j}, {k})')
