import sys

color = {'black':[0, 1], 'brown':[1, 10], 'red':[2, 100], 'orange':[3, 1000]\
         , 'yellow':[4, 10000], 'green':[5, 100000], 'blue':[6, 1000000]\
            , 'violet':[7, 10000000], 'grey':[8, 100000000], 'white':[9, 1000000000]}

color_list = []

for i in range(3):
    color_list.append(sys.stdin.readline().rstrip())

res = int(str(color[color_list[0]][0]) + str(color[color_list[1]][0])) * color[color_list[2]][1]
print(res)