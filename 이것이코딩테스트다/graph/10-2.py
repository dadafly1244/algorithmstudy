# 원래 코드 
def find_parent(parent, x):
  if parent[x] != x:
    return find_parent(parent, parent[x])
  return x
    


# 경로압축 기법 소스코드
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]