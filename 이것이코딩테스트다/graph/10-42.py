'''
42. 탑승구: 난이도 2

i번째 비행기는 1번부터 gi번째 탑승구 중 하나를 도킹 가능 

입력
탑승구 G
비행기 수 P
P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보 

출력
도킹할 수 있는 비행기의 최대 개수 
'''


'''
생각지도 못하게 서로소를 활용해서 놀랍네...? 
비행기가 가능한 큰 번호의 탑승구로 도킹시도.
도킹되면 바로 왼쪽의 탑승구와 집합을 합침. 만약 집합의 루트가 0이면 더이상 못합친다!!

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
    
#탑승구
g = int(input())
#비행기
p = int(input())

parent = [0] * (g + 1)
for i in range(1, g+1):
  parent[i] = i
  
result = 0 
for _ in range(p):
  data = find_parent(parent, int(input())) # 현재 비행기 탑승구의 루트 확인
  if data == 0: #현제 루트가 0이면 종료
    break
  union_parent(parent, data, data - 1)# 현재 루트가 0이 아니라면 왼쪽 집합이랑 합치기 
  result += 1
  
print(result)