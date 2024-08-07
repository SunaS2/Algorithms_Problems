T = int(input())
for tc in range(1,T+1):
    string = list(input())

    stack = []
    flag = 1
    for i in range(len(string)):
        if string[i] in '({':
            stack.append(string[i])
        elif string[i] in ')}':
            if stack:
                top = stack[-1]
                if top == '(' and string[i] ==')':
                    stack.pop()
                elif top == '{' and string[i] =='}':
                    stack.pop()
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break
    if len(stack) == 0 and flag == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')
