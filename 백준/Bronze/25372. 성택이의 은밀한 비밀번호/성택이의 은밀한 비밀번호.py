n = int(input())

for _ in range(n):
    lst=input()
    if lst.isdigit and 6<=len(lst)<=9:
        print('yes')
    else:
        print('no')