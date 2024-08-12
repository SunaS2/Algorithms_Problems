n, k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

num_coins = 0
for i in range(n-1,-1,-1):
    num = k//coins[i]
    if num > 0:
        k -= coins[i]*num
        num_coins += num

print(num_coins)