import sys
input = sys.stdin.readline
maxval = 0 
count = 0
for i in range(9):
  n = int(input())
  if n > maxval:
    maxval = n
    count = i + 1

print(maxval)
print(count)