n = int(input())
scores = list(map(int,input().split()))

max_score = max(scores)

total_new_scores = 0
for score in scores:
    new_score = score/max_score*100
    total_new_scores += new_score

print(total_new_scores/n)