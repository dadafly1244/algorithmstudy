'''
부품찾기 이진탐색 문제 !! 

n개의 부품중에서 m개의 부품을 확인하는 문제 
5개의 부품을 입력받고 8 3 7 9 2
3개의 부품이 있는지 입력받음 5 7 9
부품이 있으면 yes 없으면 no 

계수정렬 풀이

'''

n = int(input())
data =[0]*1000001

#가계에 있는 전체 부품 번호 입력 받아서 기록 
for i in input().split():
    data[int(i)] = 1 

print(data[:40])

#손님입력
m = int(input())
need_check = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인. 
for i in need_check:
    #해당 부품이 존재하는지 확인!
    if data[i] == 1:
        print('yes',end=' ')
    else:
        print('no',end =' ')

