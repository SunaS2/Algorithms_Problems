import sys
input = sys.stdin.readline

from heapq import heappop, heappush

start = (0,0)
dr = (-1,0,1,0)
dc = (0,1,0,-1)

tc = 0

def dij(weight, start):
    q = []
    heappush(q,(weight,start))
    distance[start[0]][start[1]] = weight

    while q:
        weight, now = heappop(q)

        now_r = now[0]
        now_c = now[1]


        for d in range(4):
            nr = now_r + dr[d]
            nc = now_c + dc[d]

            if 0<=nr<N and 0<=nc<N:
                # if distance[nr][nc] < weight:
                #     continue
                next_cost = cave[nr][nc]
                if distance[nr][nc] > weight + next_cost:
                    heappush(q,(weight+next_cost, (nr,nc)))
                    distance[nr][nc] = weight + next_cost

while True:
    N = int(input())
    tc += 1
    if N == 0:
        break

    cave = [tuple(map(int,input().strip().split())) for _ in range(N)]

    distance = [[float('inf')]*N for _ in range(N)]
    dij(cave[0][0], start)
    result = distance[N-1][N-1]

    print(f'Problem {tc}: {result}')
