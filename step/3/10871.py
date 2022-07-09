import sys
input = sys.stdin.readline

n, x = map(int, input().split())

data = list(map(int, input().split()))

result = []
for i in range(n):
  if data[i] < x:
    result.append(data[i])

for i in result:
  print(i, end=' ')