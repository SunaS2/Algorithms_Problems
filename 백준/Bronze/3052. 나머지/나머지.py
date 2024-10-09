lst = [0] * 42

for _ in range(10):
    x = int(input())
    idx = x % 42
    lst[idx] += 1

result = 0
for i in range(42):
    if lst[i] > 0:
        result += 1

print(result)