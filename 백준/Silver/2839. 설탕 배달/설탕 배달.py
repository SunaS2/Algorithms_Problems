n = int(input())

rest = n
sugar3 = 0
sugar5 = 0

while rest != 0:
    if rest < 3:
        break
    elif rest >= 3 and rest%5!=0:
        rest -= 3
        sugar3 += 1
    if rest % 5 == 0:
        sugar5 = rest // 5
        rest -= sugar5*5

if rest == 0:
    print(sugar5+sugar3)
else:
    print(-1)
