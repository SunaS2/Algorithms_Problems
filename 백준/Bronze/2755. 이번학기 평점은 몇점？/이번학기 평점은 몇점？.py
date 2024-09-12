N = int(input())
grades = {"A+" : 4.3, "A0" : 4.0, "A-" : 3.7,
          "B+" : 3.3, "B0" : 3.0, "B-" : 2.7,
          "C+" : 2.3, "C0" : 2.0, "C-" : 1.7,
          "D+" : 1.3, "D0" : 1.0, "D-" : 0.7, "F" : 0.0} # 성적

total_credit = 0 # 총 학점
total_grade = 0 # 총 성적

for _ in range(N):
    subject = input().split() # 과목, 학점, 성적 순
    credit = int(subject[1])
    grade = subject[2]

    total_credit += credit
    total_grade += (credit * grades[grade])

result = total_grade / total_credit
result2 = round(total_grade / total_credit, 2)
remain = round(result - result2, 4)

if remain < 0.005:
    print(f"{result2:.2f}")
else:
    print(f"{result2 + 0.01:.2f}")