def backtracking(row):
    global cnt

    if row == N:
        cnt+=1
        return
    
    for c in range(N):
        if check_c[c]==False and check_up[row+c]==False and check_down[(N-1)+row-c]==False:
            check_c[c]=True
            check_up[row+c]=True
            check_down[(N-1)+row-c]=True
            backtracking(row+1)
            check_c[c]=False
            check_up[row+c]=False
            check_down[(N-1)+row-c]=False


N = int(input())
board = [[0]*N for _ in range(N)]

check_c = [False]*N
check_up = [False]*(2*(N-1)+1)
check_down = [False]*(2*(N-1)+1)

cnt = 0
backtracking(0)
print(cnt)