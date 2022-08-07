import sys
input =  sys.stdin.readline
n, c = list(map(int,input().split(' ')))

house = []
for _ in range(n):
  house.append(int(input()))
house.sort()  # 정렬

start = 1 #최소거리
end = house[-1] - house[0] #제일 마지막집에서 첫집빼기
result = 0

while(start <= end):
  mid = (start + end) // 2 
  value = house[0]
  count = 1
  for i in range(1, n): #1부터 공유기 설치
    if house[i] >= value + mid:
      value = house[i]
      count += 1
  if count >= c: #c개 이상 설치할 수 있는 경우 
    start = mid + 1
    result = mid 
  else: #c개 이상 설치 x
    end = mid -1

print(result)


