
n, m, k  = map(int, input().split()) #n = 배열크기, m= 더해지는 횟수, k=연속해서 몇번 더할 수 있는지  
lst = list (map(int, input().split()))

lst.sort(reverse=True)
n1 = lst[0]
n2 = lst[1]

result =0

while True:
    for i in range(k):
        if m==0:
            break
        result += n1
        m -=1
    if m==0:
        break
    result += n2
    m-=1
    
print(result)

'''
1. 문제설명 
    1)배열의 크기, 총 몇개의 숫자를 더 할것인지, 한 숫자를 몇번까지 반복해서 받을 수 있는지를 입력받음
    2)배열을 입력받음
    3)입력받은 배열을 오름차순으로 정렬함 
    4)제일 큰 수를 반복 가능한만큼 반복해서 더하고 반복가능 횟수가 끝나면 두번째 수를 더함 
2. 접근방법 
그리디 
3. 느낀점 
처음에 while에 True말고 m>=0을 넣어서 했는데 숫자가 이상하게 나옴... 
for문에서 총 더할 수 있는 숫자를 다 더하면 빠져나와야하기 때문이었음!!! 
lst.sort(reverse=True) 오름차순 
'''
