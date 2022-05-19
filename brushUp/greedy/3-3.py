'''
숫자카드게임
'''

n, m = map(int, input().split())
result = 0 
for i in range(n):
  data = list(map(int, input().split()))
  min_n = min(data)
  result = max(result, min_n)
  
print(result)

'''
복습 포인트 
min, max 함수 
데이터를 따로 저장하지 않고 바로 min계산하는것!
'''