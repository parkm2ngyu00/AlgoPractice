import math

word = input()

for i in range(math.floor(len(word)/2)):
    if word[i] == word[-1-i]:
        continue
    else:
        print(0)
        exit(0) # 백준 사이트의 경우 exit(-1)을 하면 런타임 오류 발생

print(1)
