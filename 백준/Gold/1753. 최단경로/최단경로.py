import sys
input = sys.stdin.readline

from heapq import heappop, heappush

def dijkstra(start):
    q = []
    heappush(q,(0,start))
    visited = [float('inf')] * (V+1)
    visited[start] = 0

    while q:
        # 이번 노드
        weight, now = heappop(q)

        # 다음에 갈 곳을 탐색하면서 q에 추가함...
        for node in adjL[now]:
            if visited[node[1]] > node[0] + weight:
                visited[node[1]] = node[0] + weight
                heappush(q,(weight+node[0], node[1]))
    
    return visited


V, E = map(int,input().split())
# 1부터 v까지의 정점이 있음

adjL = [[] for _ in range(V+1)]
K = int(input())

for _ in range(E):
    u, v, w = map(int,input().split())
    # 인접리스트에 (가중치, 노드) 입력
    adjL[u].append((w,v))

visited = dijkstra(K)
visited[K] = 0

for i in range(1,V+1):
    if visited[i] == float('inf'):
        print("INF")
    else:
        print(visited[i])