#파이썬에서 입력을 받아서 문자열인지 정수인지 확인하는 방법을 보여주는 예제를 짜줘
# region 입력 받기

 

#1. 리스트 컴프리헨션(List Comprehension)
"""
var squared = numbers.Select(x => x * 2);
기존 반복문 + append 를 한 줄로 표현하는 문법.
"""
numbers = [1, 2, 3, 4]
squared = [x * 2 for x in numbers]
print(squared)   # [2, 4, 6, 8]

#2. 딕셔너리 / 집합 컴프리헨션
"""

"""
# dict
dic = {x: x * 2 for x in range(5)}

# set
s = {x for x in [1, 2, 2, 3, 3]}

# 3. 제너레이터(Generator)
"""
메모리를 거의 쓰지 않는 지연 평가(iterable)
yield 키워드가 핵심.
"""
def gen_numbers():
    for i in range(3):
        yield i

for n in gen_numbers():
    print(n)

# 데코레이터(Decorator)
"""
함수를 감싸서 기능을 추가하는 문법. (AOP 느낌)
"""
def logger(func):
    def wrapper():
        print("함수 실행 전")
        func()
        print("함수 실행 후")
    return wrapper

@logger
def hello():
    print("Hello")

hello()

"""
num1 = input()
num2 = input()

def minus(a,b):
    return a-b
    
result =minus(int(num1),int(num2)) 
    
print(result)


# region 유틸 함수

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# endregion

# bool 형
bchk = True
# 배열형 
arr = [1, 2, 3, 4, 5]

# 딕셔너리형
dict = [{"name": "홍길동", "age": 25},{"name": "고길동", "age": 32}]

print(dict[0]["name"] ,dict[1]["age"])

# 반복문
for i in range(5):
    print(f"Index: {i}, Value: {arr[i]}")

"""
