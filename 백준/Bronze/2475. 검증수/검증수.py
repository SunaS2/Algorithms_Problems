lst = list(map(int,input().split()))
result = 0
for n in lst:
    result += n**2
print(result%10)