def check(n):
    ok = 0
    if int(n) % 7 == 0:
        return int(n)
    for i in range(0, 1000):
        ok = int(n) + int(n[::-1])
        if ok % 7 == 0:
            return ok
        n = str(ok)
    return -1
t = int(input())
for i in range(t):
    n = input()
    print(check(n))