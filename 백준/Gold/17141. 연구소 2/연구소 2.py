def find_starts(arr):
    starts = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                starts.append((i,j))
    
    return starts

from collections import deque
from unittest import result

dr = (-1,1,0,0)
dc = (0,0,-1,1)

def BFS(starts):
    q = deque(starts)
    visited = check_wall(laboratory)
    for s in starts:
        visited[s[0]][s[1]] = 1

    while q:
        now = q.popleft()

        for d in range(4):
            nr = now[0] + dr[d]
            nc = now[1] + dc[d]
            if 0<=nr<N and 0<=nc<N and (laboratory[nr][nc] == 0 or laboratory[nr][nc] == 2) and visited[nr][nc] == 0:
                q.append((nr,nc))
                visited[nr][nc] = visited[now[0]][now[1]] + 1
            elif 0<=nr<N and 0<=nc<N and laboratory[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = '-'

    return find_min_sec(visited)

def find_min_sec(visited):
    min_sec = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                return -1
            elif visited[i][j] != '-':
                min_sec = max(min_sec, visited[i][j])
    return min_sec -1

def check_wall(arr):
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                visited[i][j] = '-'

    return visited


def combination(index, result=[], k=0):
    if k == M:
        # print(result)
        sec_result.append(BFS(result))
        return
    
    for i in range(index, len(starts)):
        if combi_visited[i] == 0:
            result.append(starts[i])
            combi_visited[i] = 1
            combination(i+1, result,k+1)
            result.pop()
            combi_visited[i] = 0


# 시작 위치 고르기 -> 조합
# 시작 위치를 골라서 q에 담아서 bfs 시작하기
# 가장 큰 visited 값을 찾아서 시간 갱신... 하고 list 넣기
# 다 돌고 나서 list에서 제일 작은 시간...(-1이 아닌) 찾아서 출력
# 모든 list가 -1이면 -1 출력
N, M = map(int,input().split())
laboratory = [list(map(int,input().split())) for _ in range(N)]

starts = find_starts(laboratory)
combi_visited = [0] * len(starts)

sec_result = []

combination(0)
sec_result = set(sec_result)

if len(sec_result) == 1 and  -1 in sec_result:
    print(-1)
elif -1 in sec_result:
    sec_result.remove(-1)
    print(min(sec_result))
else:
    print(min(sec_result))