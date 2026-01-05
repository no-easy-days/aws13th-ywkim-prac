# 응답 형식에 따른 처리

# ===========================================
# Content-Type에 따라 응답 Body 처리하기
# ===========================================

import requests


def handle_response(response):
    """
    응답의 Content-Type을 확인하고 적절히 처리하는 함수

    Parameters:
        response: requests 라이브러리의 Response 객체

    Returns:
        처리된 응답 데이터
    """
    # Content-Type Header 가져오기
    content_type = response.headers.get('Content-Type', '')

    print(f"📋 Content-Type: {content_type}")

    # JSON 응답 처리
    if 'application/json' in content_type:
        print("   → JSON 형식으로 파싱합니다.")
        return response.json()  # 딕셔너리로 변환

    # HTML 응답 처리
    elif 'text/html' in content_type:
        print("   → HTML 텍스트로 처리합니다.")
        return response.text  # 문자열로 반환

    # 일반 텍스트 처리
    elif 'text/plain' in content_type:
        print("   → 일반 텍스트로 처리합니다.")
        return response.text

    # 바이너리 데이터 (이미지 등)
    else:
        print("   → 바이너리 데이터로 처리합니다.")
        return response.content  # bytes로 반환


# ========== 테스트 ==========
print("=" * 50)
print("🧪 다양한 응답 형식 테스트:")
print("=" * 50)

# JSON 응답
print("\n[테스트 1] JSON 응답:")
resp1 = requests.get("https://httpbin.org/json")
data1 = handle_response(resp1)
print(f"   결과 타입: {type(data1).__name__}")

# HTML 응답
print("\n[테스트 2] HTML 응답:")
resp2 = requests.get("https://httpbin.org/html")
data2 = handle_response(resp2)
print(f"   결과 타입: {type(data2).__name__}")
print(f"   첫 100자: {data2[:100]}...")