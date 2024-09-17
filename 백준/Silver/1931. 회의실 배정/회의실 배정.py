N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int,input().split())))

lst.sort(key=lambda x : (x[1],x[0]))
cnt = 0
end = -1
for l in lst:
    if l[0] >= end:
        cnt += 1
        end = l[1]

print(cnt)