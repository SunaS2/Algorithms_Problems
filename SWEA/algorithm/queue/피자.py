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
    for i in range(1,m+1):
        pizzas_w_num.append([pizzas[i-1], i])
 
    rear = front = -1
    oven = [None] * n
 
    #1번 자리에 오면 pizza//=2
    #1번에 와서 피자가 녹았다? 0이다? 그럼 다른 피자 투입
    for i in range(n):
        en_queue(pizzas_w_num[i])
 
    cnt = 0
    #오븐 한바퀴
    escape = False
    for j in range(m):
        # 피자가 다 돌고, 녹지 않은 피자가 1개만 있는가?
        for i in range(n):
            oven[i][0]//=2
            # 치즈가 다 녹았고, 더 넣을 피자가 있으면 교체
            if oven[i][0]==0 and cnt+n <m:
                oven[i]=pizzas_w_num[n+cnt]
                # pizza_out += 1
                cnt+=1
            pizza_out = 0
            for k in range(n):
                if oven[k][0] == 0:
                    pizza_out += 1
            if pizza_out == n-1:
                escape = True
                break
        if escape == True:
            break
 
    for i in range(n):
        if oven[i][0] > 0:
            p = oven[i][1]
            print(f'#{tc} {p}')