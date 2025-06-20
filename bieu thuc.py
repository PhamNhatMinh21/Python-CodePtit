t = int(input())
for _ in range(t):
    s = input().strip()
    stack = []
    idx = 1
    for x in s:
        if x == '(':
            print(idx, end=" ")
            stack.append(idx)
            idx += 1
        elif x == ')':
            print(stack.pop(), end=" ")
    print()