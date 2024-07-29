def my_max(lst):
    max_l = 0
    for l in lst:
        if max_l < l:
            max_l = l
    return max_l

def my_min(lst):
    min_l = lst[0]
    for l in lst:
        if min_l >= l:
            min_l = l
    return min_l

T = int(input())

for tc in range(1,T+1):
    N, M = tuple(map(int,input().split()))
    num_lst = list(map(int,input().split()))

    hap = []
    for i in range(0,((N-M)+1)):
        a = 0
        for j in range(M):
            a += num_lst[i+j]
        hap.append(a)

    max_hap = my_max(hap)
    min_hap = my_min(hap)

    
    print(f'#{tc} {max_hap-min_hap}')
