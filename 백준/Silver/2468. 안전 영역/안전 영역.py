def BFS(s,safe):
    #준비
    q = []
    q.append(s)
    visited[s[0]][s[1]] = 1

    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    while q:
        now = q.pop(0)
        for k in range(4):
            nr = now[0]+dr[k]
            nc = now[1]+dc[k]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and safe[nr][nc]==1:
                q.append([nr,nc])
                visited[nr][nc] = 1
    
    return 1

def safearea(lst, rain):
    safe = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if lst[r][c] > rain:
                safe[r][c] = 1
    return safe

N = int(input())
area = [list(map(int,input().split())) for _ in range(N)]

low = min(map(min,area))
high = max(map(max,area))

num_safe_areas = []

for rain in range(low-1,high+1):
    safe = safearea(area,rain)
    cnt = 0
    visited = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c]==0 and safe[r][c]==1:
                cnt+=BFS([r,c],safe)
    num_safe_areas.append(cnt)

result = max(num_safe_areas)
print(result)
