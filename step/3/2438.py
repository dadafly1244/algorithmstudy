# import sys
# input = sys.stdin.readline

# n = int(input())

# star = ''
# for i in range(n):
#   for j in range(i + 1):
#     print('*',end='')
#   print('')

##### format의 정렬을 사용해서 간단하게 표현하는 방법이 있음!! 근데 문제에서는 출력형식이 잘못되었다고 나옴!! 
# import sys
# input = sys.stdin.readline

# n = int(input())

# for i in range(n):
#   print('{:<5}'.format('*' * (i+1))) #5칸중에서 왼쪽 정렬 , 오른쪽 정렬 >, 중간정렬 ^


######걍 이중 포문 안쓰고 하는 방법!!
import sys
input = sys.stdin.readline

n = int(input())
for i in range(5):
    print('*' * (i+1))