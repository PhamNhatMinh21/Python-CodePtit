def check(n):
    x = int(n, 2)
    y = oct(x)
    return y[2:]
n = input()
print(check(n))