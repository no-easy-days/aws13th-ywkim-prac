# 특정 Header 값 추출하기

# ===========================================
# 응답 Header에서 특정 값 추출하기
# ===========================================

import requests

response = requests.get("https://httpbin.org/get")

# ========== 개별 Header 값 접근 ==========
print("=" * 50)
print("📌 주요 응답 Header 값:")
print("=" * 50)

# 방법 1: 딕셔너리처럼 접근 (없으면 KeyError 발생)
try:
    content_type = response.headers['Content-Type']
    print(f"  Content-Type: {content_type}")
except KeyError:
    print("  Content-Type: 없음")

# 방법 2: get() 메서드 사용 (없으면 기본값 반환, 권장)
content_length = response.headers.get('Content-Length', '알 수 없음')
print(f"  Content-Length: {content_length}")

server = response.headers.get('Server', '알 수 없음')
print(f"  Server: {server}")

date = response.headers.get('Date', '알 수 없음')
print(f"  Date: {date}")

# 존재하지 않는 Header
custom = response.headers.get('X-Custom-Header', '존재하지 않음')
print(f"  X-Custom-Header: {custom}")