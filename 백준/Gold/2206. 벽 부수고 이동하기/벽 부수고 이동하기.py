from collections import deque
import sys
input = sys.stdin.readline

dr = (-1,1,0,0)
dc = (0,0,-1,1)


def bfs(r=0,c=0, chance=1):
    global maze
    q = deque()
    q.append((r,c,chance))
    visited = [[[0]*2 for _ in range(M) ] for _ in range(N)]
    visited[r][c][chance] = 1

    while q:
        now = q.popleft()
        chn = now[2]

        if now[0] == (N-1) and now[1] == (M-1):
            return visited[N-1][M-1][chn]

        for d in range(4):
            nr = now[0] + dr[d]
            nc = now[1] + dc[d]

            if 0<=nr<N and 0<=nc<M and visited[nr][nc][chn]==0:
                if maze[nr][nc] == 0:
                    q.append((nr,nc,chn))
                    visited[nr][nc][chn] = visited[now[0]][now[1]][chn] + 1
                elif maze[nr][nc]==1 and chn == 1:
                    q.append((nr,nc,0))
                    visited[nr][nc][0] = visited[now[0]][now[1]][chn] + 1

    return -1


N, M = map(int, input().split())
maze = [list(map(int,input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

print(bfs())