n = int(input())
a = list(map(int, input().split()))
min_val = 10**9
for x in a:
    cnt = 0
    for y in a:
        cnt += abs(x-y)
    if min_val > cnt:
        min_val = cnt
        ok = x
print(min_val, ok)