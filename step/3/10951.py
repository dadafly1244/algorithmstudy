# try:
#   while True:
#     a, b = map(int, input().split())
#     print(a+b)
# except:
#   print('error')

while True:
  try:
    a, b = map(int, input().split())
    print(a+b)
  except:
    break


'''
test 케이스 개수가 정해져 있지 않은 것이 가장 큰 특징!!

try except를 연습 할 수 있는 문제!! 

try: 실행코드 
except: 예외처리 코드!!(오류 발생시 이걸로 처리!)
else: 예외 처리할 오류가 없을 때 실행되는 코드
finally: 오류발생여부와 상관 없이 무조건 실행되는 코드
raise:오류를 일부러 발생시키기

1. try & except 

2. try & except & else
try에서 오류가 나지 않으면 else 실행

3. try & except & else & finally
- 오류가 나지 않았을 때 : else와 finally가 실행됨
- 오류가 났을 때 : except와 finally가 실행됨

참고 :
- https://yganalyst.github.io/pythonic/memo_16_except/
- https://dojang.io/mod/page/view.php?id=2398
'''