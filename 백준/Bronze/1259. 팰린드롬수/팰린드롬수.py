def ismirror(lst):
    for i in range(len(lst)//2):
        if lst[i] == lst[len(lst)-1-i]:
            continue
        else:
            break
    else:
        return "yes"
    return "no"

result = []
while True:
    lst = list(input())
    if lst[0]=='0':
        break

    result.append(ismirror(lst))

for r in result:
    print(r)