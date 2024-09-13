# def selection_sort(lst):
#     for i in range(N):
#         min_idx = i
#         for j in range(i,N):
#             if lst[min_idx] > lst[j]:
#                 min_idx = j
#         lst[i],lst[min_idx] = lst[min_idx], lst[i]
#
#     return lst

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()

for i in range(N):
    print(lst[i])