'''
0시 0분 0초 부터 h시 59분 59초 까지  시분초에 3이 포함 되어 있으면 카운트를 1 늘리는 방법 
접근 방법 
그냥 3중 for문을 돌면서 시간을 다 문자로 바꿔서 3이 포함되어 있는지 체크하고 있으면 count에 1을 늘려주기! 

느낀점 :
문자포함 여부는 문자로 체크해야 한다는 것!! 
'''

h = int(input())


count =0 
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
                
print(count)