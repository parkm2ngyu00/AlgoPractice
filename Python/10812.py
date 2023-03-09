# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

# 둘째 줄부터 M개의 줄에는 바구니의 순서를 바꾸는 만드는 방법이 주어진다. 방법은 i, j, k로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 회전시키는데, 그 때 기준 바구니는 k번째 바구니라는 뜻이다. (1 ≤ i ≤ k ≤ j ≤ N)

# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 회전시킨다.

N, M = map(int, input().split())
N = N + 1

initList = []
leftDefaultList = []
rightDefaultList = []

for i in range(N-1):
    initList.append(i+1)


for loop in range(M):
    i, j, k = map(int, input().split())
    leftDefaultList = initList[0:i-1]
    rightDefaultList = initList[j:N+1]
    leftList = initList[i-1:k-1]
    rightList = initList[k-1:j]
    list = []
    list = leftList
    leftList = rightList
    rightList = list
    resultList = []
    resultList = leftDefaultList + leftList + rightList + rightDefaultList
    initList = resultList

result = ' '.join([str(x) for x in initList])
print(result)
