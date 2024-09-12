N = int(input())
lst = []
for _ in range(N):
    lst.append(input())

lst = list(set(lst))
lst.sort(key=lambda x:(len(x),x))

for i in range(len(lst)):
    print(lst[i])