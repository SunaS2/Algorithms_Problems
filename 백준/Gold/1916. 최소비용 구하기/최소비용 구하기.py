from heapq import heappop, heappush
import sys

input = sys.stdin.readline

def dijkstra(start,end):
    hq = []
    heappush(hq, (0,start))
    visited = [float('inf')] * (N+1)
    visited[start] = 0
    
    while hq:
        weight, now = heappop(hq)
        
        if visited[now] < weight:
            continue
      
        for next in adjL[now]:
            next_weight, next_node = next
            if visited[next_node] > weight+next_weight:
                visited[next_node] =  weight+next_weight
                heappush(hq,(visited[next_node], next_node))
    
    return visited[end]
        


N = int(input()) # 도시 개수, 노드 수
M = int(input()) # 버스 노선 수, 간선 수

adjL = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().strip().split())
    adjL[u].append((w,v))
    
start, end = map(int,input().strip().split())
result = dijkstra(start,end)
print(result)
