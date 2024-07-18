T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    hap = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            hap += numbers[i]

    print(f"#{tc} {hap}")