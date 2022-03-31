'''
부품찾기 이진탐색 문제 !! 

n개의 부품중에서 m개의 부품을 확인하는 문제 
5개의 부품을 입력받고 8 3 7 9 2
3개의 부품이 있는지 입력받음 5 7 9
부품이 있으면 yes 없으면 no 

집합자료형 풀이

'''

n = int(input())
#가게에 있는 전체 부품 번호를 입력 받아서 집합(set) 자료형에 입력 받음. 
data = set(map(int, input().split()))



m = int(input())
need_check = list(map(int, input().split()))


#하나씩 확인..
for i in need_check:
    #해당 부품이 존재하는지 확인
    if i in data:
        print('yes',end=' ')
    else:
        print('no',end=' ')
        
'''
이진탐색에서 list에서 in을 안쓰고 set을 쓰는 경우 
https://kyleyj.tistory.com/56

'''
