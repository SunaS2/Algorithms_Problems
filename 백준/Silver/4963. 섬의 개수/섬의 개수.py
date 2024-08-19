def DFS(start):
    #준비
    dr = [-1,-1,-1,0,0,1,1,1]
    dc = [-1,0,1,-1,1,-1,0,1]

    stack = []
    stack.append(start)
    visited[start[0]][start[1]] = 1
    now = start

    #순회 시작
    while True:
        for i in range(8):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if 0<=nr<h and 0<=nc<w and seamap[nr][nc]==1 and visited[nr][nc]==0:
                visited[nr][nc] = 1
                stack.append([nr,nc])
                break
        else:
            if stack:
                now = stack.pop()
            else:
                break
    return 1
while True:
    w,h = map(int,input().split())
    if w==0 and h==0:
        break

    seamap = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]

    cnt = 0
    for r in range(h):
        for c in range(w):
            if seamap[r][c] == 1 and visited[r][c]==0:
                start = [r,c]
                cnt += DFS(start)
    
    print(cnt)