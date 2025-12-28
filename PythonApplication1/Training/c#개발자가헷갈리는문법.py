#public / private 없음 (관례만 있음)
class A:
    def __init__(self):
        self.public = 1
        self._protected = 2   # 관례
        self.__private = 3    # name mangling

#✔ _ : 건들지 마세요
#✔ __ : 클래스 내부 전용


# 인터페이스 없음 → Duck Typing
class RepoA:
    def get(self): ...

class RepoB:
    def get(self): ...

def service(repo):
    repo.get()  # 타입보다 "행동"

# new 키워드 없음
user = UserDto(1, "kim")

#None 비교는 == ❌ / is ✅
if user is None:
    print("없음")

# 참조 전달 (값 복사 아님)
a = [1, 2]
b = a
b.append(3)

print(a)  # [1,2,3]

#default parameter 함정 (중요)
def add_item(item, items=[]):  # ❌
    items.append(item)
    return items
# 올바른 방법
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

# if 문은 표현식이다
result = "A" if score > 80 else "B"

# for 문에 index 없음 (기본)
for i, value in enumerate(["a", "b", "c"]):
    print(i, value)

# 예외는 리턴값이 아니라 흐름 제어
try:
    int("x")
except ValueError:
    pass
