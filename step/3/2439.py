# n = int(input())

# for i in range(n):
#   print('{:>5}'.format('*'*(i+1))) 
# 출력 형식이 잘못되었습니다

n = int(input())
for i in range(1, n+1):
  print(' '*(n - i) + '*'*i)

##format으로 하는거랑 저거랑 먼 차이지? 흠..? 