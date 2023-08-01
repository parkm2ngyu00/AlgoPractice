import sys

goal_num = int(sys.stdin.readline())
current_num = 100
broken_num = int(sys.stdin.readline())
broken_list = []
available_list = []
btn_list = [x for x in range(10)]

if broken_num != 0:
    broken_list = list(map(int, sys.stdin.readline().split()))

for broken_btn in broken_list:
    btn_list.remove(broken_btn)

def check_number(number, num_list=broken_list):
    number_str = str(number)
    for digit in number_str:
        if int(digit) in num_list:
            return True
    return False

# btn list에 사용 가능한 button 저장

# btn list에 있는 숫자를 조합해 goal_num과 가장 가까운 수를 만들어내고 그 차이 출력
# 사용 가능하지 않은 버튼이 들어가있는지를 확인
min = 1000002
target = 0
for i in range(0, 1000001):
    if ((check_number(i) == False) and (abs(goal_num - i) < min)):
        min = goal_num - i
        target = i

remote1 = len(str(target)) + abs(goal_num - target)
# 그 후 +또는 -만으로 움직이는 것과의 차이를 비교해 작은 수를 출력
remote2 = abs(goal_num - 100)

if len(broken_list) == 10 or remote2 < remote1:
    print(remote2)
else:
    print(remote1)