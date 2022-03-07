data = input()
result=[]
value =0

for i in data :
    #알파벳인 경우에 리스트에 넣기
    if i.isalpha():
        result.append(i)
    else:
        #숫자면 더하기
        value += int(i)
        
result.sort()

if value != 0:
    result.append(str(value))
    
#print(result) 리스트로 표시됨! 
print(''.join(result))


'''
1.문자열 입력 받아서 문자는 알파벳 순으로 정렬하고 숫자는 다 더해서 마지막에 붙이기
2. 접근법 : 그대로 구현하기 

3. 리스트를 문자열로 나타내기!! 

* ''.join(리스트)
''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수

* '구분자'.join(리스트)
'구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줌
'_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줌



출처: https://blockdmask.tistory.com/468 [개발자 지망생]

'''
