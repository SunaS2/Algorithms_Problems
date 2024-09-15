from collections import deque
def BFS(start):
    global cnt
    q = deque()
    q.append(start)
    visited = [0] * (N+1)
    visited[start] = 1

    while q:
        now = q.popleft()
        cnt += 1
        for x in adjL[now]:
            if visited[x] == 0:
                visited[x] = 1
                q.append(x)

N = int(input())
E = int(input())
adjL = [[] for _ in range(N+1)]

for _ in range(E):
    a, b = map(int,input().split())
    adjL[a].append(b)
    adjL[b].append(a)

cnt = 0
BFS(1)
print(cnt-1)
