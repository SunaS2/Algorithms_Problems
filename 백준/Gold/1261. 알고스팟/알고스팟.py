from heapq import heappush, heappop

dr = (-1,1,0,0)
dc = (0,0,-1,1)

def dijkstra(start):
    q=[]
    heappush(q,(0,start))
    visited[start[0]][start[1]] = 0
    while q:
        cnt, now = heappop(q)

        for d in range(4):
            nr = now[0] + dr[d]
            nc = now[1] + dc[d]

            if 0<=nr<N and 0<=nc<M and cnt+maze[nr][nc]<visited[nr][nc]:
                visited[nr][nc] = cnt+maze[nr][nc]
                heappush(q,(cnt+maze[nr][nc],(nr,nc)))


M,N = map(int,input().split())
maze = [list(map(int,input())) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]
dijkstra((0,0))
print(visited[N-1][M-1])