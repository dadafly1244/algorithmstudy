'''
nXn  크기의 땅 
r행 c열의 나라에는 A[r][c]명이 살고 있음 
두 나라의 인구 차이가 L이상 R이하이면 국경 열기
인접한 칸만을 이용해서 이동할 수 있으면 연합!!
연합의 인구수 / 연합을 이루구 있는 칸수 (소수점은 버림)

DFS랑 BFS 둘다 가능 !! 인접한 나라의 인구수 확인 후 이동하기!!

'''
from collections import deque

n, l, r = map(int,input().split())

#나랑 정보 입력
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
    
dx = [-1,0,1,0]
dy =[0,-1,0,1]

result = 0

#특정위치에서 출발한 뒤 모든 연합 체크!! 데이터 갱신

def process(x,y,index) :
    #(x,y)의 위치와 연결된 나라 정보를 담는 리스트 
    united =[]
    united.append((x,y))
    #BFS탐색 
    q = deque() #괄호 빠져 먹어서.... 꼐속 안된듯 ㅋ
    q.append((x,y))
    union[x][y] = index #현재 연합의 번호 할당
    summary = graph[x][y] #현재 연합의 전체 인구 수 
    count = 1 #현재 연합의 국가 수 
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #바로 옆에 나라 확인 
            if 0 <= nx < n and 0 <= ny <n and union[nx][ny] == -1:
                #바로 옆 나라가 L이상 R이하의 인구수 차이라면! 
                if l <= abs(graph[nx][ny]- graph[x][y]) <= r:
                    q.append((nx,ny))
                    #연합에 추가 
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1 
                    united.append((nx,ny))
                    
    #연합국가끼리 인구를분배 
    for i ,j in united:
        graph[i][j] = summary //count
    return count


total_count = 0

#더 이상 반복 못할 떄 까지 반복 
while True:
    union = [[-1]* n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1 :#해당 나라가 아직  처리되지 않았다면!! 
                process(i,j,index)
                index += 1 
                
        
    if index == n * n:
        break
        
    total_count += 1 
        
print( total_count)