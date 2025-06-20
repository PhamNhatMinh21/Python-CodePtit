def chuyen_doi(s, b):
    x = int(s, 2)
    if b == 2:
        return s
    elif b == 4:
        while len(s) % 2 != 0:
            s = "0" + s
        result = ""
        for i in range(0, len(s), 2):
            result += str(int(s[i:i+2], 2))
        return result
    elif b == 8:
        return oct(x)[2:]
    elif b == 16:
        return hex(x)[2:].upper()
    else:
        return 0
for _ in range(int(input())):
    he = int(input())
    s = input()
    result = chuyen_doi(s, he)
    print(str(result))