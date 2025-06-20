a = {}
for _ in range(int(input())):
    ma = input()
    ten = input()
    hinhthuc = input()
    a[ma] = [ten, hinhthuc]
    res = sorted(a)
for x in res:
    print(x, a[x][0], a[x][1])