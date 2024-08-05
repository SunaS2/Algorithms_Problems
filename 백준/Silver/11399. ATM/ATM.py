def selectionsort(lst,n):
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):


            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    return lst

N = int(input())
people = list(map(int, input().split()))

sorted_people = selectionsort(people,N)

result = 0
for i in range(N):
    wait=sum(sorted_people[:i+1])
    result+=wait

print(result)