import sys
input = sys.stdin.readline

M = int(input())
S = set()
for _ in range(M):
    command = input()
    if ' ' in command:
        c, x = command.split()
        x = int(x)

    if 'add' in command:
        S.add(x)
    elif 'remove' in command:
        S.discard(x)
    elif 'check' in command:
        if x in S:
            print(1)
        else:
            print(0)
    elif 'toggle' in command:
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif 'all' in command:
        S = set(list(range(1,21)))
    elif 'empty' in command:
        S.clear()