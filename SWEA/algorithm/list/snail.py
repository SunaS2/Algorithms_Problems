T = int(input())

for tc in range(1,T+1):
    n = int(input())
    row,column = n, n

    
    snail = [[0]*n for _ in range(n)]

    r, c = 0,0
    num = 2
    snail[r][c] = 1
    while num <= n**2:
        while c+1<n and snail[r][c+1]==0:
            c+=1
            snail[r][c] = num        
            num += 1
        while r+1<n and snail[r+1][c]==0:
            r+=1
            snail[r][c] = num
            num += 1
        while c-1>=0 and snail[r][c-1]==0:
            c-=1
            snail[r][c] = num
            num += 1
        while r-1>=0 and snail[r-1][c]==0:
            r-=1
            snail[r][c] = num
            num += 1

    str_snail =''
    for i in range(len(snail)):
        for y in snail[i]:
            str_snail = str_snail + str(y) + ' '
        if i < n-1:
            str_snail = str_snail + '\n'
    
    print(f'#{tc}\n{str_snail}')