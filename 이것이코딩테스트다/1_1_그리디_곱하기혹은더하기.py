data = input()

result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
        

'''

1. 문제설명 
0~9로만 이루어진 문자열이 주어질때, 각 숫자를 순서대로 더하거나 곱해서 가장 큰 수른 만드는 문제!!
2. 접근방식 
그리디
0과 1은 더하기, 1이상부터는 곱하기가 유리함.  
3. 느낀점 
입력받는 방법, 그리고 중간에 조건을 다시생각하자... ㅋㅋ
        
numlst = list(map(int,input().split())) #문제 조건에 맞는 input을 받지 못햇음. 이건 한줄로 입력받는 것인 아니라 띄워쓰기가 필요함!!

result = 0

for i in numlst:
    if i <= 1 or result == 0: #result ==0 을 안해서 결과가 이상하게 남! ㅋㅋ 
        result +=i 
    else:
        result *=i

print(result)


'''