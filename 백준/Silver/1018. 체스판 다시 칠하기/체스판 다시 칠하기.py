
def count_recoloring(start_r,start_c):
    W_cnt = 0
    B_cnt = 0
    for r in range(start_r,start_r+8):
        for c in range(start_c,start_c+8):
            if (r+c) % 2 == 0:
                if board[r][c] != 'B':
                    B_cnt += 1
                if board[r][c] != 'W':
                    W_cnt += 1
            else:
                if board[r][c] != 'B':
                    W_cnt += 1
                if board[r][c] != 'W':
                    B_cnt += 1

    result.append(W_cnt)
    result.append(B_cnt)

N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]

result= []
for r in range(N-7):
    for c in range(M-7):
        count_recoloring(r,c)

print(min(result))