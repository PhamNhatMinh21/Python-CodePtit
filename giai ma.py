for _ in range(int(input())):
    n = input()
    a = []
    for i in range(len(n)):
        if n[i].isdigit():
            a.append(n[i-1] * (int(n[i]) - 1))
        else:
            a.append(n[i])
    for x in a:
        print(x, end = '')
    print()


