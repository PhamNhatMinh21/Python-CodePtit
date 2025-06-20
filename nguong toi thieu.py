from collections import Counter
s = input()
k = int(input())
if len(s) % 2 == 0:
    res = [s[i:i+2] for i in range(0, len(s), 2)]
else:
    res = [s[i:i+2] for i in range(0, len(s) - 1, 2)]
a = dict(Counter(res))
ok = False
for x, y in sorted(a.items()):
    if y >= k:
        print(x, y)
        ok = True
if not ok:
    print('NOT FOUND')
