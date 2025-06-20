if __name__ == '__main__':
    for _ in range(int(input())):
        result = ""
        a = list(input())
        for i in range(len(a)-1, 0, -1):
            if int(a[i]) >= 5:
                a[i] = '0'
                a[i-1] = str(int(a[i-1]) +1)
            elif int(a[i]) < 5:
                a[i] = '0'
            elif int(a[i]) == 9:
                a[i] = '0'
                a[i-1] = '10'
        result = ''.join(a)
        print(result)
        
        
        