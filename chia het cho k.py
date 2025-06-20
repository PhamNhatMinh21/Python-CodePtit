a, k, n = map(int, input().split())
check = False
for i in range(1, n//k + 1):
    if k*i-a <= n-a and k*i-a > 0:
        print(k*i-a, sep = ' ', end = ' ')
        check = True
if check == False:
    print(-1)