def highest(boxs):
    max_box = boxs[0]
    idx_of_highst = 0
    for i in range(len(boxs)):
        if max_box < boxs[i]:
            max_box = boxs[i]
            idx_of_highst = i

    return idx_of_highst

def lowest(boxs):
    min_box = boxs[0]
    idx_of_lowest = 0
    for i in range(len(boxs)):
        if min_box > boxs[i]:
            min_box = boxs[i]
            idx_of_lowest = i
    
    return idx_of_lowest

T = 10

for tc in range(1,T+1):
    N = int(input())
    boxs = list(map(int,input().split()))

    for i in range(N):
        i = highest(boxs)
        j = lowest(boxs)

        boxs[i] -= 1
        boxs[j] += 1

        h=boxs[highest(boxs)]
        l=boxs[lowest(boxs)]

        if h - l <= 1:
            break

    print(f'#{tc} {h-l}')