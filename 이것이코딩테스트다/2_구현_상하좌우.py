'''
문제 : 상하좌우 
n*n 정사각형에서 (1,1)에서 출팔해서 상하좌우로 움직였을 때, 최종 도착 좌표를 출력하는 문제 
접근방법
입력 : 정사각형 크기 n, 상하좌우를 영어로 한줄로 입력 받음
좌표 이동을 위한 변수를 선언해서 x,y 좌표와 이동할 때 받을 타입을 변수로 선언함 
입력받은 움직임을 하나씩 꺼내와서 미리 선언해둔 이동 타입이랑 비교하고 정사각형 범위를 벗어나지 않는지 보기
벗어나지 않으면 이동한 좌표를 저장하고 다음 이동 타입을 받아옴 
느낀점 : 처음에 좌표를 바로 움직이고 난 다음에 범위를 벗어나는지 보고 아니면 다시 계산을 했는데, 임시변수를 잘 사용하면 계산량을 줄일 수 있다ㅡㄴ 생각이 들었음. 

'''
n = int(input())

data  = input().split()

x,y = 1,1

dx = [0,0,-1,1] # L R U D x 좌표 
dy = [-1,1,0,0] # L R U D
next_move = ['L','R','U','D']


for move in data:
    for j in range(len(next_move)):
        if move == next_move[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx <1 or ny <1 or nx>n or ny >n:
        continue
    x,y = nx, ny 

print(x, y)
