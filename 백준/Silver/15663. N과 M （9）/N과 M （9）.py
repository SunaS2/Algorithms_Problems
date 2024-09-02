def backtrack(k,now = 0):
    if k == M:
        print(*result)
        return
    
    temp = 0
    for i in range(N):
        if temp != lst[i] and visited[i] == 0:
            result.append(lst[i])
            visited[i] = 1
            temp = lst[i]
            backtrack(k+1)
            result.pop()
            visited[i] = 0

N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
result = []
result_lst = []
visited = [0] * N

backtrack(0)