def check(n):
    n = str(n)
    if len(n) % 2 == 1:
        return False
    if n != n[::-1]:
        return False
    for x in n:
        if int(x) % 2 == 1:
            return False
    return True
def ok(n):
    p = []
    for x in range(22, n):
        if check(x):
            p.append(str(x))
    return p
t = int(input())
for i in range(t):
    n = int(input())
    result = ok(n)
    print(*result)