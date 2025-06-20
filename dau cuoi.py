t = int(input())
for i in range(t):
    n = input()
    a = list(n)
    if (a[0] == a[-2]) and (a[1] == a[-1]):
            print('YES') 
    else:
        print('NO')