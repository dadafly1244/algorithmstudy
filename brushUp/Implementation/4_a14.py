'''
외벽 점검
https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3

1<= n <= 200 자연수
1<= weak의 길이 <= 15
1<= dist의 길이 <= 8 

weak과 dist의 길이가 짧기 때문에 완전탐색이 가능함!! 
모든친구를 순열로 나열하고 경우의 수를 각각 확인하면 됨! 

'''

from itertools import permutations #순열

def solution(n, weak, dist):
    length = len(weak) #길이 2배
    for i in range(length):
        weak.append(weak[i] + n) # 선형형테로 변환!! 
    answer = len(dist) + 1 #전체 친구의 수로 초기화 최대길이 8 
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):  #dist의 길이개의 원소로 수열 만들기
            count = 1 #투입할 친구 수 
            position = weak[start] + friends[count - 1] #해당친구가 점검 할 수 있는 마지막 위치 
            for index in range(start, start + length):
                if position < weak[index]: #점검 위치 벗어나는 경우
                    count += 1 # 새로운 친구를 투입
                    if count  > len(dist): # 더 투입 불가능하면
                        break # 종료
                    position  = weak[index] + friends[count - 1]
            answer = min(answer, count) #최소값..!!
    if answer > len(dist): 
        return -1 #모두 투입해도 점검할 수 없는 경우 -1 
    return answer

  
'''
방법 2: dist가 큰 친구부터 차례로 위치 시킴 set 이용하여 모든 취약 지점이 수리 되었는지 확인
결론적으로 방법2가 훨씬 더 시간효율은 높음.

https://velog.io/@tjdud0123/%EC%99%B8%EB%B2%BD-%EC%A0%90%EA%B2%80-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-python
'''