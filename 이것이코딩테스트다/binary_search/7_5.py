'''
부품찾기 이진탐색 문제 !! 

n개의 부품중에서 m개의 부품을 확인하는 문제 
5개의 부품을 입력받고 8 3 7 9 2
3개의 부품이 있는지 입력받음 5 7 9
부품이 있으면 yes 없으면 no 

이진탐색 이용 풀이

'''


n = int(input())
data = list(map(int, input().split()))
data.sort() #이진탐색을 쓰기 위해서 정렬해야함!! 


m = int(input())
need_check = list(map(int, input().split()))

need_check.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end)//2 
        if array[mid] == target:
            return mid
        elif array[mid]  > target:
            end = mid -1
        else: 
            start = mid + 1
            
    return None 


for i in need_check:
    if binary_search(data, i, 0 , n-1) == None:
        print("no", end = " ")
        
    else:
        print("yes", end = " ")