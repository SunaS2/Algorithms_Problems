import sys
input = sys.stdin.readline

N,M = map(int,input().split())
not_see = set()
not_heard = set()

for _ in range(N):
    not_heard.add(input().strip())

for _ in range(M):
    not_see.add(input().strip())

result = list(not_heard.intersection(not_see))
print(len(result))
result.sort()
for r in result:
    print(r)