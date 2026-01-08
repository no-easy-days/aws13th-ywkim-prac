#  실습 5-1: 계산기 함수
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        return a / b
    else:
        raise ValueError("지원하지 않는 연산자 입니다.")


tests = [
    (10, 5, '+'),
    (10, 5, '-'),
    (10, 5, '*'),
    (10, 5, '/'),
    (10, 0, '/'),
    (10, 5, '%')
]

for a, b, op in tests:
    try:
        print(calculator(a, b, op))
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)


# 실습 5-2: 학생 성적 처리
def print_report(name, scores):
    print(f"==={name} 성적표 ===")
    print(f"점수 : {scores}")
    average = sum(scores) / len(scores)
    print(f"평균 : {average}점")
    print(f"최고점 : {max(scores)}점")
    print(f"최저점 : {min(scores)}점")
    if average >= 90:
        print(f"등급 : A")
    elif average >= 80:
        print(f"등급 : B")
    elif average >= 70:
        print(f"등급 : C")
    elif average >= 60:
        print(f"등급 : D")
    else:
        print(f"등급 : F")
    pass


print_report("김철수", [85, 92, 78, 96, 88])


# 예상 출력:
# === 김철수 성적표 ===
# 점수: [85, 92, 78, 96, 88]
# 평균: 87.8점
# 최고점: 96점
# 최저점: 78점
# 등급: B

# 실습 5-3: 비밀번호 검증
def validate_password(password):
    # 여기에 코드 작성
    # 유효하면 True, 아니면 False와 이유 반환
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if password.islower():
        return False
    return True


print(validate_password("abc"))  # (False, "8자 이상이어야 합니다")
print(validate_password("abcdefgh"))  # (False, "숫자를 포함해야 합니다")
print(validate_password("abcdefg1"))  # (False, "대문자를 포함해야 합니다")
print(validate_password("Abcdefg1"))  # (True, "유효한 비밀번호입니다")
