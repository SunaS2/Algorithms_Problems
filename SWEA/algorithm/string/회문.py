def ismirror(lst):
    mid = len(lst)//2
    count = 0
    for i in range(0,mid):
        if lst[i]==lst[len(lst)-1-i]:
            count+=1
    
    if count == mid:
        return True
    else:
        return False

T = int(input())

for tc in range(1,T+1):
    n, m = tuple(map(int, input().split()))
    string = [list(input()) for _ in range(n)]

    #가로에서 회문 찾기
    for r in range(n):
        for c in range(0,(n-m)+1):
            temp = string[r][c:c+m]
            if ismirror(temp)==True:
                answer = temp

    #세로 가로 바꾸기
    for r in range(n):
        for c in range(n):
            if r<c:
                string[r][c],string[c][r] = string[c][r],string[r][c]
    
    #세로(가로)에서 회문 찾기
    for r in range(n):
        for c in range(0,(n-m)+1):
            temp = string[r][c:c+m]
            if ismirror(temp)==True:
                answer = temp

    print(f'#{tc} {"".join(answer)}')
