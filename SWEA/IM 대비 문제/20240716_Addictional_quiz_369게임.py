#369 게임
# 1부터 n까지의 숫자를 하나씩 대면서 3, 6, 9가 들어가는 숫자에는
# 숫자를 출력하는 대신 그 갯수 만큼 "짝"을 치도록 출력을 해보시오.
#
# <입력>
# 15
#
# <출력>
# 1 2 짝 4 5 짝 7 8 짝 10 11 12 짝 14 15

i = int(input())

for x in range(1,i+1):
    x = str(x)
    count = 0
    if '3' in x or '6' in x or '9' in x:
        for y in x:
            if y in '369':
                count += 1
        x='짝'*count
    print(x, end=' ')
