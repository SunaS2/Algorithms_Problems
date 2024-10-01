N, M = map(int,input().split())
trees = tuple(map(int,input().split()))

left = 0
right = max(trees)

while left <= right:
    mid = (left+right)//2

    cutted = 0
    for tree in trees:
        if tree >= mid:
            cutted += tree-mid

    if cutted >= M:
        left = mid+1
    else:
        right = mid-1

print(right)