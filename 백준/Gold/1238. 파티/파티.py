from heapq import heappush, heappop

def dijkstra(start,end):
    q = []
    heappush(q,(0,start))
    visited = [float('inf')] * (N+1)
    visited[start] = 0

    while q:
        time, now = heappop(q)

        for next in range(len(adjM[now])):
            if adjM[now][next] > 0 and adjM[now][next]+time<visited[next]:
                visited[next] = adjM[now][next]+time
                heappush(q,(adjM[now][next]+time,next))
    
    return visited[end]



N,M,X = map(int,input().split())
adjM = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b, t = map(int,input().split())
    adjM[a][b] = t

times = [0] * (N+1)

# 가는 시간
for i in range(1,N+1):
    times[i] = dijkstra(i,X)
    times[i] += dijkstra(X,i)

print(max(times))