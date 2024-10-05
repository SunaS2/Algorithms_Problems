from collections import deque
import sys
input = sys.stdin.readline

dr = (-2,-2,0,0,2,2)
dc = (-1,1,-2,2,-1,1)

def BFS(s_row, s_col, end_r, end_c):
    q = deque()
    q.append((s_row,s_col))
    visited = [[0] * N for _ in range(N)]
    visited[s_row][s_col] = 1

    while q:
        r, c = q.popleft()
        if r == end_r and c == end_c:
            return visited[r][c] - 1

        for k in range(6):
            nr = r+dr[k]
            nc = c+dc[k]

            if 0<=nr<N and 0<=nc<N and visited[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = visited[r][c] + 1

    return -1

N = int(input())
r1, c1, r2, c2 = map(int, input().strip().split())

print(BFS(r1,c1,r2,c2))