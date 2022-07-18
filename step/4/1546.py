import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
maxValue = max(data)
result = 0

for i in data:
  i = i / maxValue*100
  result += i

print(result/n)


# 다른 사람풀이
# n = int(input())
# s = [int(x) for x in input().split()]

# ss = sum(s)
# print(ss/max(s)*100/n)

# sum 이용하기
# 연산을 여러번 할 필요 없이 다 더하고 난 다음에 해도 상관없네!!