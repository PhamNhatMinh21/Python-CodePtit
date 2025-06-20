t = int(input())
for _ in range(t):
    a = input()
    cnt = 1
    for i in range(1, len(a)):
        if a[i] == a[i-1]:
            cnt += 1
        else:
            print(cnt, end = '')
            print(a[i-1], end = '')
            cnt = 1
    print(cnt, end = '')
    print(a[-1])