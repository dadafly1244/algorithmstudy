'''
정렬된 배열에서 특정 수의 개수 구하기 
문제 설명 : n개의 원소를 포함하고 잇는 수열이 오름차순으로 정렬 되어 있다. 이 수열에서 x가 등장하는 횟수를 계산하시오. 
시간 복잡도가 O(log N)이 되어야 합격!! 

'''


'''
# 나의 접근 방법
부품찾기를 계수정렬로 푼 풀이가 생각이 났다. 
계수 정렬로 풀면 되지 않나? 해서 계수 정렬로 풀었음.... 답도 잘 나온다 ㅋㅋ
근데 찾아보니까 ㅋㅋㅋㅋㅋㅋ 시간복잡도가 O(n)이라고 한다. 
다시 풀어야 할 것 같다. 

'''
'''
내 코드
n, x = map(int, input().split())

data = [0] * 1000001

for i in input().split():
    data[int(i)] += 1

if data[x] >0:
    print(data[x])
else:
    print(-1)

'''

#정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드 
from tkinter import W


    
#첫 위치 탐색
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    
    #해당 값을 가지는 원소 중에서 가장 왼쪽에 잇는 경우에만 인덱스 반환 
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    #중간점에서 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽확인 
    elif array[mid]>=target:
        return first(array, target, start, mid-1)
    #중간점의 값보다 찾고자 하는 값이 크거나 같은 경우 오른쪽 확인
    else:
        return first(array, target, mid +1 , end)
    
#마지막 위치 탐색
def last(array, target, start, end):
    if start >end:
        return None
    mid = (start + end)//2
    
    #해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우 인덱스 반환
    if (mid == 0 or target < array[mid+1]) and array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인. 
    elif array[mid] > target:
        return last(array, target, start, mid -1)
    #중간점의 값보다 찾고자 하는 값보다 큰 경우 오른쪽 확인
    else:
        return last(array, target, mid +1, end)
    
#정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드    
def count_by_value(array,x):
    n= len(array)
       
    #x가 처음 등장한 인텍스 계산    
    a = first(array, x, 0,n-1)
    if a == None:
        return 0
    
    b = last(array, x, 0,n-1)
    
    return b - a +1



n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array,x)

if count == 0:
    print(-1)
else:
    print(count)
    
    