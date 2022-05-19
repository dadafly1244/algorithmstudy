'''
큰수의 법칙
p93

'''

n, m , k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
first = data[0]
second = data[1]

result = 0
for i in range(1,m+1):
  if i % k == 0:
    result += second
  else:
    result += first
  
  
print(result)

'''
복습 포인트 
sort함수

'''