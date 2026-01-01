# 사람(Person)을 표현하는 클래스
class Person:
    # 생성자: 객체가 만들어질 때 자동으로 호출됨
    def __init__(self, name, age):
        # self는 "이 객체 자기 자신"
        self.name = name
        self.age = age

    # 인스턴스 메서드
    def introduce(self):
        print(f"이름: {self.name}, 나이: {self.age}")


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    # 입금
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원 입금, 잔액: {self.balance}")

    # 출금
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족")
            return

        self.balance -= amount
        print(f"{amount}원 출금, 잔액: {self.balance}")

class Employee:
    # 클래스 변수 (모든 객체가 공유)
    company = "ABC Corp"

    def __init__(self, name):
        # 인스턴스 변수 (객체마다 다름)
        self.name = name

    def show_info(self):
        print(f"{self.name} / {Employee.company}")



# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("소리를 낸다")

# 자식 클래스
class Dog(Animal):
    def speak(self):
        print(f"{self.name}: 멍멍")

#실무 느낌: 로그 찍는 클래스
import datetime

class Logger:
    def __init__(self, service_name):
        self.service_name = service_name

    def log(self, message):
        now = datetime.datetime.now()
        print(f"[{now}] [{self.service_name}] {message}")
