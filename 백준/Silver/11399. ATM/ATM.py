N = int(input())
times = sorted(map(int, input().split()))
ans = 0

for i in range(N+1):
    ans += sum(times[:i])

print(ans)