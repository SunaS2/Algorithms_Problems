N = int(input()) # 사람 수 N
times = sorted(map(int, input().split())) # 걸리는 시간
# 필요한 시간의 합의 최솟값을 구해야한다 => 오름차순으로 정렬
ans = 0

for i in range(1, N+1): # 1번부터 N번까지
    ans += sum(times[:i]) # i번 사람까지 걸리는 시간의 합을 누적

print(ans)