# backtracking으로 타순을 만든다 -> 1번 선수는 4번 타자 고정 8번돌려서 순서 만듬, 선수 번호 = idx
# idx(선수 번호)로 타순을 정한다.
# 순서가 만들어지면 한 이닝 경기를 함
# 한 이닝이 끝나기 위해서는 아웃카운트 3이 되어야함 -> while문과 타순 mod 연산자로 야구 시행
# 각 이닝마다 선수가 어떤 경기를 진행하는지는 입력값을 참고해야한다.
# 각 타순 마다 점수를 세어서, 가장 큰 점수를 출력한다.
def baseball(hitter_order):
    global score
    idx = 0 # 타석 수
    for inning in range(N): # 경기 시작, inning 은 현재 이닝 표기
        out_count = 0 # 이닝 종료를 알리는 out_count
        home, base1, base2, base3 = 0,False,False,False # 각 base에 사람이 있는지 없는지 표시
        while out_count < 3: # out_count가 3이면 경기 종료
            # 경기 시작
            # 타석에 선수가 들어섰었다(맨 아래에 선언)
            hitter = hitter_order[idx%9] # 현재 타석에 선 선수의 번호(idx가 계속 커지면 mod 연산자로 접근)
            hit = ability[inning][hitter] # 현재 선수가 이번 이닝에서 어떤 결과를 가져오는가
            if  hit == 0:
                # 주자가 아웃 된다
                out_count += 1
            elif 1 <= hit <= 3:
                # 안타를 쳤다
                if hit == 1:
                    home += base3
                    base1, base2, base3 = True, base1, base2
                elif hit == 2:
                    home += base3
                    home += base2
                    base1, base2, base3 = False, True, base1
                elif hit == 3:
                    home += base3
                    home += base2
                    home += base1
                    base1, base2, base3 = False, False, True
                score += home
                home = 0
            elif hit == 4:
                # 홈런을 쳤다
                score += base1 + base2 + base3 + 1
                home, base1, base2, base3 = 0, False, False, False  # 그라운드 초기화
            idx += 1
def backtracking(k):
    global max_score, score
    if k == 8:
        hitter_order_result = hitter_order[:]
        hitter_order_result.insert(3,0) # 1번 선수의 자리 4번에 넣어줌
        baseball(hitter_order_result)
        if max_score < score:
            max_score = score
        score = 0
        return
    
    for i in range(1,9): # 1번 선수는 이미 4번 타자로 고정이므로, 나머지 선수들의 타순 정하기
        if visited[i] == 0:
            visited[i] = 1
            hitter_order.append(i)
            backtracking(k+1)
            hitter_order.pop()
            visited[i] = 0

N = int(input())
ability = [list(map(int,input().split())) for _ in range(N)]
# 각 이닝 마다 선수들의 경기력을 보여줌
# ability[1][3] -> 1회에서 4번 선수의 경기력

visited = [0] * 9
hitter_order = []
score = 0
max_score = 0

backtracking(0)
print(max_score)