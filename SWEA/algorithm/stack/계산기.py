def postfix(lst):
    stack = []
    result = []
    for l in lst:
        if l.isdigit():
            result.append(l)
        else:
            stack.append(l)
    for _ in range(len(stack)):
        result.append(stack.pop())

    return result

def calcul(lst):
    stack1 = []
    for l in lst:
        if l.isdigit():
            stack1.append(int(l))
        else:
            a = stack1.pop()
            b = stack1.pop()
            if l == '+':
                c = b + a
            stack1.append(c)
    return stack1[0]

T = 10
for tc in range(1,T+1):
    n = int(input())
    lst = list(input())
    result = calcul(postfix(lst))

    print(f'#{tc} {result}')