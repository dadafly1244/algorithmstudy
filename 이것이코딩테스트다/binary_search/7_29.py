import sys
f = sys.stdin.readline
n, c = map(int, f().split())
house = []
for _ in range(n):
    house.append(int(f()))

house.sort()

start = 1 #가능한 최소 거리
end = house[-1] - house[0] # 가능한 최대 거리 
result = 0

while(start <= end):
    mid = (start + end)//2 #가장 인접한 두 공유기 사이의 거리 의미! 
    value = house[0]
    count =1
    #현재 mid 값을 이용해 공유기를 설치하기 
    for i in range(1,n):
        if house[i] >= value + mid:
            value = house[i]
            count += 1 
    if count >= c: #c개 이상의 공유기를 설치할 수 있는 경우 , 거리 증가 
        start = mid +1
        result = mid #최적의 결과 저장
    else:
        end = mid -1

print(result)




n , c =list( map(int, input().split()))

house = []
for _ in range(n):
    house.append(int(input()))
    
house.sort()

start = 1 #가능한 최소 거리
end = house[-1] - house[0] # 가능한 최대 거리 
result = 0

while(start <= end):
    mid = (start + end)//2 #가장 인접한 두 공유기 사이의 거리 의미! 
    value = house[0]
    count =1
    #현재 mid 값을 이용해 공유기를 설치하기 
    for i in range(1,n):
        if house[i] >= value + mid:
            value = house[i]
            count += 1 
    if count >= c: #c개 이상의 공유기를 설치할 수 있는 경우 , 거리 증가 
        start = mid +1
        result = mid #최적의 결과 저장
    else:
        end = mid -1

print(result)