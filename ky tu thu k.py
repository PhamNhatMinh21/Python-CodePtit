def find(n, k):
    if k == 2 ** (n-1):
        return n
    if k > 2 ** (n-1):
        return find(n-1, k - 2 ** (n-1))
    return find(n-1, k)
for _ in range(int(input())):
    n, k = map(int, input().split())
    print(chr(find(n, k) + 64))