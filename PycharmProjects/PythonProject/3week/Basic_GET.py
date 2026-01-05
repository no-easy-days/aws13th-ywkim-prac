# ===========================================
# HTTP GET 요청 보내기
# GET: 서버에서 데이터를 "가져오는" 요청
# ===========================================

import requests  # HTTP 요청을 위한 라이브러리 불러오기

# 테스트용 API 서버에 GET 요청 보내기
# httpbin.org: HTTP 요청을 테스트할 수 있는 무료 서비스
response = requests.get("https://httpbin.org/get")

# ========== 응답 상태 확인 ==========
print("=" * 50)
print("📊 응답 상태 코드:", response.status_code)
# 200: 성공, 404: 찾을 수 없음, 500: 서버 오류

print("📊 응답 상태 메시지:", response.reason)
# OK, Not Found, Internal Server Error 등

# ========== 응답 Header 확인 ==========
print("\n" + "=" * 50)
print("📨 응답 Header (서버가 보낸 메타데이터):")
print("=" * 50)

# response.headers: 딕셔너리 형태의 Header 정보
for header_name, header_value in response.headers.items():
    print(f"  {header_name}: {header_value}")

# ========== 응답 Body 확인 ==========
print("\n" + "=" * 50)
print("📦 응답 Body (서버가 보낸 실제 데이터):")
print("=" * 50)

# response.text: Body를 문자열로 반환
print(response.text)

# response.json(): Body를 JSON(딕셔너리)으로 파싱
# JSON 형식일 때만 사용 가능
data = response.json()
print("\n📦 JSON으로 파싱한 결과:")
print(f"  요청한 URL: {data['url']}")