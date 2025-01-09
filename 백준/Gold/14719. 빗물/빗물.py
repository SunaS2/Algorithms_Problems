H, W = map(int,input().split())
blocks = list(map(int,input().split()))

cnt = 0
for i in range(1,W-1):
    left = max(blocks[:i])
    right = max(blocks[i:])
    m = min(left,right)

    if m >= blocks[i]:
        cnt += (m-blocks[i])

print(cnt)