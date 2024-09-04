T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    nums = input()

    passwords = set()

    for n in range(N//4):
        for i in range(0,N,N//4):
            passwords.add(nums[i:i+N//4])
        nums = nums[-1] + nums[:N-1]

    passwords=list(passwords)
    passwords.sort(reverse=True)

    result = passwords[K-1]
    result = int(result,16)

    print(f'#{tc} {result}')