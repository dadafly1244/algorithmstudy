from collections import deque

n,m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

#상하좌우
dx=[-1,1,0,0]
dy = [0,0,-1,1] 

#BFS 소스코드  
def bfs(x,y):
    #큐 구현을 위한 deque 라이브러리 사용
    queue = deque() 
    queue.append((x,y))
    #큐가 빌때까지 반복
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로 위치 확인 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로의 찾기 공간을 벗어난 경우 무시 
            if nx < 0 or ny <0 or nx >=n or ny >= m:
                continue
            #벽인경우 무시
            if graph[nx][ny] == 0:
                continue
            #해당노드를 처음 방문하는 경우에만 최단 거리 
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        #가장 오른ㅉ고 아래까지의 최단 거리 변환        
    return graph[n-1][m-1]
    
print(bfs(0,0))