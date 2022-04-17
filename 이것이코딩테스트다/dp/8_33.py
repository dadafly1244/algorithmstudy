n = int(input())
t =[] #각 상담 완료하는데 걸리는 시간
p = [] #각 상담 완료했을 때 받을 수있는 금액
dp =[0] * (n+1) #다이나믹 프로그래밍을 위한 1차원 dp테이블 초기와 
max_value = 0

for _ in range(n):
    x,y = map(int, input().split())
    t.append(x)
    p.append(y)
    
for i in range(n-1,-1 , -1):
    print(i)
    time = t[i] +i
  
    if time <= n:
    
      dp[i] = max(p[i] + dp[time], max_value)
      max_value = dp[i]
      
    else:
      dp[i] = max_value

print(max_value)