'''
이진 탐색 : 반으로 쪼개면서 탐색하기

**배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있음!!** 

찾으려는 데이터와 중간점(middle) 위치에 있는 데이터를 반복적으로 비교 (시작점, 끝점, 중간점 변수 사용!!)

시간복잡도 O(logN)

이진 탐색 구현방법 

1. 재귀함수
2. 단순반복문

** 외우기 !!1 

'''

# 1. 재귀함수

def binary_search(array, target, start, end):
    if start > end: #시작이랑 끝점이 잘 설정되었는지 보기!
        return None
    mid = (start + end) //2
    #찾은 경우 중간점 인덱스 반환 
    if array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid -1)
    #중간점의 값보다 찾고자 하는 값이 큰은 경우 오른쪽 확인
    else:
        return binary_search(array,target, mid+1, end)
    

#n(원소의 개수)과 target(찾고자하는 문자열)을 입력받기 
n, target = list(map(int, input().split()))
#전체 원소 입력받기 
array = list(map(int, input().split()))


#이진탐색수행하기 
result = binary_search(array, target,0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) #인덱스번호는 0부터 시작이기때문에 1 더해주기!1 


    