def my_max(lst):
    max_value = 0
    for l in lst:
        if max_value < l:
            max_value = l
    return max_value

for tc in range(1,11):

    N = int(input())
    buildings = list(map(int,input().split()))

    have_view = []
    for i in range(2,N-2):
        near_buildings = []

        me = buildings[i]
        near_buildings.append(buildings[i-2])
        near_buildings.append(buildings[i-1])
        near_buildings.append(buildings[i+1])
        near_buildings.append(buildings[i+2])

        highest_except_me = my_max(near_buildings)
        

        if me - highest_except_me > 0:
            have_view.append(me - highest_except_me)
        else:
            have_view.append(0)

    total = 0

    for view in have_view:
        total += view
    
    print(f'#{tc} {total}')

