'''
문제설명 :  n개의 도시와 m 개의 단방향 도로가 존재함. 모든 도로의 거리는 1. 
도시 x로부터 출발하여 도착할 수 있는 도시 중 최단 거리가 k인 도시 번호를 출력하는 프로그램 만들기. 


문제 접근 방법 : 모든 도로의 거리 1 = 간선의 비용이 1이기 때문에 너비우선탐색(BFS)를 사용할 수 있음 너비우선 탐색은 큐(FIFO)로 구현

'''


from collections import deque

n, m, k , x= map(int,input().split()) # 도시의 개수, 도로의 개수, 거리정보 k ,출발도시번호 
graph = [[] for _ in range(n+1)]
'''
a = [[0]*3 for _ in range(3)]
print(a)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

'''

#도로 입력 받기 
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    
#print( graph)

#모든 도시에 대한 최단 거리 초기화 
distance = [-1] * (n+1)
distance[x] = 0 #출발도시까지의 거리는 0으로 설정
#print(distance)

#너비우선 탐색 (BFS)
q = deque([x])
#print(q)

while q:
    now = q.popleft()
    #print(now)
    #print(q)
    #현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        #아직 방문학지 않은 도시라면
        if distance[next_node] == -1:
            #최단거리 갱신
            distance[next_node] = distance[now] + 1
            #print(distance)
            q.append(next_node)
            #print(q)

#최단거리가 k인 모든 도시의 번호를 오름차순으로 출력 
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check =True
# 만약 최단거리가 k인 도시가 없다면 -1출력
if check == False:
    print(-1)
    