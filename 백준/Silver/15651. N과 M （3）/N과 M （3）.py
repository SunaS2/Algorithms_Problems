def backtrack(row,m):
    global n
    if row == m:
        print(*result)
        return

    for i in range(n):
        result[row] = lst[i]
        backtrack(row+1,m)
        result[row] = 0
    pass

n,m = map(int,input().split())
result = [0] * m
lst = [x for x in range(1,n+1)]

backtrack(0,m)