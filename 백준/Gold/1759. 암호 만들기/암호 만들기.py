import sys; input = sys.stdin.readline

def check(lst):
    mo, ja = 0, 0
    for i in range(L):
        if lst[i] in vowels:
            mo += 1
        else:
            ja += 1
    
    if mo >= 1 and ja >= 2:
        return True
    else:
        return False

def secretcode(long, start):
    if long == L:
        if check(ans) is True:
            print(''.join(ans))
            return
    
    for i in range(start, C):
        ans.append(arr[i])
        secretcode(long + 1, i + 1)
        ans.pop()

L, C = map(int, input().split())
arr = sorted(map(str, input().split()))
vowels = ["a", "e", "i", "o", "u"]
ans = []

secretcode(0, 0)