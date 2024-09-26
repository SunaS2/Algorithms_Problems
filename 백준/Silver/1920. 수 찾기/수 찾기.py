def binary_search(key,left,right):
    if left > right:
        return 0
    
    mid = (left+right)//2

    if A[mid]==key:
        return 1
    elif A[mid] < key:
        return binary_search(key,mid+1,right)
    else:
        return binary_search(key,left,mid-1)

N = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
lst = list(map(int,input().split()))
for x in lst:
    print(binary_search(x,0,N-1))
