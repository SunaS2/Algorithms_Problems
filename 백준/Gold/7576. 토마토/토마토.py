import sys
input = sys.stdin.readline

from collections import deque

def find_start():
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append((i,j))

dr = (-1,1,0,0)
dc = (0,0,-1,1)

def bfs():
    global day
    while q:
        now = q.popleft()
        for d in range(4):
            nr = now[0] + dr[d]
            nc = now[1] + dc[d]

            if 0<=nr<N and 0<=nc<M and box[nr][nc] == 0:
                q.append((nr,nc))
                box[nr][nc] = box[now[0]][now[1]] + 1

def solv(result):
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1
    
    return result-1

M, N = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(N)]

q = deque()
find_start()

bfs()
result = max(map(max,box))

print(solv(result))