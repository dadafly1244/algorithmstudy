
'''
n개의 원소를 가지는 두 배열을 입력 받음. 
원소를 k번 바꿀 수 있는데, a 배열의 합이 최대가 될 수 있도록 만드는 것!! 

'''


n , k =  map(int,input().split())

#입력 잘못 받았네....? 헣헣 숫자 하나 치고 엔터해야 받아짐.. 
# a = []
# b = [] 
# for _ in range(n):
#     a.append(int(input()))

# for _ in range(n):
#     b.append(int(input())) 

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #오름차순
b.sort(reverse= True)#내림차순

for i in range(k):
   if a[i] < b[i]:
        a[i] , b[i] = b[i] , a[i]
   else: # 설정해주기!!! 아니면 시간을 낭비할 듯!! 
       break
        

print(sum(a))


    
    