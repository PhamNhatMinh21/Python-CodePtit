from functools import cmp_to_key
def cmp(a, b):
    if a[1] != b[1]:
        return b[1] - a[1]
    if a[2] != b[2]:
        return a[2] - b[2]
    return (a[0] > b[0]) - (a[0] < b[0])
a = {}
res = []
for _ in range(int(input())):
    ten = input()
    bai, sub = map(int, input().split())
    res.append((ten, bai, sub))
res.sort(key = cmp_to_key(cmp))
for x in res:
    print(x[0], x[1], x[2])