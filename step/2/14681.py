x = int(input())
y = int(input())

if x> 0 and y > 0: #양양 1사분면
  print(1)
elif x < 0 and y > 0: #음양 2사분면
  print(2)
elif x < 0 and y < 0: #음음 3사분명
  print(3)
else: 
  print(4)