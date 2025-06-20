def check(n):
    for x in n:
        if x not in '012':
            return False
    return True
t = int(input())
for i in range(t):
    a = input()
    print('YES' if check(a) else 'NO')