# 1: 변수 선언
name = input("이름 입력: ")
age = input("나이  입력 : ")
num = input("숫자 입력 : ")
print(f"{name}과 {age}, {num}")
# 실습 2: 값 교환 (기초)
first = "A"
second = "B"

first,second = second,first
print(first)
print(second)
# 실습 3: 복합 연산 (기초)
balance = 10000
print((balance - 3000)* 2)
# 4: 오류 수정 (응용)
second_place = "은메달"
user_name = "홍길동"
my_class = "1학년"
# 실습 5: 자료형 확인하기 (기초)
print(type(42))
print(type(3.14))
print(type("Hello"))
print(type(True))
print(type(None))
# 실습 6: 형변환 연습 (기초)
num_1 = int(input())
num_2 = int(input())
print(num_1 + num_2)
# 실습 7: 자기소개 프로그램 (응용)
name = input("이름")
age = int(input("나이"))
height = int(input("키"))

print(f'이름 : {name} 나이 : {age} 키 : {height}입니다. 내년에는 {age+1}살 입니다.')
#실습 8: 계산기 만들기 (심화)
class Calculator:
    def __init__(self):
        pass
    def add(self, a, b):
        return a+b
    def sub(self, a, b):
        return a-b
    def mul(self, a, b):
        return a*b
    def div(self, a, b):
        return a / b

calculator = Calculator()
a = int(input("숫자를 입력하세요 : "))
b = int(input("두번째 숫자를 입력하세요 : "))

print(calculator.add(a,b))
