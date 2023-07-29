import sys

n = int(sys.stdin.readline())
command_list = []
stack_list = []

for _ in range(n):
    command_list.append(sys.stdin.readline().rstrip())

for command in command_list:
    if command[:4] == 'push':
        com = int(command.split()[1])
        stack_list.append(com)
    elif command == 'pop':
        if len(stack_list) > 0:
            res = stack_list.pop()
            print(res)
        else:
            print(-1)
    elif command == 'size':
        print(len(stack_list))
    elif command == 'empty':
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[len(stack_list)-1])
