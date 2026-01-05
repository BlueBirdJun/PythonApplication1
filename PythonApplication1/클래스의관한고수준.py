"""
클래스 정의할때 [___str___()] 이름의 메서드를 정의해 둘수가 있습니다.
그러면 내장함수 str()의 인수에 이 클래스의 인스턴스 를 지정했을때  이 __str___() 메서드가 호출됩니다.

"""

class Person:
    name:str
    def __init__(self,**arg):
      name =arg[0]
    

p = Person("홍길동")

print(p.name)  # <__main__.Person object at 0x...>0
print(str(p))  # <__main__.Person object at 0x...>