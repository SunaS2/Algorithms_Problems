import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
arr_sorted = sorted(list(set(arr)))

ditList = dict(zip(arr_sorted, list(range(len(arr_sorted)))))

result = [0] * N
for i in range(N):
    result[i] = ditList[arr[i]]

print(*result)