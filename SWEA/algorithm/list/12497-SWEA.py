from pprint import pprint as print

T = int(input())

for tc in range(1,T+1):
    num_area = int(input())
    color_area = [0]*num_area

    all_matrix = [[0]*10 for _ in range(10)]

    for i in range(num_area):
        color_area[i]=list(map(int,input().split()))
    

    for area in color_area:
        width = [area[0],area[2]]
        height = [area[1],area[3]]
        color = area[4]
        for i in range(height[0],height[1]+1):
            for j in range(width[0],width[1]+1):
                all_matrix[i][j]+=color

    count_purple = 0
    for i in range(10):
        for j in range(10):
            if all_matrix[i][j] == 3:
                count_purple += 1

    print(f'#{tc} {count_purple}')