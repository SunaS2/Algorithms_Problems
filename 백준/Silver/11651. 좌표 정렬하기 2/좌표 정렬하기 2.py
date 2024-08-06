n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

lst.sort(key=lambda x:(x[1],x[0]))
for i in range(len(lst)):
	temp = list(map(str,lst[i]))
	print(' '.join(temp))