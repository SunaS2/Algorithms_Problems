# def dec_sort(lst):
#     for i in range(len(lst),0,-1):
#         for j in range(0,i-1):
#             temp = 0
#             if lst[j] < lst[j+1]:
#                 temp = lst[j]
#                 lst[j] = lst[j+1]
#                 lst[j+1] = temp
#     return lst

# def asc_sort(lst):
#     for i in range(len(lst),0,-1):
#         for j in range(0,i-1):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst
def my_max(lst):
    max_v = lst[0]
    for i in range(len(lst)):
        if max_v < lst[i]:
            max_v = lst[i]

    return max_v

def my_min(lst):
    min_v = lst[0]
    for i in range(len(lst)):
        if min_v > lst[i]:
            min_v = lst[i]

    return min_v

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    lst = list(map(int,input().split()))

    # asc = asc_sort(lst)
    # dec = dec_sort(lst)

    result = [0] * n

    for i in range(n):
        if i % 2 == 0:
            result[i]=my_max(lst)
            lst.remove(result[i])
        else:
            result[i]=my_min(lst)
            lst.remove(result[i])

    result = [str(x) for x in result[0:10]]
    
    print(f"#{tc} {' '.join(result)}")

    # print(asc, dec)

    # for i in range(n//2+1):
    #     if i % 2 == 0:
    #         result[i*2] = dec[i]
    # for i in range(n//2+1):
    #     if i % 2 == 1:
    #         result[(2*i)+1] = asc[i]