T = int(input())
 
for tc in range(1, T+1):
    n = int(input())
    bus_lines = [list(map(int,input().split())) for _ in range(n)]
    p = int(input())
    bus_stops = [int(input()) for _ in range(p)]
 
    farest_stops = []
    for i in bus_lines:
        farest_stops.append(max(i))
     
    stops_for_count_lines = [0]*5001
     
    for line in bus_lines:
        for stop in range(line[0],(line[1]+1)):
            stops_for_count_lines[stop] += 1
     
    for_print = ''
    for stop in bus_stops:
        for_print = for_print +str(stops_for_count_lines[stop])+' '
 
     
    print(f'#{tc} {for_print}')