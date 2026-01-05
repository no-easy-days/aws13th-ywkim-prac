# ===========================================
# HTTP POST 요청 보내기
# POST: 서버에 데이터를 "보내는" 요청
# ===========================================

import requests
import json

# ========== 보낼 데이터 준비 (Body에 담길 내용) ==========
user_data = {
    "name": "ywkim",           # 사용자 이름
    "email": "jeff@example.com",  # 이메일
    "role": "instructor"      # 역할
}

# ========== 요청 Header 설정 ==========
# Content-Type: 보내는 데이터의 형식을 서버에 알려줌
headers = {
    "Content-Type": "application/json",  # JSON 형식으로 보낸다고 명시
    "Authorization": "Bearer my_token_123",  # 인증 토큰 (예시)
    "X-Custom-Header": "youngwon"  # 사용자 정의 Header (X-로 시작)
}

print("=" * 50)
print("📤 보내는 요청 정보:")
print("=" * 50)
print(f"  URL: https://httpbin.org/post")
print(f"  Method: POST")
print(f"  Headers: {json.dumps(headers, indent=4, ensure_ascii=False)}")
print(f"  Body: {json.dumps(user_data, indent=4, ensure_ascii=False)}")

# ========== POST 요청 보내기 ==========
response = requests.post(
    "https://httpbin.org/post",  # 요청 URL
    headers=headers,              # 요청 Header
    json=user_data                # 요청 Body (자동으로 JSON 변환)
)

# ========== 응답 확인 ==========
print("\n" + "=" * 50)
print("📥 받은 응답 정보:")
print("=" * 50)
print(f"  상태 코드: {response.status_code}")

# httpbin.org는 받은 요청 정보를 그대로 응답으로 돌려줌
response_data = response.json()
print(f"\n  서버가 받은 Header:")
for key, value in response_data['headers'].items():
    print(f"    {key}: {value}")

print(f"\n  서버가 받은 Body (JSON):")
print(f"{response_data['json']}")