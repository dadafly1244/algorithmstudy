'''
43. 어두운길  난이도 2 

0번집 부터 n-1번 집까지 번호!!
집 사이에 있는 가로등을 최소한으로 켜서 최대한 금액을 절약하는 문제!!

'''

'''
[입력]
집의수 N, 도로의 수 M
x번 집, y번 집 , z길이
x, y가 동일한 경우는 없음.

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
    
    
n, m =map(int, input().split())
parent = [0] * (n + 1)
for i in range(1, n + 1):
  parent[i] = i 
  
edges = []
result = 0

for _ in range(m):
  x, y, z = map(int, input().split())
  edges.append((z, x, y))
  
edges.sort()
total = 0 # 전체 가로등 비용

for edge in edges:
  cost, a, b = edge
  total += cost 
  #사이클 발생 x인 경우에 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a ,b)
    result += cost
  
print(total - result)
