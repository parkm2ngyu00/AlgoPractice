from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline())
print_list = []
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command[:4] == 'push':
        target = command.split()[1]
        queue.append(target)
    elif command == 'pop':
        if len(queue) != 0:
            num = queue.popleft()
            print_list.append(num)
        else:
            print_list.append(-1)
    elif command == 'size':
        print_list.append(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print_list.append(1)
        else:
            print_list.append(0)
    elif command == 'front':
        if len(queue) != 0:
            print_list.append(queue[0])
        else:
            print_list.append(-1)
    elif command == 'back':
        if len(queue) != 0:
            print_list.append(queue[-1])
        else:
            print_list.append(-1)

for i in range(len(print_list)):
    print(print_list[i])