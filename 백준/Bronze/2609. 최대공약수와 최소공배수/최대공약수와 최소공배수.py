A, B = map(int,input().split())
lst_A = set()
lst_B = set()

for a in range(1,A+1):
    if A%a == 0:
        lst_A.add(a)

for b in range(1,B+1):
    if B%b == 0:
        lst_B.add(b)

common = lst_A & lst_B
common = list(common)
GCD = max(common)

LCM = GCD*(A//GCD)*(B//GCD)

print(GCD)
print(LCM)