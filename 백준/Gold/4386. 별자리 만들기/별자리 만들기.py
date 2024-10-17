def prim(start):
    visited = set()
    visited.add(start)

    weight = 0

    for _ in range(N-1):
        min_dist, next_node = float('inf'), -1

        for node in visited:
            for j in range(N):
                if j not in visited and 0<graph[node][j]<min_dist:
                    min_dist = graph[node][j]
                    next_node = j
        weight += min_dist
        visited.add(next_node)
    
    return weight

N = int(input())
stars = []
for _ in range(N):
    x,y = map(float,input().split())
    stars.append((x,y))

graph = [[float('inf')] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        d = (((stars[i][0] - stars[j][0])**2)+((stars[i][1] - stars[j][1])**2))**(0.5)
        graph[i][j] = d

result = prim(0)
print(result)