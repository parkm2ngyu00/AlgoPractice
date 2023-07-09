import sys

def brute_force(nums):
    results = []  # 결과를 저장할 리스트

    # 첫 번째 원소를 선택하는 for문
    for i in range(len(nums) - 6):
        selected = [nums[i]]  # 선택된 원소를 저장할 리스트

        # 두 번째 원소를 선택하는 for문
        for j in range(i + 1, len(nums) - 5):
            selected.append(nums[j])

            # 세 번째 원소를 선택하는 for문
            for k in range(j + 1, len(nums) - 4):
                selected.append(nums[k])

                # 네 번째 원소를 선택하는 for문
                for l in range(k + 1, len(nums) - 3):
                    selected.append(nums[l])

                    # 다섯 번째 원소를 선택하는 for문
                    for m in range(l + 1, len(nums) - 2):
                        selected.append(nums[m])

                        # 여섯 번째 원소를 선택하는 for문
                        for n in range(m + 1, len(nums) - 1):
                            selected.append(nums[n])

                            # 일곱 번째 원소를 선택하는 for문
                            for p in range(n + 1, len(nums)):
                                selected.append(nums[p])

                                results.append(selected[:])  # 결과 리스트에 현재 조합 추가

                                selected.pop()  # 마지막에 추가한 원소 제거

                            selected.pop()  # 여섯 번째 원소 제거

                        selected.pop()  # 다섯 번째 원소 제거

                    selected.pop()  # 네 번째 원소 제거

                selected.pop()  # 세 번째 원소 제거

            selected.pop()  # 두 번째 원소 제거

        selected.pop()  # 첫 번째 원소 제거

    return results


height_list = []

for i in range(9):
    height_list.append(int(sys.stdin.readline()))

result_list = brute_force(height_list)

for i in range(36):
    if sum(result_list[i]) == 100:
        result_list[i].sort()
        for j in range(7):
            print(result_list[i][j])
        break