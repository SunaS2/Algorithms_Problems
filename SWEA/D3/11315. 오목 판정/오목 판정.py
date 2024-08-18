
T = int(input())
for tc in range(1,T+1):
    N = int(input()) #판 사이즈
    board = [list(input()) for _ in range(N)]
    r_result = False
    for r in range(N):
        temp = ''
        for c in range(N):
            temp = temp + board[r][c]
        if 'ooooo' in temp:
            r_result = True

    c_result = False
    for c in range(N):
        temp = ''
        for r in range(N):
            temp = temp + board[r][c]
        if 'ooooo' in temp:
            c_result = True

    cross_to_right_over = False
    d = [1,1]
    for c in range(N):
        r = 0
        temp = board[r][c]
        nr = r + d[0]
        nc = c + d[1]
        while 0<=nr<N and 0<=nc<N:
            temp = temp + board[nr][nc]
            nr += d[0]
            nc += d[1]

        if 'ooooo' in temp:
            cross_to_right_over = True

    cross_to_right_under = False
    for r in range(N):
        c = 0
        temp = board[r][c]
        nr = r + d[0]
        nc = c + d[1]
        while 0<=nr<N and 0<=nc<N:
            temp=temp+board[nr][nc]
            nr += d[0]
            nc += d[1]
        if 'ooooo' in temp:
            cross_to_right_under = True

    cross_to_left_over = False
    d = [1,-1]
    for c in range(N):
        r = 0
        temp = board[r][c]
        nr = r + d[0]
        nc = c + d[1]
        while 0<=nr<N and 0<=nc<N:
            temp=temp+board[nr][nc]
            nr += d[0]
            nc += d[1]
        if 'ooooo' in temp:
            cross_to_left_over = True

    cross_to_left_under = False
    for r in range(N):
        c = N-1
        temp = board[r][c]
        nr = r + d[0]
        nc = c + d[1]
        while 0 <= nr < N and 0 <= nc < N:
            temp = temp + board[nr][nc]
            nr += d[0]
            nc += d[1]
        if 'ooooo' in temp:
            cross_to_left_under = True

    if r_result or c_result or cross_to_left_under or cross_to_left_over or cross_to_right_over or cross_to_right_under:
        result = 'YES'
    else:
        result = 'NO'

    print(f'#{tc} {result}')
