'''
우선순위 큐 참고: https://velog.io/@mein-figur/Python%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90-heapq
문제 https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3


'''


import heapq

def solution(food_times, k):
    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times)<=k:
        return -1
        
    #시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    hq = []
    for i in range(len(food_times)):
        #(음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(hq,(food_times[i],i+1))
        
    sum_value =0 #먹기 위해 사용한 시간
    previous =0 #직전에 다 먹은 음식 시간 
    length = len(food_times) #남은 음식의 개수
    
    #sum_value + (현재의 음식 시간 - 이전의 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((hq[0][0] - previous) * length) <= k:
        now = heapq.heappop(hq)[0]
        sum_value += (now - previous) * length
        length -= 1 #다먹은 음식 제외
        previous = now #이전 음식 시간 재설정
        
    result = sorted(hq, key=lambda x: x[1]) #음식의 번호 기준으로 정렬
    return result[(k-sum_value) % length][1]
    
  