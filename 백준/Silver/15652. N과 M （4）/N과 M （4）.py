def backtracking(row,m):
    global n
    global now
    if row == m:
        print(*result)
        return
    for i in range(n):
        if now < lst[i]:
            result[row] = lst[i]
            backtracking(row+1,m)
            now = result[row]
            result[row] = 0

n, m = map(int,input().split())
lst = [x for x in range(1,n+1)]
result = [0] * m
now = result[0]

backtracking(0,m)