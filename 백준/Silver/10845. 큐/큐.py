q = []
N = int(input())
for _ in range(N):
    command = input()
    if 'push' in command:
        y,x = command.split()
        q.append(int(x))
    elif 'pop' in command:
        if len(q)==0:
            print(-1)
        else:
            print(q.pop(0))
    elif 'size' in command:
        print(len(q))
    elif 'empty' in command:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif 'back' in command:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])