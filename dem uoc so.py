for i in range(int(input())):
    s1 = input()
    s2 = input()
    x = ''.join(sorted(s1))
    y = ''.join(sorted(s2))
    print(f'Test {i+1}: ' + ('YES' if x == y else 'NO'))