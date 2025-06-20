n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(set(a))
n = len(a)
b = [0] * (k + 1)
def Try(i):
    for j in range(b[i] + 1, n + 1):
        b[i+1] = j
        if i + 1 == k:
            for m in range(1, k + 1):
                print(a[b[m] - 1], end= ' ')
            print()
        else:
            Try(i + 1)  
Try(0)
