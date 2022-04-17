'''


'''


n = int(input())

ugly = [0] * n #못생긴 수를 담기 위한 1차원 dp 테이블
ugly[0] =1 # 첫번째 못생긴 수는 1 

#2,3,5배를 위한 인덱스 
i2 = i3 = i5 =0
#처음에 곱한값을 초기화 
next2, next3, next5 = 2,3,5

#1부터 n까지 못생긴 수를 찾기 

for i in range(1,n):
  #간으한 곱셈 결과 중에서 가장 작은 수를 선택 
  ugly[1] = min(next2,next3,next5)
  #인덱스에 따라서 곱셈 결과르 ㄹ증가 
  if ugly[1] == next2:
    i2 +=1 
    next2 = ugly[i2] * 2 
  if ugly[1] == next3:
    i3 +=1 
  next2 = ugly[i3] * 3 
  if ugly[1] == next5:
    i5 +=1 
  next2 = ugly[i5] * 5
  
print(ugly[n-1]) 