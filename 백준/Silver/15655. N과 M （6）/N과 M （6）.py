def backtracking(k,now=0):
    if k == M:
        print(*result)
        return

    for i in range(now,N):
        if visited[i] == 0:
            result.append(lst[i])
            visited[i] = 1
            backtracking(k+1,i+1)
            visited[i] = 0
            result.pop()



N, M = map(int,input().split())
# N개의 자연수 중에서 M 개를 고른 순열
lst = list(map(int,input().split()))
lst.sort()

visited = [0] * N
result = []
now = lst[0]
backtracking(0)