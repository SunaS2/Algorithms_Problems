dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


def DFS(now_r, now_c, k):
    global MAX,visited
    MAX = max(MAX, visited[now_r][now_c])
    # 해당 장소에서의 연산 수행
    # 주변에 갈 수 있는 곳들을 탐색하고, 갈 수 있는 곳들을 list로 생성
    # 현재보다 작은 곳만 찾아간다, K 내에서 깎기가 가능하다면 현재 위치보다 -1일 때까지 깎는다
    # 돌아 올 때 다시 돌려놓는다
    for d in range(4):
        nr = now_r + dr[d]
        nc = now_c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
            if mountin[now_r][now_c] > mountin[nr][nc]:
                visited[nr][nc] = visited[now_r][now_c] + 1
                DFS(nr, nc, k)
                visited[nr][nc] = 0
            elif k and mountin[nr][nc] - K < mountin[now_r][now_c]:
                tmp = mountin[nr][nc]
                mountin[nr][nc] = mountin[now_r][now_c] - 1
                visited[nr][nc] = visited[now_r][now_c] + 1
                DFS(nr, nc, k - 1)
                visited[nr][nc] = 0
                mountin[nr][nc] = tmp


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountin = []
    top = 0
    for i in range(N):
        mountin.append(list(map(int,input().split())))
        for j in range(N):
            if mountin[i][j]>top:
                top = mountin[i][j]

    MAX = 0
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if mountin[r][c] == top:
                visited[r][c] = 1
                DFS(r, c, 1)
                visited[r][c] = 0

    print(f'#{tc} {MAX}')