# 입력 받은 값 정수형이 아닐때 try except 문 사용하기
# 입력 받은 값에서 정수만 뽑아내기
from pickle import NONE
import re
import step3

step3.Print1()

step3.Print3()

def str_to_int(s):   
    try:
        return int(s)
    except ValueError:
        print("정수를 입력해주세요.")
        return None

def str_to_getnumber(s):   
    try:
        numbers = re.findall(r'\d+', s)
        if numbers is NONE or len(numbers) == 0:
            print("정수를 입력해주세요.")
            return None
        
        combine =''.join(numbers)
        return int(numbers[0])
    except ValueError:
        print("정수를 입력해주세요.")
        return None

while True:    
    inputcost = str_to_getnumber(input("매출을 입력하세요 "))
    if inputcost is not None:
        break





if inputcost > 100:
    print("매출이 100보다 큽니다.")
else:
    print("매출이 100보다 작습니다.")

sale =10
print ("Initial sale:", sale,"dolor")

inputval = input("Enter new sale value: ")
print("Input value:", inputval)
intval =int(input("Number"))
print("Number value:", intval+3)