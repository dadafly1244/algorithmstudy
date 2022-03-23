'''
문제 : 몇명의 학생을 입력 받을지 입력받음.!
학생이름과 점수를 입력 받아서 점수가 낮을 순으로 이름을 출력하기!

접근방법 : 튜플로 입력받아서 sort함수의 key에 lambda함수를 이용해서 오름차순으로 정렬하기! 

'''


n = int(input())

lst =[]
for _ in range(n):
    student = input().split()
    lst.append((student[0],int(student[1])))
    
#print(lst)
lst.sort(key= lambda x: x[1])
# lst = sorted(lst, key = lambda x: x[1]) 이거랑 위에랑 같음!! 

#print(lst)
for i in lst:
    print(i[0], end= ' ')
    



'''
sort() 원형을 변형시켜서 sort함!!1
리스트.sort()
sorted() 원형을 변형시키지 않음!! 
새로운 리스트 = sorted(기존리스트)


lambda 매개편수: 표현식!!



key의 경우 
정렬을 목적으로 함수를 넣음!! 
>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list, key=len))  # 함수
['굿모닝', '좋은하루', 'niceday', 'good_morning']

>>> print(sorted(str_list, key=lambda x : x[1]))  # 람다
['niceday', 'good_morning', '굿모닝', '좋은하루']


튜플도 가능! 
>>> tuple_list = [('좋은하루', 0),
    	          ('niceday', 1), 
    	          ('좋은하루', 5), 
    	          ('good_morning', 3), 
    	          ('niceday',5)]
                  
>>> tuple_list.sort(key=lambda x : (x[0], x[1]))  # '-'부호를 이용해서 역순으로 가능! 예를 들면 x[0]: 오름차순, -x[1] : 내림차순
>>> print(tuple_list)
[('good_morning', 3), ('niceday', 1), ('niceday', 5), ('좋은하루', 0), ('좋은하루', 5)]

'''