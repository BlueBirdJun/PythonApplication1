# __init__과 __call__의 차이점  init 는 객체가 생성될 때 호출되고, call 은 객체가 함수처럼 호출될 때 실행됩니다. 파이썬은 이 두 메서드를 통해 객체의 초기화와 함수 호출을 다르게 처리할 수 있습니다.

class A:
    def  __init__(self):
      print("__init__ 호출됨")
    def __call__(self):
        print("__call__ 호출됨")

class B:
    def __call__(self, *args, **kwds):        
        print("__call__ 호출됨1 with args:", args, "and kwds:", kwds)      

a = A()  # __init__ 호출됨   
b = B()  # __init__ 호출되지 않음

a()  # __call__ 호출됨
b(1,2,3,4)
b(test="value")
b(1, "aa", name="test", value=42)
b(2, debug=True)


class Malma():
    def __init__(self,name):
       self.name=name+" Malma"
    def walk(self):
        print(f"{self.name} is walking")
    def eat(self):
        print(f"{self.name} is eating")

class Human(Malma):
    def __init__(self, name,hand):
        super().__init__(name)  
        self.name=name
        self.hand=hand
    def wave(self):
        print(f"{self.name} is waving with {self.hand}")    
        

class C():
    def __init__(self,value):
        value.walk()
    
        
person = Human("Alice","right hand")
person.wave()
person.walk()

C = C(person)

class D():
    __slots__ ='arg1','arg2'
    def __init__(self,arg1,arg2):
        self.arg1 = arg1
        self.arg2 = arg2

qh = D("value1","value2")

qh.arg2="value3"  # AttributeError: 'D' object has no attribute 'arg3'"

import matplotlib.font_manager as fm
from matplotlib import rc
font_name = fm.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)