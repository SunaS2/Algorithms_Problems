from heapq import heappop, heappush
N = int(input())

q = []
for _ in range(N):
    lst = list(map(int,input().split()))

    if not q: # 빈 q에 첫 번째 입력 시
        for x in lst:
            heappush(q,x)

    else: # 그게 아니라면..
        for x in lst: # n으로 queue 길이를 N으로 유지한다.
            if q[0] < x: # q의 최솟값보다 현재 수가 더 크면 현재수 push, 기존 최솟값 pop
                heappush(q,x)
                heappop(q)

print(q[0])
