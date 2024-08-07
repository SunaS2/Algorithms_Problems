def DFS(s): #s: 시작 정점 v: 정점 개수 혹은 1번부터인 정점의 마지막 정점
    visited = [0]*(100) #방문 정점 표시
    stack=[] #스택 생성
    visited[s] = 1 #시작정점 방문 표시
    n = s
    while True:
        #n에 인접하고, 방문 안한 w가 있으면
        for w in data[n]:
            if visited[w]==0:
                stack.append(n) #현재 정점을 push하고
                n = w #w에 방문
                visited[w] = 1 #w에 방문 표시
                break # for w에 대한 break v부터 다시 탐색
        else: #남은 인접 정점이 없어서 for 가 break가 걸리지 않은 경우
            if stack:
                n = stack.pop()
            else:
                break #while의 break
    return visited[99]

T = 10
for t in range(1,T+1):
    tc, e = map(int,input().split())
    arr = list(map(int,input().split()))
    data = [[] for _ in range(100)]
    s = 0
    g = 99

    for i in range(e):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        data[v1].append(v2) #단방향
    # for i in range(e):
    #     v1, v2 = arr[i * 2], arr[i * 2 + 1]
    #     if data[0][v1] == 0:
    #         data[0][v1] = v2
    #     else:
    #         data[1][v1] = v2

    print(f'#{tc} {DFS(s)}')