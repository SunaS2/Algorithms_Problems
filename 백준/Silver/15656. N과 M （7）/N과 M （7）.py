def backtrack(k):
    if k == M:
        print(*result)
        return
    for i in range(N):
        result.append(lst[i])
        backtrack(k+1)
        result.pop()

N, M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

result = []

backtrack(0)