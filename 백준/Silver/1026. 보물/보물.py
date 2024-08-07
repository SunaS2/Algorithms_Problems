n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

sortb = sorted(b,reverse=True)

idx = []
for i in range(n):
    idx.append(sortb.index(b[i]))
    sortb[sortb.index(b[i])] = -1

sorta = sorted(a)
result = [0]*n
for i in range(n):
    result[i] = sorta[idx[i]]

bomul = 0
for i in range(n):
    bomul += b[i] * result [i]

print(bomul)