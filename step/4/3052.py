import sys 
input = sys.stdin.readline

data = [0] * 42

for i in range(10):
  n = int(input())
  data[n % 42] +=1

count = 0 
for i in data:
  if i > 0:
    count += 1

print(count)

#다른 사람 풀이 1
# a=[]
# for i in range(10):
#     a.append(int(input())%42)
# print(len(set(a)))
# set을 사용하면 중복되는 수를 없앨 수 있어서 더 간단하네!! 대박


# 다른 사람 풀이 2
# b = [int(input())%42 for i in range(10)]
# print(len(set(b)))
# 배열을 초기화 하는 코드를 사용해서 풀 수 있다니!!