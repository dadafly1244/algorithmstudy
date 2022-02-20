'''
1. 문제설명
N이 1이 될때까지 
1)N-1 or N/K(K로 나누어 떨어질 때만 !!)
2. 접근방법 
그리디 
3. 느낀점... 엥...? 왜 책에서는 반복문을 2개를 만들어서 두번 도는거지..? 흠...?

'''

n , k = map(int, input().split())
count = 0

while True:
    if n == 1: #n이 1이면 멈춤
        break
    if n % k == 0: # 숫자가 k로 나눠떨어지면 k로 나누기 
        n /= k 
        count += 1
    else: #k로 나눠떨어 지지 않으면 1빼기 
        n -= 1
        count +=1 
        
print(count)