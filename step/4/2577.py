import sys
input = sys.stdin.readline

data = [0] * 10

n = 1 
for i in range(3):
  a = int(input())
  n *= a
#print(n)
while n > 0:
  index = int(n % 10)
  #print('print index',index)
  data[index] +=1
  n //= 10

for i in range(10):
  print(data[i])