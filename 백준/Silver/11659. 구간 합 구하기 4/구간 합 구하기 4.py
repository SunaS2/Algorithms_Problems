import sys
input = sys.stdin.readline

N, M = map(int,input().split())
lst = list(map(int,input().split()))
dp = [0]
mysum = 0

for i in range(N):
    mysum += lst[i]
    dp.append(mysum)

for _ in range(M):
    x, y = map(int,input().split())
    print(dp[y]-dp[x-1])