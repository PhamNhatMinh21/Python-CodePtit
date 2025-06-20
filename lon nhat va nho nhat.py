while True:
    n = int(input())
    if n == 0:
        break
    res = [0] * n
    for i in range(n):
        res[i] = int(input())
    if len(set(res)) == 1:
        print('BANG NHAU')
    else:
        print(min(res), max(res))
