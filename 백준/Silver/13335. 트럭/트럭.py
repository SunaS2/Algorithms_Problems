from collections import deque
import sys
input = sys.stdin.readline

N, W, L = map(int,input().strip().split())
trucks = list(map(int,input().strip().split()))

q = deque()
for _ in range(W):
    q.append(0)

time = 0

idx = 0
while idx < N:
    time += 1
    q.popleft()
    # 맨 앞 차가 다리를 벗어남

    # 아직 다리에 있는 차들 + 새로운 차 -> 하중이 버틸 수 있다?
    if sum(q)+trucks[idx] <= L:
        # 새 트럭 드루와
        q.append(trucks[idx])
        # 다음 트럭 넘버
        idx += 1
    # 하중이 안되면 일단 기다려... (0 넣어서 다리 길이만 유지)
    else:
        q.append(0)

# idx를 다 사용하고 나면 큐가 빌 때까지 시간을 세어 준다
while q:
    time += 1
    q.popleft()

print(time)