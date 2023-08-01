a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatia_word = input()

for i in a:
    croatia_word = croatia_word.replace(i, "*")

print(len(croatia_word))