s = input()
if len(s) % 2 == 0:
    res = [s[i:i+2] for i in range(0, len(s), 2)]
else:
    res = [s[i:i+2] for i in range(0, len(s) - 1, 2)]
a = list(dict.fromkeys(res))
a.sort()
print(*a)
