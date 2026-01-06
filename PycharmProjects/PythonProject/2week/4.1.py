# 실습 4-1: 등급 판정

try:
    score = int(input("점수를 입력하세요: "))
    if not 0 <= score <= 100:
        raise ValueError("점수는 0~100 사이여야 합니다.")
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(grade)
except ValueError:
    print("잘못된 입력입니다.")


#  실습 4-2: 구구단 출력
dan = int(input("입력 :"))

print(f'==={dan}단===')
for i in range(1, 10):
    print(dan, 'x', i, '=', dan * i)

#  실습 4-3: 소수 판별 (도전!)

for i in range(2, 100):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
print()
# 실습 4-4: 숫자 맞추기 게임 (도전!)
import random

answer = random.randint(1, 100)
count = 0
while True:
    num = int(input("숫자를 입력하세요 : "))
    count += 1
    if num > answer:
        print("더 작은 수를 입력하세요")
    elif num < answer:
        print("더 큰수를 입력하세요")
    else:
        print(f"정답입니다! {count}번 만에 맞추셨습니다!")
        break
