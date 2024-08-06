T = int(input())
for tc in range(1,T+1):
    string, key = input().split()
    
    i=0
    key_cnt = 0

    while i<len(string):
        if string[i:i+len(key)]==key:
            key_cnt+=1
            i+=len(key)
        else:
            key_cnt+=1
            i += 1
    print(f'#{tc} {key_cnt}')
