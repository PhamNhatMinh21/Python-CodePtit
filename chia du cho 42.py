from sys import stdin
if __name__ == '__main__':
    a = []
    for s in stdin:
        a += list(map(int, s.split()))
        if len(a) == 10:
            break
    b = []
    for x in a:
        b.append(x%42)
    x = set(b)
    print(len(x))