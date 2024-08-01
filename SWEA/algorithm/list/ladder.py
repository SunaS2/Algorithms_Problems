T=1

for t in range(1,T+1):
    tc = int(input())

    ladder_game = [list(map(int, input().split())) for _ in range(100)]

    #2를 찾는다
    destination = ladder_game[99].index(2)

    #도착 지점의 배열 인덱스는 [99][destinaiton]
    row = 98
    column = destination

    while row > 0:
        # 오른쪽으로 이동할 수 있는지 확인
        while column <= 99 and ladder_game[row][column + 1] == 1:
            column += 1

        # 왼쪽으로 이동할 수 있는지 확인
        while column >= 0 and ladder_game[row][column - 1] == 1:
            column -= 1

        # 위로 이동
        row -= 1
    
    print(row, column)