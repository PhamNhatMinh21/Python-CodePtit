n = int(input())
x = set()
for _ in range(n):
    tmp = input().strip()
    x.add(tmp)
print(len(x))