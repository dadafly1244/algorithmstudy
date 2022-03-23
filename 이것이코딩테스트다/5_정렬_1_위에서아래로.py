'''
위에서 아래로 !
문제 설명 : 몇개의 숫자를 받을지 입력 받은 후 입력 받은 숫자를 내림차순으로 정렬하는 문제!
접근방법 : sort()함수쓰기!

'''



n= int(input())
lst = []

for _ in range(n):
  lst.append(int(input()))

lst.sort(reverse = True)

#print(lst)# 문제에서 원하는 형태가 아니군..!!  [96, 22, 15]

for i in lst:
  print(i,end = ' ')