n = int(input())
people = [list(input().split()) for _ in range(n)]

for p in people:
    p[0] = int(p[0])

people.sort(key= lambda x: x[0])

for p in people:
    print(p[0],p[1])