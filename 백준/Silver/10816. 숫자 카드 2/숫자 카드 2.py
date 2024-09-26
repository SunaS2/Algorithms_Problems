import sys

input = sys.stdin.readline

def binary_search(key, left, right):
    if left > right:
        return 0
    
    mid = (left+right)//2

    if cards[mid] == key:
        return cards_dic[key]
    elif cards[mid] < key:
        return binary_search(key,mid+1,right)
    else:
        return binary_search(key,left,mid-1)


N = int(input())
cards = list(map(int,input().split()))
cards.sort()

cards_dic = {}
for n in cards:
    if n in cards_dic:
        cards_dic[n] += 1
    else:
        cards_dic[n] = 1

M = int(input())
lst = list(map(int,input().split()))

for m in lst:
    print(binary_search(m,0,N-1), end=' ')