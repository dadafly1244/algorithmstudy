'''
안테나 설치! 
집이 어디에 있는지! 
안테나로부터 모든 집들의 거리의 총합이 최소가 되는 안테나 설치 위치 선정하기! 

접근법 : 제일 작은수와 큰수의 평균으로 하면 되지 않을까?!!! 
n = int(input())

house = list(map(int,input().split()))


house.sort()

result = house[0] + house[n-1] // 2

print(result)

틀림...
'''




n = int(input())
house = list(map(int,input().split()))
house.sort()


#중간값 출력!...!!!!! 
print(house[(n-1)//2])

'''
중간값이 필요했음!! 

'''