h, m = map(int, input().split())
inputval = int(input())

h += inputval //60
m += inputval % 60 

if m >= 60:
  h += 1
  m -= 60

if h >= 24:
  h -= 24

print(h, m)