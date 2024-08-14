def BFS(s,V,g):
    q = []
    visited = [0] * (V+1)
    q.append(s) #정점 기록
    visited[s] = 1 #시작으로부터의 거리 기록(1부터 시작)
    # if s==g:
    #     return 0
    while q: #q에 뭐가 들어 있을 때(만약에 q가 비면 모든 정점을 다 돌았단 뜻)
        #q의 첫 번째 노드를 방문하고, 여기에 관련된 노드들을 탐색해 q에 추가한다
        n = q.pop(0)
        if n == g:
            return visited[g] - 1
        for w in adjL[n]: 
            if visited[w] == 0: 
                q.append(w)
                visited[w] = visited[n] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    lst = [list(map(int,input().split())) for _ in range(E)]
    S, G = map(int,input().split())

    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        v1 = lst[i][0]
        v2 = lst[i][1]

        adjL[v1].append(v2)
        adjL[v2].append(v1)

    result = BFS(S,V,G)

    print(f'#{tc} {result}')
