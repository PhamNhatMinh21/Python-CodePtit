def check(s):
    if len(s) < 4:
        return 0
    for x in s :
        if x.isdigit():
            if int(x) < 0 or int(x) > 255:
                return 0
        else:
            return 0
    return 1
for _ in range(int(input())):
    x = input().split('.')
    print('YES' if check(x) == 1 else 'NO')