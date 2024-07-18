N = int(input())
people = []
rates = []

for _ in range(N):
    W, H = map(int, input().split())
    people.append([W, H])

for i in range(N):
    rate = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rate += 1
    rates.append(rate)

for i in rates:
    print(i, end=" ")