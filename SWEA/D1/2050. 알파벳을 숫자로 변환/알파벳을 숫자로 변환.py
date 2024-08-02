T = 1

for tc in range(1,T+1):
    string = list(input())

    lst_num =[]
    for char in string:
        lst_num.append(str(ord(char)-64))

    print(f'{" ".join(lst_num)}')