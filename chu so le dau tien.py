s = input()
for i in range(len(s)-1):
    if s[i] == '.':
        print(f'Result = {s[i+1]}')
        break