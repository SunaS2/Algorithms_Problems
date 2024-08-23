def BFS(lst,visited,s,color):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    q = []
    q.append(s)
    visited[s[0]][s[1]]=1

    while q:
        now = q.pop(0)
        for d in range(4):
            nr = now[0]+dr[d]
            nc = now[1]+dc[d]
            if 0<=nr<N and 0<=nc<N and visited[nr][nc]==0 and lst[nr][nc]==color:
                q.append([nr,nc])
                visited[nr][nc]=1

    return 1

N = int(input())
board = [list(input()) for _ in range(N)]
#비색약인
RGB = [[0]*N for _ in range(N)]
#색약인
RB = [[0]*N for _ in range(N)]
for r in range(N):
    for c in range(N):
        #색약인 R,G모두 1, B=0
        #비색약인 R=1, G=2, B=0
        if board[r][c]=='R':
            RB[r][c] = 1
            RGB[r][c] = 1
        elif board[r][c]=='G':
            RB[r][c] = 1
            RGB[r][c] = 2

RGB_visited=[[0]*N for _ in range(N)]
RB_visited=[[0]*N for _ in range(N)]

red = 1
green = 2
blue = 0


red_cnt = green_cnt = blue_cnt = 0
for r in range(N):
    for c in range(N):
        if RGB[r][c]==red and RGB_visited[r][c]==0:
            red_cnt += BFS(RGB,RGB_visited,[r,c],red)
        elif RGB[r][c]==green and RGB_visited[r][c]==0:
            green_cnt += BFS(RGB,RGB_visited,[r,c],green)
        elif RGB[r][c]==blue and RGB_visited[r][c]==0:
            blue_cnt += BFS(RGB,RGB_visited,[r,c],blue)

RB_red_cnt = RB_blue_cnt = 0
for r in range(N):
    for c in range(N):
        if RB[r][c]==red and RB_visited[r][c]==0:
            RB_red_cnt += BFS(RB,RB_visited,[r,c],red)
        elif RB[r][c]==blue and RB_visited[r][c]==0:
            RB_blue_cnt += BFS(RB,RB_visited,[r,c],blue)



print(red_cnt+green_cnt+blue_cnt, RB_red_cnt+RB_blue_cnt)