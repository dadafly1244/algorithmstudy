
'''
# 문제 설명 :

고정값문제 

오름차순으로 정리된 배열을 입력받아서 배열의 값과 인덱스의 값이 일치하는 값이 있으면 그 값을 출력하고, 없으면 -1 출력하는 문제


'''


'''

풀이 접근방법 : 오름차순 정리..!! 이진탐색을 쓸 수 있다!!  중간점 인덱스 값에 가서 값을 살펴 봤는데 작으면 왼쪽 크면 오른쪽으로가기! 

'''
def find_fixed_point(array, start, end):
    
    while start <= end:
        mid = (start + end)//2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1 
            
        else:
            end = mid -1
    return None

n = int(input())

data = list(map(int, input().split()))

result = find_fixed_point(data, 0, n-1)

if result == None:
    print(-1)
else:
    print(result)
    

            