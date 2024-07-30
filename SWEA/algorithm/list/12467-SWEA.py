T = int(input())

for tc in range(1, T+1):
    k, m, n = list(map(int,input().split()))
    chargers = list(map(int, input().split()))
    stops = [0]*(m+1)

    for charger in chargers:
        stops[charger] = 1
    charging = 0
    present_position = 0
    while present_position >= len(stops):
        if stops[present_position+k] == 1:
            charging += 1
            previous_charging = present_position
        else:
            for i in range(1,k):
                if stops[present_position-i] == 1:
                    charging += 1
                    present_position = present_position-i
                    break
#순화언니 안뇽!!!!!!!!!!!!!
#내가 누구게
        new_charging = charging
        if charging == new_charging:
            charging = 0
            break

        previous_charging = present_position

    print(f'#{tc} {charging}')

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






