from heapq import heappop, heappush
import sys

input = sys.stdin.readline

def dijkstra(start, time):
    q = []
    heappush(q,(time, start))
    memo[start] = 0

    while q:
        t, now = heappop(q)

        if memo[now] < t:
            continue

        for move in ((1, now - 1), (1, now + 1), (0, now * 2)):
            if 100000 >= move[1] >= 0 and memo[move[1]] > move[0]+t:
                heappush(q,(move[0]+t,move[1]))
                memo[move[1]] = move[0]+t


N, K = map(int, input().strip().split())
memo = [float('inf')] * 100001
dijkstra(N, 0)
print(memo[K])