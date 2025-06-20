n = int(input())
a = {}
check = True
for _ in range(n - 1):
    x, y = [int(x) for x in input().split()]
    if x in a:
        a[x] += 1
    else:
        a[x] = 1
    if y in a:
        a[y] += 1
    else:
        a[y] = 1
for i in range(1, n + 1):
    if not(i in a) or (a[i] != 1 and a[i] != n - 1):
        check = False
        print('No')
        break
if check == True:
    print('Yes')