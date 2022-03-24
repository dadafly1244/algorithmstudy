'''
문제 : 
학생n명을 이름, 국어, 영어, 수학 점수를 입력 받음. 
국어점수 오름차순, 국어점수 같으면 수학점수 내림차순, 모든점수 같으면 영어점수 오름차순 순서로 이름출력하기! 

접근방법 
리스트

'''


n = int(input())


student =[]

for _ in range(n):
    student.append(input().split())
    
    
# student.sort(key= lambda x : (int(-x[1]),int(x[2]),int(-x[3]), x[0]))
student.sort(key= lambda x : (-int(x[1]),int(x[2]),-int(x[3]), x[0]))


for i in student:
    print(i[0])