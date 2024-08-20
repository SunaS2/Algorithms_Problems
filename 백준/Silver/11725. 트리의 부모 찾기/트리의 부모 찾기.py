def DFS(s):
    stack = []
    visited=[0]*(N+1)
    stack.append(s)
    visited[s] = 1
    now = s
    dfs = [0]*(N-1)
    while True:
        for w in adjL[now]:
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1
                dfs[w-2] = now
                break
        else:
            if stack:
                now = stack.pop()
            else:
                break
    return dfs



N = int(input())
arr = [list(map(int,input().split())) for _ in range(N-1)]
adjL = [[] for _ in range(N+1)]
for i in range(N-1):
    a1 = arr[i][0]
    a2 = arr[i][1]

    adjL[a1].append(a2)
    adjL[a2].append(a1)

d = DFS(1)

for x in d:
    print(x)