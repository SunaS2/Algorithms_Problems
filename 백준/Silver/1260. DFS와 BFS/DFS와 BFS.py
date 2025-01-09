def DFS(start, visited=[]):

    visited.append(start)

    for next in adjL[start]:
        if next not in visited:
            DFS(next,visited)

    return visited

from collections import deque
def BFS(start):
    q = deque()
    visited = [False] * (N+1)
    q.append(start)
    visited[start] = True

    result = []

    while q:
        now = q.popleft()
        result.append(now)
        for next in adjL[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

    return result

N, M, V = map(int,input().split())
adjL = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    adjL[a].append(b)
    adjL[b].append(a)

for L in adjL:
    L.sort()

print(*DFS(V))
print(*BFS(V))