def check(a, b):
    if b == 1:
        if 1 <= a <= 19:
            return 'Ma Ket'
        elif 20 <= a <= 31:
            return 'Bao Binh'
    elif b == 2:
        if 1 <= a <= 18:
            return 'Bao Binh'
        elif 19 <= a <= 29:
            return 'Song Ngu'
    elif b == 3:
        if 1 <= a <= 20:
            return 'Song Ngu'
        elif 21 <= a <= 31:
            return 'Bach Duong'
    elif b == 4:
        if 1 <= a <= 19:
            return 'Bach Duong'
        elif 20 <= a <= 30:
            return 'Kim Nguu'
    elif b == 5:
        if 1 <= a <= 20:
            return 'Kim Nguu'
        elif 21 <= a <= 31:
            return 'Song Tu'
    elif b == 6:
        if 1 <= a <= 20:
            return 'Song Tu'
        elif 21 <= a <= 30:
            return 'Cu Giai'
    elif b == 7:
        if 1 <= a <= 22:
            return 'Cu Giai'
        elif 23 <= a <= 31:
            return 'Su Tu'
    elif b == 8:
        if 1 <= a <= 22:
            return 'Su Tu'
        elif 23 <= a <= 31:
            return 'Xu Nu'
    elif b == 9:
        if 1 <= a <= 22:
            return 'Xu Nu'
        elif 23 <= a <= 30:
            return 'Thien Binh'
    elif b == 10:
        if 1 <= a <= 22:
            return 'Thien Binh'
        elif 23 <= a <= 31:
            return 'Thien Yet'
    elif b == 11:
        if 1 <= a <= 22:
            return 'Thien Yet'
        elif 23 <= a <= 30:
            return 'Nhan Ma'
    elif b == 12:
        if 1 <= a <= 21:
            return 'Nhan Ma'
        elif 22 <= a <= 31:
            return 'Ma Ket'
    else:
        return '0'
    
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(check(a, b))