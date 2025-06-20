def check(a, n, m):
    b = []
    for j in range(m):
        b.append([0] * n)
    for i in range(n):
        for j in range(m):
            b[j][i] = a[i][j]
    res = []
    for i in range(n):
        res.append([0] * n)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                res[i][j] += a[i][k] * b[k][j]
    for x in res:
        print(' '.join(map(str, x)))

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    check(a, n, m)