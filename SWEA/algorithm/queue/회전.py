# def en_queue(data):
#     global n, rear
#     rear = (rear+1) % n
#     myqueue[rear] = data

# def de_queue():
#     global n,front
#     front = (front+1) % n
#     return myqueue[front]

T = int(input())

for tc in range(1,T+1):
    n, m = map(int,input().split())
    lst = list(map(int,input().split()))

    # front = rear = 0
    # myqueue = [None] * n

    # for l in lst:
    #     en_queue(l)

    print(f'#{tc} {lst[m%n]}')
        
