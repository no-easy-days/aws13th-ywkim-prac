# ===========================================
# Form 데이터로 POST 요청 보내기
# 웹 브라우저의 로그인 폼과 동일한 방식
# ===========================================

import requests

# ========== 폼 데이터 준비 ==========
# 일반적인 로그인 폼에서 전송되는 데이터 형식
login_data = {
    "username": "jeff",
    "password": "secure_password_123"
}

# ========== Form 형식으로 POST 요청 ==========
# data= 파라미터 사용 시 자동으로
# Content-Type: application/x-www-form-urlencoded 설정됨
response = requests.post(
    "https://httpbin.org/post",
    data=login_data  # json= 대신 data= 사용
)

print("=" * 50)
print("📋 Form 데이터 전송 결과:")
print("=" * 50)

result = response.json()
print(f"Content-Type: {result['headers']['Content-Type']}")
print(f"전송된 Form 데이터: {result['form']}")