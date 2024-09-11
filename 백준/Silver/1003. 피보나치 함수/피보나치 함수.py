## 시간 초과
# def fibonacci(n):
#     global call_0, call_1
#     if n == 0:
#         call_0 += 1
#         return 0
    
#     elif n == 1:
#         call_1 += 1
#         return 1
    
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
T = int(input())

for _ in range(T):
    N = int(input())
    call_0, call_1 = 1, 0

    for i in range(1, N+1):
        call_0, call_1 = call_1, call_0 + call_1

    # fibonacci(N)
    print(call_0, call_1)