x = input()
a = [0] * len(x)
def Try(s, k):
    if k == len(x):
        print(s)
        return
    for i in range(len(x)):
        if a[i] == 0 :
            a[i] = 1
            if k == len(x):
                print(s)
            else:
                Try(s + x[i], k + 1)
            a[i] = 0
Try('', 0)