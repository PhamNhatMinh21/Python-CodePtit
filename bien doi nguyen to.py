a = [1] * 10001
b = []
for i in range(2, 10001) :
    if a[i] == 1 :
        for j in range(i * i, 10001, i) :
            a[j] = 0
        b.append(i)
ans = 0
n = int(input())
res = map(int, input().split())
for x in res:
    s = 10**9
    for y in b:
        s = min(s, abs(x - y))
    ans = max(ans, s)
print(ans)
