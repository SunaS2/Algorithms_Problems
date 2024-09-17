from collections import deque

def BFS(s):
    q = deque()
    q.append((s,0))
    visited = [0]*100001
    visited[s] = 1

    while q:
        now, depth = q.popleft()

        if now == K:
            return depth

        for cal in (now+1, now-1, 2*now):
            if 0<= cal <= 100000 and visited[cal] == 0:
                q.append((cal, depth+1))
                visited[cal] = 1

N, K = map(int,input().split())
print(BFS(N))
