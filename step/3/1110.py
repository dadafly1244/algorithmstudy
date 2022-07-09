# import sys 
# input = sys.stdin.readline

# n = int(input())
# count = 0
# one = n // 10 
# two = n % 10 
# while True: 
#   if n == one:
#     break
#   one = one + two 
#   if one < 10:
#     one *= 10
#   else:
#     one //= 10 
#     two = one % 10 
#   count += 1
#   #print(count, one, two)
# print(count)
# 문제를 잘 이해를 못했음!!! 
######

import sys 
input = sys.stdin.readline
n = int(input())
num = n 
count = 0

while True:
  a = num//10
  b = num % 10
  c = (a + b) % 10
  num = (b * 10) + c
  count += 1
  if num == n:
    break

print(count)