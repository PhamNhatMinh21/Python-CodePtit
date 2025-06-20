fibo = [0, 1, 1]
for i in range(3, 93):
    fibo.append(fibo[i - 1] + fibo[i - 2])
for i in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        print(fibo[i], end = ' ')
    print()