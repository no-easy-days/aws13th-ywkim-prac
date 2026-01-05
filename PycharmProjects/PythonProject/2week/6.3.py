# 문제 1: 기본 클래스 만들기
class Student:
    def __init__(self, name, student_id, grade):
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def introduce(self):
        print(f'안녕하세요 {self.grade}학년 {self.name}입니다. (학번 : {self.student_id})')


kim = Student("김철수", "2024001", 1)
kim.introduce()
# 문제 2: 상태 관리하기
class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        self.balance -= amount
        if self.balance < 0:
            return print("잔액이 부족합니다")
        return self
    def get_balance(self):
        return self.balance



account = BankAccount("홍길동")
account.deposit(10000)
account.withdraw(3000)
print(account.get_balance())  # 7000

account.withdraw(10000)  # 잔액이 부족합니다

#  ## 문제 3: 리스트 속성 관리하기
class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def complete_task(self, task):
        self.tasks.remove(task)
    def show_tasks(self):
        for i,task in enumerate(self.tasks,start=1):
            print(f"{i}. {task}")




my_todo = TodoList()
my_todo.add_task("Python 공부")
my_todo.add_task("Git 연습")
my_todo.show_tasks()
# 출력:
# 1. Python 공부
# 2. Git 연습

my_todo.complete_task("Python 공부")
my_todo.show_tasks()
# 출력:
# 1. Git 연습



#문제 4: 실무 스타일 - dataclass 사용하기 
from dataclasses import dataclass

@dataclass
class DatabaseConfig:
    host:str
    port:int
    username:str
    password:str
    database:str
    timeout:int = 30
    pool_size:int = 5

config = DatabaseConfig(
    host="localhost",
    port=3306,
    username="admin",
    password="secret123",
    database="myapp"
)
print(config)

