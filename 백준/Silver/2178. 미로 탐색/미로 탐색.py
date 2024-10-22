from collections import deque

dr = (-1,1,0,0)
dc = (0,0,-1,1)

def BFS(r,c, visited):
    start = (r,c)
    q = deque()
    q.append(start)
    visited[r][c] = 1

    while q:
        now = q.popleft()

        for d in range(4):
            nr = now[0] + dr[d]
            nc = now[1] + dc[d]

            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0 and maze[nr][nc] == 1:
                q.append((nr,nc))
                visited[nr][nc] = visited[now[0]][now[1]] + 1
    
    return visited[N-1][M-1]
 
N, M = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
print(BFS(0,0,visited))

