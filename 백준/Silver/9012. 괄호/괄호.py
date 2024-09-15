N = int(input())
for _ in range(N):
    lst = input()
    stack = []
    result = 'NO'
    for x in lst:
        if x == ')' and len(stack) > 0:
            stack.pop()
        elif x == ')' and len(stack) == 0:
            break
        elif x == '(':
            stack.append(x)
    else:
        if len(stack) == 0:
            result = 'YES'

    print(result)