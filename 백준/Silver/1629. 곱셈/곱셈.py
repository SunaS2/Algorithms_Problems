import sys
input = sys.stdin.readline
def exp(N, M, K):
    if M == 1:
        return N%K

    x = exp(N,M//2,K)
    if M % 2 == 1:
        return ((x*x)%K) * N%K
    else:
        return (x*x)%K

N, M, K = map(int,input().strip().split())
print(exp(N,M,K))