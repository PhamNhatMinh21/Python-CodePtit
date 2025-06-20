n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
k = int(input())
tren, duoi = 0, 0
for i in range(n):
    for j in range(n):
        if j < n - i - 1:
            duoi += a[i][j]
        elif j > n - i - 1:
            tren += a[i][j]
res = abs(tren - duoi)
if res <= k:
    print('YES')
else:
    print('NO')
print(res)
