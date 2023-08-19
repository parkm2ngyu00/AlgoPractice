cnt = int(input())


for i in range(cnt):
    student_scores = list(map(int, input().split()))
    scores = student_scores[1:]
    student = student_scores[0]
    average = sum(scores) / student
    a = 0
    for j in range(student):
        if scores[j] > average:
            a += 1
    print("{:.3f}%".format(a / student * 100))

