def backtrack(k):
    if k == M:
        print(*result)
        return
    
    for i in range(N):
        if visited[i]==0:
            result.append(lst[i])
            visited[i] = 1
            backtrack(k+1)
            visited[i] = 0
            result.pop()


N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

result = []
visited = [0] * N

backtrack(0)