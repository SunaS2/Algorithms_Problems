def cardgame(lst,start,end):
    
    if start == end:
        return start
    elif start+1 == end:
        winner = rsp(lst,start,end)
        return winner
    else:
        mid = (start+end)//2
        winner1 = cardgame(lst,start,mid)
        winner2 = cardgame(lst,mid+1,end)

        final_winner = rsp(lst,winner1,winner2)
        return final_winner

def rsp(lst,right, left):
    if lst[right] == 1 and lst[left]==3:
        return right
    elif lst[left] == 1 and lst[right] == 3:
        return left
    elif lst[right] == 3 and lst[left]==2:
        return right
    elif lst[left] == 3 and lst[right] == 2:
        return left
    elif lst[right] == 2 and lst[left]==1:
        return right
    elif lst[left] == 2 and lst[right] == 1:
        return left
    else:
        return right

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    cards = list(map(int,input().split()))

    print(f'#{tc} {cardgame(cards,0,n-1)+1}')
