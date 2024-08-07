T = int(input())

for tc in range(1,T+1):
    n=int(input())

    stack1 = [1]
    print(f'#{tc}')
    str_stack1 = list(map(str,stack1))
    print(f'{" ".join(str_stack1)}')
    for i in range(n-1):
        stack2 = []
        stack2.append(1)
        while len(stack1) > 1: #다음 줄 만들기 -> 반복, stack1이 빌 때까지
            p = stack1.pop()
            top = stack1[-1]
            stack2.append(top + p)
        stack2.append(1)

        str_stack2 = list(map(str,stack2))
        print(f'{" ".join(str_stack2)}')

        stack1 = stack2


