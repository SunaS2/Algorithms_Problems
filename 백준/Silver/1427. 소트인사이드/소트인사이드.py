def mysort(lst): #count 정렬, 각 자리 수는 0~9로 한정되어 있기 때문
    cnt = [0] * 10
    for l in lst:
        cnt[l] += 1

    for i in range(len(cnt)-2,-1,-1):
        cnt[i] += cnt[i+1]

    result = [0] * len(lst)
    for idx in range(len(lst)-1,-1,-1):
        cnt[lst[idx]] -= 1
        result[cnt[lst[idx]]] = lst[idx]

    return result




lst = list(map(int,input()))
sorted_lst = list(map(str,mysort(lst)))

print(''.join(sorted_lst))
