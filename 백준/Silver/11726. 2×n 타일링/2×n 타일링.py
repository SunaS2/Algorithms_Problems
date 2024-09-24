def solv(n):
    if n >= len(memo):
        memo.append(solv(n-1)+solv(n-2))
    return memo[n]

N = int(input())
memo = [0,1,2]
print(solv(N)%10007)