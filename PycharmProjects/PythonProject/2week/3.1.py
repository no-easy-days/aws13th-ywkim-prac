# 실습 3-1: 이메일 주소 분리하기
email = input("이메일 입력 : ")
part = email.split("@")
print("사용자 이름 : ", part[0])
print("도메인 : ", part[1])
# 실습 3-2: 비밀번호 길이 검사
password = input("비밀번호를 입력하세요 : ")
if len(password) >= 8:
    print("✅ 유효한 비밀번호입니다.")
# 실습 3-3: 3의 배수 찾기
multipes_of_3 = [x for x in range(1, 21) if x % 3 == 0]
print(multipes_of_3)
# 습 3-4: 공통 관심사 찾기
chulsoo = ["축구", "영화", "음악", "게임", "독서"]
younghee = ["영화", "음악", "요리", "여행", "독서"]

set1 = set(chulsoo)
set2 = set(younghee)
result = set1.intersection(set2)
print(list(result))
# 실습 3-5: 최고 점수 학생 찾기
scores = {
    "철수": 85,
    "영희": 92,
    "민수": 78,
    "지수": 95,
    "현우": 88
}
max = 0
for k, v in scores.items():     # k : 이름 , v : 점수
    if v > max:
        max = v
        name = k

print(f"최고점을 받은 사람 {name} : {max}")
