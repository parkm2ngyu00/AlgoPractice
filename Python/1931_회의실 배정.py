import sys

n = int(sys.stdin.readline())
meeting_list = []
result_list = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    temp_list = []
    temp_list.append(a)
    temp_list.append(b)
    meeting_list.append(temp_list)

# 하나를 무작위로 선택하고, 다음 끝나는 시간이 가장 빠른 다음거 선택함 -> 정렬하면 되잖아...
meeting_list.sort(key = lambda x : (x[1], x[0]))

end_time = meeting_list[0][1]
result_list.extend(meeting_list[0])
for i in range(1, len(meeting_list)):
    if end_time <= meeting_list[i][0]:
        result_list.extend(meeting_list[i])
        end_time = meeting_list[i][1]

print(len(result_list) // 2)