for _ in range(int(input())):
    a = input()
    n, p, s = len(a), -1, '0'
    for i in range(n-2, -1, -1):
        if a[i] > a[i+1]:
            p = i
            break
    if p == -1:
        print('-1')
        continue
    q = p + 1
    for i in range(p + 1, n):
        if a[i] > s and a[i] > a[p+1] and a[i] < a[p]:
            s = a[i]
            q = i
    a = a[:p:] + a[q] + a[p+1:q:] + a[p] + a[q+1::]
    if a[0] == '0':
        print('-1')
    else:
        print(a)