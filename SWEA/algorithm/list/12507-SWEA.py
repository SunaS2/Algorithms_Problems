def binarysort(page,key):
    l = 1
    r = page
    count_finding = 0
    while l <= r:
        c = int((l+r)/2)
        count_finding +=1
        if c == key:
            return count_finding
        elif c > key:
            r = c
        elif c < key:
            l = c
    
T = int(input())

for tc in range(1,T+1):
    p, a, b = tuple(map(int,input().split()))
    #book = [x for x in range(1,p+1)]

    
    count_a = binarysort(p, a)
    count_b = binarysort(p, b)



    if count_a < count_b:
        print(f'#{tc} A')
    elif count_a > count_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')
