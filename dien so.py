for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    a = sorted(a)
    print(a[-1] - a[0] + 1 - len(a))   