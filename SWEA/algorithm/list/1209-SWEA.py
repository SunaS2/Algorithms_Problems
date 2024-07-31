def my_max(lst):
    max_value = lst[0]
    for l in lst:
        if max_value < l:
            max_value = l
    return max_value

T = 10

for tc in range(1,T+1):
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]

    sums_of_rows = [0]*N
    sums_of_columns = [0]*N

    for i in range(N): #열 -> 행
        sum_of_a_row = 0
        for j in range(N):
            sum_of_a_row += matrix[i][j]
        sums_of_rows[i] = sum_of_a_row
    
    for j in range(N):
        sum_of_a_column = 0
        for i in range(N):
            sum_of_a_column+=matrix[i][j]
        sums_of_columns[j] = sum_of_a_column
    
    sum_of_cross_to_right = 0
    for i in range(N):
        sum_of_cross_to_right+=matrix[i][i]
    
    sum_of_cross_to_left = 0
    for i in range(N-1,-1,-1):
        sum_of_cross_to_left+=matrix[i][i]

    sums_of_crosses = [sum_of_cross_to_left,sum_of_cross_to_right]

    all_sums = sums_of_rows + sums_of_columns + sums_of_crosses

    max_value = my_max(all_sums)

    print(f'#{tc} {max_value}')