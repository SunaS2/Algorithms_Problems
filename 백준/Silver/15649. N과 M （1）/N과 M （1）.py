def backtrack(row, m):
    if row == m:
        print(*result)
        return

    for i in range(len(lst)):
        if check[i] == False:
            check[i] = True #방문했어요 방명록 작성
            result[row] = lst[i] #이번 스텝의 결과 리스트에 고른 순열 담기
            backtrack(row+1,m) #다음 스텝으로 넘어가기
            check[i] = False #다음 스텝에 갔다가 돌아오면 나가기 체크아웃
            result[row] = 0 #체크아웃 하면서 결과 리스트도 원상복구 시키기

n, m = map(int,input().split())
check = [False] * n
lst = [x for x in range(1,n+1)]
result = [0] * m

backtrack(0,m)