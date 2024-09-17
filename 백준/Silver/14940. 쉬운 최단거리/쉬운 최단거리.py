from collections import deque
dr = (-1,1,0,0) # 상 하 좌 우
dc = (0,0,-1,1) # 가로, 세로

def BFS(node):
    q = deque()
    q.append(node)

    while q:
        now = q.popleft()
        for d in range(4):
            nr = now[0] + dr[d]
            nc = now[1] + dc[d]

            if 0<=nr<N and 0<=nc<M and visited[nr][nc] <= 0 and arr[nr][nc] == 1:
                q.append((nr,nc))
                visited[nr][nc] = visited[now[0]][now[1]] + 1
def find_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                return (i,j)

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

visited = [[-1] * M for _ in range(N)]
s = find_start()
visited[s[0]][s[1]] = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            visited[i][j] = 0
BFS(s)

for x in visited:
    print(*x)