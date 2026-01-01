# 리스트 언패킹 

from heapq import merge
from typing import Self


a,b, *rest = [1,2,3,4,5]
print(a,b, rest)

c,d,e, *rest1 = [1,2,3,4,5]
print(c,d,e, rest1)
# 1 2 [3, 4, 5]


base = {"a":1}
extra = {"b":2}
merge = base | extra

print(merge.get("a"))
merge.update({"c":3})
merge.pop("c") # remove key c
print(merge)
# {'a': 1, 'b': 2}

def calc(price: int, tax: float = 0.1) -> int:
    return int(price * (1 + tax) )

print(calc(100))
               
               
users=[
    {"name":"kim", "age":30},
    {"name":"lee", "age":25},
]

users_sorted = sorted(users, key=lambda u: u["age"])
users_sel = list(filter(lambda u: u["age"] > 26, users))
print(users_sorted)
print(users_sel)
print(len(users_sel))

class User:
    def __init__(self,age:int):
      self._age = age
    
    @property
    def age(self):
       return self._age
   
    @age.setter
    def age(self,value):
       if value < 0:
           raise ValueError("age 는 0이상")
       self._age =value
u =User(30)
u.age = 30
print(u.age)

try:
    x=int("10a")
except ValueError:
      print("예외 발생")
else :
      print("예외 없음")
finally:
       print("무조건 실행")


class Repo:
    def get(self):
                return "data"

class Service:
    def __init__(self, repo: Repo):
        self.repo = repo

    def run(self):
        return self.repo.get()


def model_factory(name: str):
    if name == "gpt":
        return lambda x: f"GPT:{x}"
    if name == "bert":
        return lambda x: f"BERT:{x}"
    raise ValueError()

model = model_factory("gpt")
print(model("hello"))