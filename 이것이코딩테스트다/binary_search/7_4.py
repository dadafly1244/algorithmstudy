'''
input()이 동작 속도가 느려서 시간초과될 떄!1


'''

import sys
#하나의 문자열 데이터 입력받기 
input_data = sys.stdin.readline().rstrip()

#임력받은 문자열 그대로 출력
print(input_data)