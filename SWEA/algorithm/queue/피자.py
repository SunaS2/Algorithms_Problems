def en_queue(cheese):
    global n, rear
    rear = (rear+1) % n
    oven[rear] = cheese

def de_queue():
    global n,front
    front = (front+1) % n
    return oven[front]

T = int(input())
for tc in range(1,T+1):
    n,m = map(int, input().split())
    pizzas = list(map(int,input().split()))

    pizzas_w_num = []
    for i in range(m):
        pizzas_w_num.append([pizzas[i], i])

    rear = front = 0
    oven = [None] * n

    #1번 자리에 오면 pizza//=2
    #1번에 와서 피자가 녹았다? 0이다? 그럼 다른 피자 투입
    for i in range(n):
        en_queue(pizzas_w_num[i])
    
    print(oven)
    cnt = 0
    #오븐 한바퀴
    for j in range(m):
        for i in range(n):
            oven[i][0]//=2
            if oven[i][0]==0 and cnt+n <m:
                oven[i]=pizzas_w_num[n+cnt]
                cnt+=1
            print(oven)

