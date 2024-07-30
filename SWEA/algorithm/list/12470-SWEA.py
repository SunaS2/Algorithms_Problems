T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cards = list(map(int,input()))

    counts = [0]*10

    for card in cards:
        counts[card] += 1

    max_num = 0
    for c in counts:
        if max_num < c:
            max_num = c

    for i in range(10):
        if counts[i] == max_num:
            card_number = i

    print(f'#{tc} {card_number} {max_num}')
