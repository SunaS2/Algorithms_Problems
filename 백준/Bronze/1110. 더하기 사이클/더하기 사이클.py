N = int(input())
number = N
cnt = 0

while True:
    A = number // 10 # n의 10의자리 수
    B = number % 10 # n의 1의자리 수
    C = (A + B) % 10 # 새로운 수의 1의자리 수, A + B 가 10 이상일 경우까지 생각

    number = B * 10 + C
    cnt += 1
    
    if N == number:
        break

print(cnt)