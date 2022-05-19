'''
거스름돈
p 87
'''

n = int(input())
list = [500, 100, 50, 10]
count = 0

for big in list:
  count += (n // big)
  n %= big

print(count)


'''
복습 포인트 
가장 큰 돈 부터 거슬러주기
// : 몫을 반환
% : 나머지 연산자

'''