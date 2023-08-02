from itertools import combinations

L, C = map(int, input().split())

vowels = ['a', 'e', 'i', 'o', 'u']
available_list = list(input().split())
sorted_list = sorted(available_list)
vowels_list = [x for x in available_list if x in vowels]
consonants_list = [x for x in available_list if x not in vowels]
result_list = []

for num in combinations(sorted_list, L):
    vowels_count = 0
    consonants_count = 0
    for i in num:
        if i in vowels_list:
            vowels_count += 1
        if i in consonants_list:
            consonants_count += 1
    if vowels_count < 1 or consonants_count < 2:
        continue
    else:
        result_list.append(num)

for i in result_list:
    print(''.join(i))