N, K = map(int,input().split())

lst = [(0,0)]
for _ in range(N):
    W, V = map(int, input().split())
    lst.append((W,V))

dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1,N+1):
    w, v = lst[i]
    for j in range(1,K+1):
        if j >= w: # 현재 무게가 j보다 작거나 같을 때
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-w]+v)
        else: # 현재 무게가 j보다 클 때
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][K])