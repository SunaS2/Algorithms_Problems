def postfix(lst):
    stack = []
    post= []
    for l in lst:
        if l.isdigit():
            post.append(l)
            # if stack:
            #     post.append(stack.pop())
        else:
            if l == '(':
                stack.append(l)
            elif l == ')':
                while stack:
                    s= stack.pop()
                    if s == '(':
                        break
                    else:
                        post.append(s)
            elif l == '+':
                if stack and stack[-1] == '*':
                    while stack:
                        post.append(stack.pop())
                stack.append(l)
            elif l == '*':
                stack.append(l)
    while stack:
        post.append(stack.pop())
    return post

def calcul(postfixed):
    digit = []
    for p in postfixed:
        if p.isdigit():
            digit.append(int(p))
        elif p == '+':
            a = digit.pop()
            b = digit.pop()
            c = a+b
            digit.append(c)
        elif p == '*':
            a = digit.pop()
            b = digit.pop()
            c = a * b
            digit.append(c)
    return digit
T = 1
for tc in range(1,T+1):
    n = int(input())
    lst = list(input())

    postfixed = postfix(lst)
    print(postfixed)
    result = calcul(postfixed)

    print(result)