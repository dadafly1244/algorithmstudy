'''
컴퓨터가 신뢰관계일때 한번에 해킹 가능!! 

첫출에 n (10,000 작거나 같음), m(100,000 작거나 같음 )
A가 B를 신뢰한다 


출력 
한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터를 오름차순으로 출력

'''

'''
모든 정점에 대해서 dfs 수행
수행할때 마낟 방문하게 되는 노드의 개수를 계산 

'''
import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

def bfs(start):
	cnt = 1 #방문하는 정점의 갯수계산
	queue = deque([start])
	visit = [False for _ in range(n+1)]
	visit[start] = True

	while queue:
		cur = queue.popleft()

		for nx in graph[cur]:
			if not visit[nx]:
				visit[nx] = True
				cnt += 1
				queue.append(nx)

	return cnt

graph = [[] for _ in range(n+1)]

for _ in range(m):
	a,b = map(int,input().split())
	graph[b].append(a)

ans = []
maxCnt = -1


for i in range(1,n+1):
  cnt = bfs(i) # 매번 모든 정점에 대해서 계산
  if cnt > maxCnt:
    ans = [i]
    maxCnt = cnt
  elif cnt == maxCnt:
    ans.append(i)
    maxCnt = cnt

		

for i in ans:
  print(i, end=' ')