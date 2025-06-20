def check(n, b):
    if n == 0:
        return '0'
    x = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while n > 0:
        result.append(x[n % b])
        n //= b
    return ''.join(result[::-1])
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(check(a, b))