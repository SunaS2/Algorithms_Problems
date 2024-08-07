n = int(input())
a = list(map(int,input().split()))

sortA = sorted(a)

p = []

for i in range(n):
    p.append(sortA.index(a[i]))
    sortA[sortA.index(a[i])] = -1


print(*p)