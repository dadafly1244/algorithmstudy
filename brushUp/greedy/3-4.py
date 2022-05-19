'''
1이 될 때까지
p99
'''

n, k = map(int, input().split())
result = 0

while True:
  #나눠 떨어지는 수가 될때까지 1빼는거!! 
  tar = (n // k) *k 
  result += (n - tar)
  n = tar

  if n < k:
    break
  result += 1
  n //= k

#마지막으로 1씩 
result += (n-1)
print(result)

    
    
'''
복습포인트 
2중 반복문을 돌아도 되지만 몫 연산자를 이용해서 1개의 반복문만 돌기 
나누셈을 최대한 많이 하기!! = 배수일때 나누고 아니면 1빼기


'''