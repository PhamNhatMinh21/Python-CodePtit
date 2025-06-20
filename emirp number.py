a = [0] * 1000001
def sieve():
    a[0] = a[1] = 1
    for i in range(2, 1000):
        if a[i] == 0:
            for j in range(i*i, 1000001, i):
                a[j] = 1
sieve()
for i in range(int(input())):
    n = int(input())
    for i in range(1, n):
        x = int(str(i)[::-1])
        if x > i and x < n and a[i] == 0 and a[x] == 0:
            print(i, x, end = ' ')
    print()