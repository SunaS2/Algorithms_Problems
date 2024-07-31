T = int(input())

for tc in range(1,T+1):
    n, k = tuple(map(int,input().split()))
    my_set = [x for x in range(1,13)]

    lst_subset = []
    for i in range(1<<len(my_set)):
        subset = []
        for j in range(len(my_set)):
            if i & (1<<j):
                subset.append(my_set[j])
        if len(subset) == n:
            lst_subset.append(subset)
    
    count_k = 0
    for ls in lst_subset:
        sum_of_subset = 0
        for i in range(n):
            sum_of_subset += ls[i]
        if sum_of_subset == k:
            count_k += 1

    print(f'#{tc} {count_k}')
