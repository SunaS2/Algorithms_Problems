def DFS(s,g):
    stack = []
    visited = [0]*(N+1)
    stack.append(s)
    visited[s] = 1
    now = s

    while True:
        for w in adjL[now]:
            if visited[w]==0:
                stack.append(w)
                visited[w] = visited[now] + 1
                break
        else:
            if stack:
                now = stack.pop()
            else:
                break
    
    if visited[g]:
        return visited[g] - 1
    else:
        return -1

N = int(input())
S,G = map(int,input().split())
M = int(input())
family = [list(map(int,input().split())) for _ in range(M)]

adjL = [[] for _ in range(N+1)]
for i in range(M):
    a1 = family[i][0]
    a2 = family[i][1]

    adjL[a1].append(a2)
    adjL[a2].append(a1)

print(DFS(S,G))
