n = int(input())
scary =list(map(int, input().split()))

scary.sort()

groupNum = 0

count = 0 #현재 그룹에 포함된 모험가의 수

for i in scary: #scary에서 하나씩 꺼내와서 비교
    count += 1
    if count >= i: #지금 꺼내온 수가 포함된 사람의 수보다 크거나 같으면 
        groupNum += 1 # 그룹을 하나 만들기
        count =0 #count 초기화 
        
print(groupNum)
    
'''
1. 문제설명 
    1)최소로 그룹을 이룰 수 있는 공포도
    2)각 모험가별 공포도 입력받기 
    3)오름차순으로 정렬
    4)현재 그룹에 포함된 모험가의 수 >= 현재 모험가의공포도 일때 그룹을 형성
2. 접근방법 
그리디 
3. 느낀점 
for i in scary:로 코딩하면 더 좋은데, for i in range(len(scary))로 코딩했.... 

'''   