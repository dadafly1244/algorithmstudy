data = input()
strstr = []
num = 0

for i in data:
  if i.isalpha():#알파벳
    strstr.append(i)
  else: 
    num += i
    
strstr.sort()

if num != 0:
  strstr.append(str(num))
  
print(''.join(strstr)) #배열을 문자열로 변환하는거!! 문자열사이에 /를 넣고 싶으면 '/'.join(strstr)
    
  