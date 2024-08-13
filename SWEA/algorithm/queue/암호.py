def en_queue(data):
    global n, rear
    rear = (rear+1) % n
    myqueue[rear] = data

def de_queue():
    global n,front
    front = (front+1) % n
    return myqueue[front]

T = 10
for t in range(1,T+1):
    tc = int(input())
    lst = list(map(int,input().split()))
    n = 8
    front, rear = 0, 0
    myqueue = [None] * n

    for l in lst:
        en_queue(l)

    front = 0
    i = 1
    while myqueue[front%n] >= 0:
        if i == 6:
            i = 1
        new = de_queue() - i
        if new <= 0:
            en_queue(0)
            break
        en_queue(new)
        i += 1

    new_lst = []
    for i in range(n):
        if myqueue[i] <= 0:
            new_lst = myqueue[i+1:]+ myqueue[:i+1]

    new_lst = list(map(str,new_lst))
    print(f'#{tc} {" ".join(new_lst)}')
    


