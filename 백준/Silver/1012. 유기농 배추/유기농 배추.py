def DFS(s):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    stack = []
    stack.append(s)
    visited[s[0]][s[1]] = 1
    now = s
    while True:
        for i in range(4):
            nr = now[0]+dr[i]
            nc = now[1]+dc[i]
            if 0<=nr<n and 0<=nc<m and farm[nr][nc]==1 and visited[nr][nc]==0:
                visited[nr][nc] = 1
                stack.append([nr,nc])
                break 
        else:
            if stack:
                now=stack.pop()
            else:
                break
    return 1

T = int(input())
for tc in range(T):
    m, n, k = map(int,input().split())

    farm = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int,input().split())
        farm[y][x] = 1
    
    cnt = 0
    for r in range(n):
        for c in range(m):
            if farm[r][c] == 1 and visited[r][c] == 0:
                cnt += DFS([r,c])
    
    print(cnt)