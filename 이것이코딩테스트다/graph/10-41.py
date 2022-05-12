'''
41. 여행계획  : 난이도 2

'''

'''
입력
여행지 수 n, 여행계획이 속한 도시 수 m
n*n 행열로 연결되어 있는지 주어짐 1은 연결이라는 의미 0아니라는의미
마지막줄 한울이의 여행계획이 포함된 여행지들의 번호 주어짐. 

출력
여행계획이 가능하면 yes 아니면 no 출력하기
'''





'''풀이 계획
서로소 집합 사용하기. 
10-7이랑 비슷한 문제인 것 같음. 

'''

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent,parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  
#여행지 수 n, 여행계획이 속한 도시 수 m
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1: #연결된 경우!!
      union_parent(parent, i + 1, j + 1)

# 여행계획 
plan = list(map(int, input().split()))

result = True
#여행계획에 속하는 모든 노드의 루트가 동일한지 확이 ㄴ
for i in range(m - 1):
  if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
    result = False
    
if result:
  print('yes')
else:
  print('no')
  
'''
for 문 돌면서 부모 연결하는 부분을 생각을 못함.. ! 

'''