def my_max(lst):
    if len(lst)==1:
        return lst[0]
    else:
        max_value = lst[0]
        for l in lst:
            if max_value < l:
                max_value = l
        return max_value

def my_min(lst):
    if len(lst)==1:
        return lst[0]
    else:
        min_value = lst[0]
        for l in lst:
            if min_value > l:
                min_value = l
        return min_value
T=int(input())

for tc in range(1,T+1):
    num = int(input())
    num_lst = list(map(int,input().split()))

    min_num = my_min(num_lst)
    max_num = my_max(num_lst)

    print(f'#{tc} {max_num-min_num}')