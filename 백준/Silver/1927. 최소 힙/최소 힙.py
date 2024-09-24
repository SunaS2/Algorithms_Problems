from heapq import heapify, heappop, heappush
import sys

input = sys.stdin.readline

N  = int(input())
pq = []
heapify(pq)
for _ in range(N):
    x = int(input())
    if x == 0 and pq:
        print(heappop(pq))
    elif x > 0:
        heappush(pq,x)
    else:
        print(0)