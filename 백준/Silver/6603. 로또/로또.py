def lotto(arr, lst, index, cnt):
    if cnt == 6:
        print(*arr)
        return
    
    for i in range(index, len(lst)):
        arr[cnt] = lst[i]
        lotto(arr, lst, i+1, cnt+1)

while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break

    arr = [0] * 6
    lotto(arr, lst[1:], 0, 0)
    print()