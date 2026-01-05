# ===========================================
# 내가 보낸 요청의 Header 확인하기
# ===========================================

import requests

# 요청 보내기
response = requests.get(
    "https://httpbin.org/headers",
    headers={
        "Accept": "application/json",
        "Accept-Language": "ko-KR",
        "X-Requested-By": "jeff"
    }
)

# ========== 내가 보낸 요청 정보 확인 ==========
print("=" * 50)
print("📤 내가 보낸 요청 Header:")
print("=" * 50)

# response.request: 보낸 요청 객체에 접근
request = response.request

print(f"  Method: {request.method}")
print(f"  URL: {request.url}")
print(f"  Headers:")
for key, value in request.headers.items():
    print(f"    {key}: {value}")

# ========== 서버가 받은 Header 확인 ==========
# httpbin.org/headers는 서버가 받은 Header를 응답으로 반환
print("\n" + "=" * 50)
print("📥 서버가 실제로 받은 Header:")
print("=" * 50)

server_received = response.json()
for key, value in server_received['headers'].items():
    print(f"  {key}: {value}")