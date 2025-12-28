# list / dict comprehension + 조건
# 0~9 중 짝수만 제곱
squares = [x * x for x in range(10) if x % 2 == 0]
print(squares)
##################################
# 길이가 3 이상인 단어만 길이로 매핑
words = ["ai", "python", "dto", "model"]
length_map = {w: len(w) for w in words if len(w) >= 3}
print(length_map)

##################################
# unpacking (실무에서 매우 많이 씀)
# 리스트 언패킹
a, b, *rest = [1, 2, 3, 4, 5]
print(a, b, rest)

##################################
# 딕셔너리 병합 (Python 3.9+)
base = {"a": 1}
extra = {"b": 2}
merged = base | extra
print(merged)

##################################
#함수 고급 문법 (기본값 + 타입힌트)
def calc(price: int, tax: float = 0.1) -> int:
    # 기본값 + 타입 힌트
    return int(price * (1 + tax))

print(calc(1000))
print(calc(1000, 0.2))

##################################
#lambda + sorted (면접/실무 단골)
users = [
    {"name": "kim", "age": 30},
    {"name": "lee", "age": 25},
]

##################################
# 나이 기준 정렬
users_sorted = sorted(users, key=lambda u: u["age"])
print(users_sorted)

##################################
# @property (get/set 패턴)
class User:
    def __init__(self, age: int):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("age는 0 이상")
        self._age = value

u = User(30)
u.age = 40
print(u.age)

##################################
# with 문은 자원 자동 해제
with open("test.txt", "w") as f:
    f.write("hello")

# f.close() 자동 호출됨

####################
# generator (메모리 절약 핵심)
def even_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i  # 값을 하나씩 반환

for n in even_numbers(10):
    print(n)

##################################
#try / except / else / finally (고급 예외 흐름)

try:
    x = int("10")
except ValueError:
    print("변환 실패")
else:
    print("성공:", x)
finally:
    print("항상 실행")

