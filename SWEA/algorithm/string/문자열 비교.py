T= int(input())

for tc in range(1,T+1):
    short = input()
    long = input()

    len_shrt = len(short)
    len_lng = len(long)
    
    for x in range((len_lng-len_shrt)+1):
        if long[x:x+len_shrt] == short:
            result = 1
            break
        else:
            result = 0
    
    print(f'#{tc} {result}')

    # if short in long:
    #     print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')