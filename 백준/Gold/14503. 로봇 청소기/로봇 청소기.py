def cleaner(r,c,d):
    cnt = 0
    now_r = r
    now_c = c
    now_d = d
    while True:
        # 현재 칸이 청소 되지 않은 경우, 현재 칸을 청소한다.
        if room[now_r][now_c] == 0:
            room[now_r][now_c] = 2
            cnt += 1
        # 현재 칸의 주변 4칸 중 청소 되지 않은 빈칸이 있는 경우
        # 반시계 방향으로 회전해서 앞칸이 청소 되지 않았다면 한칸 전진
        if 0 in (room[now_r-1][now_c], room[now_r+1][now_c],room[now_r][now_c-1],room[now_r][now_c+1]):
            for _ in range(4):
                now_d = (now_d + 3)%4
                nr = now_r + directions[now_d][0]
                nc = now_c + directions[now_d][1]
                if 0<=nr<N and 0<=nc<M and room[nr][nc] == 0:
                    now_r = nr
                    now_c = nc
                    break # for문 탈출
        # 현재 칸 주변4칸 중 청소되지 않은 빈칸이 없는 경우 (4방향 모두 탐색하였으나 1 or 2이면 for문을 다 돌게 됨)
        else:
            nr = now_r - directions[now_d][0]
            nc = now_c - directions[now_d][1]
            # 벽이라 후진이 안되면 작동 멈춤
            if 0<=nr<N and 0<=nc<M and room[nr][nc] == 1:
                return cnt # while문 탈출
            # 한칸 후진 할 수 있다면 후진 한다.
            elif 0<=nr<N and 0<=nc<M:
                now_r = nr
                now_c = nc


# 로봇 청소기와 방의 상태 -> 청소하는 영역의 개수 구하기
N, M = map(int,input().split())
r,c,d = map(int,input().split())
directions = ((-1,0), (0,1), (1,0), (0,-1))
room = [list(map(int,input().split())) for _ in range(N)]
# 0 -> 청소 되지 않은 칸, 1 -> 벽
print(cleaner(r,c,d))