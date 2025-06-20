for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    check = False
    i, j, h = 0, 0 , 0
    while i < n and j < m and h < k:
        if a[i] == b[j] == c[h]:
            print(a[i], end = ' ')
            check = True
            i += 1
            j += 1
            h += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[h]:
            j += 1
        else:
            h += 1
    if check == False:
        print('NO')
    else:
        print()