'''
문제 설명 
공중 미래 도시 1 ~ n까지 번호의 회사가 있음. 
회사끼리 연결되어 있는 도로를 이용하는 방법이 유일함. 
특정 회사와 다른 회사가 연결되어 있다면 1만큼의 시간으로 이동 가능 
a 현재 위치 1 ->  k번째 회사에가서 소개팅 -> x번째 회사에가서 물건팔기 목표!! 


'''
'''
입력 
회사 개수 n, 경로 개수 m 
'''


INF = int(1e9)
n , m = map(int, input().split())
graph = [[INF] * (n+1) for  _ in range(n+1)]

# 자기 자신으로 가는 비용 0 초기화 
for a in range(1 , n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0
      
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
  # 도시간 비용 1
  a,b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1
  
# 거쳐 갈 노드 x랑 k 입력 받기 
x, k = map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])
      
# 수행된 결과 출력
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우  -1을 출력 
if distance >= INF:
  print('-1')
else: 
  print(distance)
  
