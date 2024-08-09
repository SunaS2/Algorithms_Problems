def backtrack(matrix,k,n): #k=현재 위치, n = 인덱스 개수
    c = [0] * n #인덱스 후보 만큼 리스트 만들기
    global min_hap
    global hap
    if k == n: #문제 없이 다 골랐으면 전체 합을 내놓아라
        min_hap = hap
        return
    else:
        ncandidates = construct_candidates(matrix,k,n,c)
        for i in range(ncandidates):
            if min_hap > hap+matrix[k][c[i]]:
                hap += matrix[k][c[i]]
                backtrack(matrix,k+1,n)
                hap -= matrix[k][c[i]]

def construct_candidates(matrix,k,n,c):
    column = [False] * (n+1)
    for i in range(n):
        column[i] = True

    ncandidates = 0
    for i in range(n):
        if column[i] == False:
            c[ncandidates] = i
            ncandidates += 1

    return ncandidates

T = int(input())

for tc in range(1,T+1):

    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    min_hap = 0xFFF
    hap = 0
    backtrack(matrix,0,N)

    print(min_hap)