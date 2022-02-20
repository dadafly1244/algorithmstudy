n = int(input('거스름돈 : '))
count = 0

while(n >0):
    if n >= 500:
        n-=500
        count +=1       
    elif n >= 100:
        n-=100
        count +=1        
    elif n >= 50:
        n-=50
        count+=1 
    elif n >= 10:
        n-=10
        count +=1     

print('동전의 최소 개수 :{}'.format(count))

'''
답안 예시 

n = int(input('거스름돈 : '))
count =0
coin_types = [500,100,50,10]

for coin in coin_types:
    count += n //coin #해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기 
    n %= coin
print(count)
1. 문제설명 : 거스름돈을 500,100,50,10원을 사용하여 최소한의 동전 개수로 거슬러 주는 것!!
2. 접근방법 : 그리디 사용 
3. 느낀점 리스트 쓸 생각을 안하고 너무 단순하게 while문을 돌아버린 것 같...다.... 
'''

