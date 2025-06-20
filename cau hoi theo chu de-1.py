n = int(input())
a = []
s = ''
for i in range(n):
    s = input()
    a.append(s)
    if s == '':
       n += 1
       print(f'{a[0]}: {len(a)-2}')
       a.clear()
print(f'{a[0]}: {len(a)-1}')


