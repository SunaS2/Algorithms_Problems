# bj1012: 유기농 배추

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(a,b):
    q = deque()
    q.append((a,b))
    farm[a][b] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if farm[nx][ny] == 1:
                farm[nx][ny] = 0
                q.append((nx, ny))


T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                cnt += 1
                BFS(i, j)
    print(cnt)