def backtrack(start,s):
    global cnt
    if sum(subset) == s and len(subset) > 0:
        cnt += 1

    for i in range(start,N):
        subset.append(lst[i])
        backtrack(i+1,s)
        subset.pop()

N, S = map(int,input().split())
lst = list(map(int,input().split()))

cnt = 0
subset = []

backtrack(0,S)
print(cnt)