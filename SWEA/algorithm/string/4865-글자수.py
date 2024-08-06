def my_max(lst):
    max_value = lst[0]
    for l in lst:
        if max_value < l:
            max_value = l
    return max_value

T = int(input())
for tc in range(1,T+1):
    str1=input()
    str2=input()

    cnt_lst = []
    
    for i in str1:
        cnt = 0
        for j in str2:
            if i==j:
                cnt+=1
        cnt_lst.append(cnt)
    
    result = my_max(cnt_lst)

    print(f'#{tc} {result}')