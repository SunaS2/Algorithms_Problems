T = int(input())

for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int,input()))

    counts_lst = []
    counts = 0
    for x in lst:
        if x == 0:
            counts = 0
        if x == 1:
            counts += 1
        counts_lst.append(counts)

    max_value = 0
    for i in counts_lst:
        if max_value < i:
            max_value = i
    
    print(f'#{tc} {max_value}')