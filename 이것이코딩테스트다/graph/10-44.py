'''
44. 행성터널 
모든 3차원 점을 연결하는 최소한의 비용 구하기

입력: 행성개수
각 행성의 x, y, z 좌표 

5 
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b: 
    parent[b] = a
  else:
    parent[a] = b
    
    
n = int(input()) 
parent = [0] * (n + 1)
for i in range(1, n + 1):
  parent[i] = i 
  
edges = []
result = 0

x=[]
y=[]
z=[]

for i in range(1, n+1):
  data = list(map(int, input().split()))
  x.append((data[0], i))
  y.append((data[1], i))
  z.append((data[2], i))
  
x.sort() 
y.sort()
z.sort() 

#인접한 노드들로 부터 간선 정보를 추출하여 처리 
for i in range(n-1):
  edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
  edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
  edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))
  
# print(edges) 
# [(11, 3, 4), (10, 1, 2), (0, 1, 2), (1, 4, 1), (1, 2, 4), (10, 2, 3), (3, 1, 2), (0, 4, 5), (4, 3, 4), (5, 2, 5), (3, 5, 3), (20, 4, 5)] 

edges.sort()

# print(edges)
# [(0, 1, 2), (0, 4, 5), (1, 2, 4), (1, 4, 1), (3, 1, 2), (3, 5, 3), (4, 3, 4), (5, 2, 5), (10, 1, 2), (10, 2, 3), (11, 3, 4), (20, 4, 5)]

for edge in edges:
  cost, a, b = edge
  #사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
  
'''
참고 :https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80-2887-%ED%96%89%EC%84%B1-%ED%84%B0%EB%84%90 
'''