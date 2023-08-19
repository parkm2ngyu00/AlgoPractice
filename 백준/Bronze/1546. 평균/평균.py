scores = []
new_score = []
score_add = 0
cnt = int(input())

scores = list(map(int, input().split()))
# for i in range(cnt):
#     scores.append(int(input()))

max_score = max(scores)

for i in range(cnt):
    new_score.append(scores[i] / max_score * 100)
    score_add += new_score[i]

print("{:2}".format(score_add / cnt))