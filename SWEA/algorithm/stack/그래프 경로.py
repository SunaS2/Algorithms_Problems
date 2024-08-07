def DFS(s,v,g):
    visited = [0]*(v+1)
    stack = []

    visited[s] = 1
    n = s
    while True:
        for w in adjL[n]:
            if visited[w] == 0:
                stack.append(n)
                n = w
                visited[w] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    if visited[g] == 1: #단방향이므로
        return 1
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())

    adjL = [[] for _ in range(V+1)]

    for i in range(E):
        v1, v2 = graph[i][0], graph[i][1]
        adjL[v1].append(v2)

    result = DFS(S,V,G)

    print(f'#{tc} {result}')
'''
1   
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''
