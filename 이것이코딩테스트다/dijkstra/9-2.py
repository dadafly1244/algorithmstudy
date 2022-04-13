
'''
우선순위 큐를 활용한 개선된 다익스트라 알고리즘 


'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) #무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작노드
start = int(input())

# 최단거리 테이블 무한으로 초기화
distance = [INF] * (n+1)
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]

#간선 정보 입력 받기
for _ in range(m):
  a, b, c = map(int, input().split()) #a번 노드에서 b로 가는 비용이 c
  graph[a].append((b, c)) #튜플 형식으로 넣어주기


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))  # 시작노드 정보 우선순위 큐에 삽입 (거리, 노드)로 삽입. 거리를 기준으로 우선순위!! 
  distance[start] = 0            # 시작노드->시작노드 거리 기록
  while q: #큐가 비어 있지 않다면! 
    # 가장 거리가 짧은 노드에 대한 정보 꺼내기! 
    dist, now = heapq.heappop(q)
    
    # 큐에서 뽑아낸 거리가 이미 갱신된 거리보다 클 경우(=방문한 셈) 무시
    if distance[now] < dist:
      continue
    # 큐에서 뽑아낸 노드와 연결된 인접노드들 탐색
    for next in graph[now]:
      cost = distance[now] + next[1]   # 시작->now거리 + now->now의인접노드 거리
      if cost < distance[next[0]]:      # cost < 시작->now의인접노드 거리
        distance[next[0]] = cost
        heapq.heappush(q, (cost, next[0]))

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, len(distance)):
  #도달할 수 없는 경우 무한이라고 출력
  if distance[i] == INF:
    print('INFINITY')
  else: #도달할 수 있는 경우 거리를 출력
    print(distance[i])
        
        
# 참고 블로그 : https://techblog-history-younghunjo1.tistory.com/248       