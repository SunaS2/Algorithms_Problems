import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()
        for next in adjL[now]:
            if visited[next]==0:
                q.append(next)
                visited[next] = 1
    
    return 1


N, M = map(int,input().split())

adjL = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int,input().split())
    adjL[u].append(v)
    adjL[v].append(u)

visited = [0] * (N+1)

cnt = 0
for x in range(1,N+1):
    if visited[x] == 0:
        cnt += bfs(x)

print(cnt)