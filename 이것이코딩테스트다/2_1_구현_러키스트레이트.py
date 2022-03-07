from traceback import StackSummary


n = input()
L =0 
R=0

for i in range(len(n)//2):
    L += int(n[i])

for i in range(len(n)//2,len(n)):
    R += int(n[i])
    
if L == R :
    print('LUCKY')
else:
    print('READY')
    
'''
책 풀이 
n = input()
length =  len(n)
summary = 0 

#왼쪽 
for i in range(length//2):
    summary += int(n[i])

#오른쪽 빼기 
for i in range(length//2, length):
    summary -= int(n[i])
    
if summary == 0:
    print('LUCKY')
else:
    print('READY')

'''