import heapq
import sys
INF = int(1e9) # 무한을 의미하는 값

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드 번호를 입력받기
start=n
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만드릭
graph=[[] for i in range(100001)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] *(n+1)

for i in range(1, 100000):
    if i+1 not in graph[i]:
        graph[i].append((i+1, 1))
    if i not in graph[i+1]:
        graph[i+1].append((i, 1))
    if i-1 not in graph[i]:
        graph[i].append((i-1, 1))
    if i not in graph[i-1]:
        graph[i-1].append((i, 1))
    if i*2 <= 100000 and i*2 not in graph[i]:
        graph[i].append((i*2, 1))
    if i*2 <= 100000 and i not in graph[i*2]:
        graph[i*2].append((i, 1))
  
def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start]=0
    while q : # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now= heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시 (이미 최단 거리라면 무시)
        if distance[now] < dist:
                continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[i]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost <distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i]==INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거기를 추력
    else:
        print(distance[i])