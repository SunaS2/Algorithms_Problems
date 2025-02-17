from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(apt, a, b):
    n = len(apt)
    queue = deque()
    queue.append((a, b))
    apt[a][b] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if apt[nx][ny] == 1:
                apt[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count


n = int(input())
apt = []
for i in range(n):
    apt.append(list(map(int, input())))

cnt = []
for i in range(n):
    for j in range(n):
        if apt[i][j] == 1:
            cnt.append(bfs(apt, i, j))

cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])