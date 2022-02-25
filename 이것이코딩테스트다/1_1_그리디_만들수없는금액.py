'''
문제 : N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최소값
접근법 : 그리디
1부터 target까지의 모든 금액을 만들 수 있는 상태로 보고 target을 만들 수 있는지 체크하는 것 

'''
n = int(input())
data= list(map(int,input().split()))
data.sort()

target = 1 
for x in data:
    #만들 수 없는 금액을 찾았을 때 반복 종료 
    if target <x:
        break
    target += x
    
print(target)
