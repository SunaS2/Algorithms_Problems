def BFS(s,n,g):
    q = []
    visited = [[0] * n for _ in range(n)]
    q.append(s) #정점 기록
    visited[s[0]][s[1]] = 1 #시작점!
    d = [[0,-1],[-1,0],[0,1],[1,0]]
    while q: #q에 뭐가 들어 있을 때(만약에 q가 비면 모든 정점을 다 돌았단 뜻)
        #q의 첫 번째 노드를 방문하고, 여기에 관련된 노드들을 탐색해 q에 추가한다
        curr = q.pop(0)
        if curr == g:
            return 1
        for k in range(4):
            nr = curr[0]+d[k][0]
            nc = curr[1]+d[k][1]
            if 0<=nr<n and 0<=nc<n and maze[nr][nc] != 1 and visited[nr][nc]==0:
                q.append([nr,nc])
                visited[nr][nc] = visited[curr[0]][curr[1]] + 1
    return 0

T = 10
for t in range(1,T+1):
    tc = int(input())
    n = 100
    maze = [list(map(int,input())) for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if maze[r][c] == 2:
                S = [r,c]
    for r in range(n):
        for c in range(n):
            if maze[r][c] == 3:
                G = [r,c]
    print(f'#{tc} {BFS(S,n,G)}')


    
