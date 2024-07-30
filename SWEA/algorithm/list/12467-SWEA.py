T = int(input())

for tc in range(1, T+1):
    k, m, n = list(map(int,input().split()))
    chargers = list(map(int, input().split()))
    stops = [0]*(m+1)

    for charger in chargers:
        stops[charger] = 1

    
    charging = 0
    present_position = 0
    cannotgo = 0

    while present_position+k < m:
        previous_charging = present_position
        present_position += k
        if stops[present_position] == 1:
            charging += 1
            previous_charging = present_position
            continue
        else:
            count_charger = 0
            idx = 0
            for i in range(1,len(stops[previous_charging:present_position])):
                if stops[previous_charging+i] == 1:
                    count_charger += 1
                    idx = i
            if count_charger >= 1:
                present_position = previous_charging + idx
                charging += 1
            elif count_charger == 0:
                cannotgo = 1
        
    if cannotgo == 1:
        print(f'#{tc} {cannotgo-1}')
    else:
        print(f'#{tc} {charging}')

#순화언니 안뇽!!!!!!!!!!!!!
#내가 누구게
    # while idx <= len(stops):
    #     for i in range(rest_chargers,0,-1):
    #         if (stops[chargers[charger_idx + i]] - previous_charger) > k:
    #             if (stops[chargers[charger_idx]] - previous_charger) > k:
    #                 cannotgo += 1
    #                 break
    #             elif (stops[chargers[charger_idx]] - previous_charger) <= k:
    #                 count_charging += 1
    #                 previous_charger = stops[chargers[charger_idx]]
    #                 charger_idx += 1
    #         else:
    #             if (stops[chargers[charger_idx]] - previous_charger) == k:
    #                 count_charging += 1
    #                 previous_charger = stops[chargers[charger_idx]]
    #                 charger_idx += 1
    #
    #
    #
    # for i in range(1,len(chargers)+1,2):
    #     if (stops[chargers[i]]-previous_charger)<=k:
    #         if (stops[chargers[i-1]] - previous_charger) > k:
    #             cannotgo += 1
    #             break
    #         elif (stops[chargers[i-1]]-previous_charger)<=k:
    #             count_charging +=1
    #             previous_charger = stops[chargers[i-1]]
    #         else:
    #             count_charging +=1
    #             previous_charger = stops[chargers[i]]
    #     previous_charger = stops[chargers[i-1]]


    # if cannotgo == 1:
    #     count_charging = 0
