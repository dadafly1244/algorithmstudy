'''
소팅을 통해서 그냥 하면 된다고 생각함!! 
n = int(input())

data = []

for _ in range(n):
    data.append(int(input()))
    
    
data.sort()
result = data[0] + data[1]
for i in data:
    if i == data[0] or i == data[1]:
        continue
    result += i 
    
print(result)


틀림.....항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장 !!  나는 합친 카드도 다시 정렬해야한다는 것을 생각 못함!!
'''


'''
문제 : 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장 !! 
우선순위큐를 사용하면 항상 가장 작은 크기의 두 카드 묶음을 가져올 수 있음. 
https://velog.io/@mein-figur/Python%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-heapq
https://www.daleseo.com/python-priority-queue/

우선순위 큐 만들기 1 

from queue import PriorityQueue
que = PriorityQueue()
만약 최대 크기를 설정하고 싶으면 
que = PriorityQueue(maxsize=8)
que.put(1)
print(que.get())  # 1

다른 기준으로 정렬하고 싶으면  (우선순위, 값)으로 해주기!! 
que.put((3, 'Apple'))
que.put((1, 'Banana'))
que.put((2, 'Cherry'))

print(que.get()[1])  # Banana
print(que.get()[1])  # Cherry
print(que.get()[1])  # Apple
PriorityQueue 클래스의 put(), get() 함수는 O(log n)의 시간 복잡도를 가짐. 


우선순위큐 만들기 2:

import heapq

hq = []


* push
heapq.heappush(heap, item)
>힙의 형태를 유지하면서 item을 push
heapq.heappush(hq, 4)

*pop
heapq.heappop(heap)
>힙의 형태를 유지하면서 가장 작은 항목을 pop, 반환
>비어있으면 IndexError 발생
>반환하지 않고 접근하고 싶다면, heap[0] 활용
heapq.heappop(hq) # 1

*heapify
heapify(x)
>리스트 x를 선형 시간으로 제자리에서 heap으로 변환
x = [4, 3, 1, 2, 5, 6]
print(x) # [4, 3, 1, 2, 5, 6]
heapq.heapify(x)
print(x) # [1, 2, 4, 3, 5, 6]


'''

import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
    
result = 0

#힙에 원소가 1개 남을 때 까지 
while len(heap) != 1:
    #가장 작은 2개의 카드 묶음 꺼내기 
    one= heapq.heappop(heap)
    two= heapq.heappop(heap)
    #카드 묶음을 합쳐서 힙에 다시 삽입 
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap,sum_value)
    
    
print(result)