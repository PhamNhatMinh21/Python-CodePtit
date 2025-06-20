for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    print('YES' if all(a[i] <= b[i] for i in range(n)) else 'NO')