def combination(k,start,result):
    if k == 3:
        # 3장이 안넘게
        hap.append(sum(result))
        return

    for i in range(start,N):
        if visited[i] == 0 and sum(result)+cards[i] <= M:
            visited[i] = 1
            result.append(cards[i])
            combination(k+1,start+1,result)
            visited[i] = 0
            result.pop()

N, M = map(int,input().split())
cards = list(map(int,input().split()))

visited = [0] * N
hap = []
combination(0,0,[])
print(max(hap))