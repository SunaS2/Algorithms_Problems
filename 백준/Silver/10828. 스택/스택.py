import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    line = input().split()

    if "push" in line:
        arr.append(line[1])
    elif "top" in line:
        if arr:
            print(arr[-1])
        else:
            print(-1)
    elif "pop" in line:
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif "size" in line:
        print(len(arr))
    elif "empty" in line:
        if arr:
            print(0)
        else:
            print(1)