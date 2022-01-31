# Python 자습서 공부하기! 
by 양다영

<br>
<br>

## 22년 1월 31일
>자습서 보면서 새로 배운 부분 
### *name와 **name2의 뜻
* 참고 : https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs , https://sshkim.tistory.com/182

1.  *name : 파라미터를 몇개를 받을지 모르는 경우 사용함. *name은 튜플 형태로 전달됨 
  ```python
def print_param(*name):
    print(name)
    for p in name:
        print(p)

  print_param('a','b','c')
    #('a','b','c')
    #a
    #b
    #c
```

2.  **name2 : 파마미터 명을 같이 보낼 수 있다. name2는 딕셔녀리 형태로 전달 
```python
def table_things(**kwargs):
     for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

table_things(apple = 'fruit', cabbage = 'vegetable')
#apple = fruit
#cabbage = vegetable
```

3. 자습서에서 이를 활용한 부분 

```python

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch          


```
4. 인자 목록 언 패킹에서도 사용함. 

```python
args = [3,6]
list(range(*args))
#[3, 4, 5]

#------------
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
#-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !


```

<br>
<br>

