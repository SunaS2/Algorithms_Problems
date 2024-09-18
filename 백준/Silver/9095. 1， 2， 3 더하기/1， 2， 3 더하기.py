def solv(n):
    if n <= 3:
        return d[n]
    else:
        for i in range(4,n+1):
            d[i] = d[i-1]+d[i-2]+d[i-3]

        return d[n]
T = int(input())
for _ in range(T):
    N = int(input())
    d = [0] * 12
    d[1] = 1
    d[2] = 2
    d[3] = 4

    print(solv(N))