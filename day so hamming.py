dict = {1:1}
while True:
    a = []
    ok = 0
    for x in dict:
        if x < 10**18:
            if (x*2) not in dict:
                a.append(x*2)
            if (x*3) not in dict:
                a.append(x*3)
            if (x*5) not in dict:
                a.append(x*5)
    for x in a:
        ok = 1
        dict[x] = 1
    if ok == 0:
        break
cnt = 1
a = sorted(list(dict))
for x in a:
    dict[x] = cnt
    cnt += 1
for _ in range(int(input())):
    n = int(input())
    if n in dict:
        print(dict[n])
    else:
        print('Not in sequence')