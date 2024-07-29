#T = int(input())
#for tc in range(1, T + 1):
number_of_carrot = 8 #int(input())
carrots = [1,2,1,2,3,1,2,1]#list(map(int, input().split()))

temp = carrots[0]
max_count = 0
count = 1
for i in range(1, number_of_carrot):
    if carrots[i] - temp == 1:
        count = count + 1
        if max_count <= count:
            max_count = count
    elif carrots[i] - temp != 1:
        if max_count <= count:
            max_count = count
        count = 1

    temp = carrots[i]

print(f"{max_count}")