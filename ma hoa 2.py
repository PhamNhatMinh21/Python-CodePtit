p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    a = input()
    if a[0] == "0":
        break
    k, s = a.split()
    k = int(k)
    res = ""
    for i in range(len(s)):
        res += p[(p.index(s[i]) + k) % 28]    
    print(res[::-1])