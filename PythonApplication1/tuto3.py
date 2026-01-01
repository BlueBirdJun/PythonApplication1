from pickle import TRUE
from functools import wraps

def Decoration(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("별 출력 시작 ", args[0])
        result = func(*args, **kwargs)
        print("별 출력 끝",func)
        return result
    return wrapper


# 2️⃣ 데코레이터 적용
@Decoration
def starprint(n):    
    try:
        for i in range(n):
            print('*' * (i + 1))
    except Exception as  e:
         print(e)
          

starcount=0

#while starcount > 20: 
while starcount < 20:            
        starcount= int(input("별 개수 입력: "))
        starprint(starcount)


