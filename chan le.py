from math import *
t = int(input())
for i in range(t):
    n = input()
    a = list(n)
    ok = True
    cnt = 0
    for x in a:
        cnt += int(x)
    for i in range(len(n)-1):
        if abs(int(n[i+1]) - int(n[i])) != 2:
            ok = False
            break
    if ok and cnt % 10 == 0:
        print('YES')
    else:
        print('NO')