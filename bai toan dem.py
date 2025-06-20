from sys import stdin
if __name__ == '__main__':
    n = int(input())
    a = []
    for s in stdin:
        a += list(map(int, s.split()))
        if len(a) == n:
            break
    res = max(a)
    ok = True
    for i in range(1, res + 1):
        if i not in a:
            print(i)
            ok = False
    if ok:
        print('Excellent!')


