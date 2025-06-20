while True:
    x, y, z, t = list(map(int, input().split()))
    if x == 0 and y == 0 and z == 0 and t == 0:
        break
    cnt = 0
    while not(x == y == z == t):
        x1 = abs(x - y)
        y1 = abs(y - z)
        z1 = abs(z - t)
        t1 = abs(t - x)
        x, y, z, t = x1, y1, z1, t1
        cnt += 1
    print(cnt)