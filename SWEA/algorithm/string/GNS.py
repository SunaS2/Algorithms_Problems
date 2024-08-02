def change_to_num(lst):
    num_lst = [0]*len(lst)
    for i in range(len(lst)):
        if lst[i] == 'ZRO':
            num_lst[i] = 0
        elif lst[i] == 'ONE':
            num_lst[i] = 1
        elif lst[i] == 'TWO':
            num_lst[i] = 2
        elif lst[i] == 'THR':
            num_lst[i] = 3
        elif lst[i] == 'FOR':
            num_lst[i] = 4
        elif lst[i] == 'FIV':
            num_lst[i] = 5
        elif lst[i] == 'SIX':
            num_lst[i] = 6
        elif lst[i] == 'SVN':
            num_lst[i] = 7
        elif lst[i] == 'EGT':
            num_lst[i] = 8
        elif lst[i] == 'NIN':
            num_lst[i] = 9
    return num_lst

def change_to_str(lst):
    num_lst = [0]*len(lst)
    for i in range(len(lst)):
        if lst[i] == 0:
            num_lst[i] = 'ZRO'
        elif lst[i] == 1:
            num_lst[i] = 'ONE'
        elif lst[i] == 2:
            num_lst[i] = 'TWO'
        elif lst[i] == 3:
            num_lst[i] = 'THR'
        elif lst[i] == 4:
            num_lst[i] = 'FOR'
        elif lst[i] == 5:
            num_lst[i] = 'FIV'
        elif lst[i] == 6:
            num_lst[i] = 'SIX'
        elif lst[i] == 7:
            num_lst[i] = 'SVN'
        elif lst[i] == 8:
            num_lst[i] = 'EGT'
        elif lst[i] == 9:
            num_lst[i] = 'NIN'
    return num_lst

def sorting(num_lst):
    for i in range(len(num_lst)):
        min_idx = i
        for j in range(i+1,len(num_lst)):
            if num_lst[min_idx] > num_lst[j]:
                min_idx = j
        temp = num_lst[i]
        num_lst[i] = num_lst[min_idx]
        num_lst[min_idx] = temp
    return num_lst

import sys
sys.stdin = open("GNS_test_input.txt","r")
T = int(input())

for t in range(1,T+1):
    tc,n = tuple(input().split())
    n = int(n)
    lst_string = list(map(str,input().split()))

    num_lst = change_to_num(lst_string)
    sorted_lst = sorting(num_lst)
    result = change_to_str(sorted_lst)

    print(tc)
    print(f'{" ".join(result)}')