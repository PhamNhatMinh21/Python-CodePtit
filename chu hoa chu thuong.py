n = input()
a = list(n)
cnt1 = 0
cnt2 = 0
for x in a:
    if x.isupper(): cnt1 += 1
    elif x.islower(): cnt2 += 1
if cnt1 > cnt2:
    print(n.upper())
else:
    print(n.lower())