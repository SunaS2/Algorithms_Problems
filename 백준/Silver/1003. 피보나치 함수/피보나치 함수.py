import sys
input = sys.stdin.readline
def fibo(n):
    if n >= len(memo):
        memo.append(fibo(n-1)+fibo(n-2))
    return memo[n]

T = int(input())
for tc in range(1,T+1):
    N=int(input())
    memo = [0,1]
    zero = 0
    one = 0
    fibo(N)
    # if N > 0:
    #     zero = memo[N-1]
    #     one = memo[N]
    print(memo[N-1],memo[N])