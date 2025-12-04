
a =11 
b ="hello"  
c =[1,2,3]
d ={"name":"Alice","age": 30}

print("hello world")
print(a)

x =10

if x > 10:
    print("x is greater than 10")
elif x == 10:
     print("x is equal to 10")
else :
     print("x is less than 10")
items = [1, 2, 3, 4, 5]
for x in items:
        print(x)

for idx, value in enumerate(items):
        print(f"Index: {idx}, Value: {value}")

squres = [x*x for x in range(10)]
print(squres)

def add(a,b):
        return a + b

class Dog:
        def __init__(self, name):
                self.name = name
        def bark(self):
                return "Woof!"


