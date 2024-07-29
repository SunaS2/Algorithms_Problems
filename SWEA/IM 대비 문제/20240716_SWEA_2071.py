
T = 1 #int(input())
for tc in range(1, T+1):
    numbers = [1,2,3,4,5] #list(map(int, input().split()))
    hap=0
    for i in range(len(numbers)):
        hap=hap+numbers[i]

    avg = hap/10

    print(f"#{tc} {round(avg)}")