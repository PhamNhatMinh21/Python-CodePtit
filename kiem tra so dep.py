t = int(input())
for i in range(t):
    a = input()
    s = set(a)
    ok = True
    for i in range(len(a)):
        if int(a[i]) == int(a[i-1]) or(i>1 and a[i] != a[i-2]):
            ok = False
    print('YES' if ok else 'NO')