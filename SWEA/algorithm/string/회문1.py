def ismirror(string):
    cnt = 0
    for x in range(len(string)//2):
        if string[x] == string[len(string)-1-x]:
            cnt += 1
    if cnt == len(string)//2:
        return True
    else:
        return False

def tran(lst):
    for r in range(len(lst)):
        for c in range(len(lst)):
            if r<c:
                lst[r][c], lst[c][r] = lst[c][r], lst[r][c]
    
    return lst

T = 1
for tc in range(1,T+1):
    n = int(input())
    matrix = [list(input()) for _ in range(8)]

    count = 0
    for r in range(8):
        for c in range(8-n+1):
            if ismirror(matrix[r][c:c+n])==True:
                count += 1
    
    matrix = tran(matrix)
    
    for r in range(8):
        for c in range(8-n+1):
            if ismirror(matrix[r][c:c+n])==True:
                count += 1
                
    print(f'#{tc} {count}')