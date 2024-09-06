N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

lst.sort(key= lambda x: (x[0], x[1]))

for l in lst:
    print(*l)