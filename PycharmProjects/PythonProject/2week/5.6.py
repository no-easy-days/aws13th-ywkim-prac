# 실습 1: 정렬하기
cities = [
    {"name": "서울", "population": 9700000},
    {"name": "부산", "population": 3400000},
    {"name": "인천", "population": 2900000},
    {"name": "대구", "population": 2400000}
]

# 인구수 오름차순 정렬
sorted_cities = sorted(cities, key=lambda x: x["population"], reverse=False)
print([sorted_cities["name"] for sorted_cities in sorted_cities])

# 결과: [대구, 인천, 부산, 서울]

# 실습 2: 데이터 변환
str_numbers = ["10", "20", "30", "40", "50"]

# 1단계: 정수로 변환
# 2단계: 100 더하기
# map(함수, iterable) : for문 반복문 없이 간겷하게 데이터반환할때 유용하다.
int_numbers = list(map(int, str_numbers))

result = list(map(lambda x: x + 100 , int_numbers))
print(result)

# 결과: [110, 120, 130, 140, 150]

# 실습 3: 필터링
products = [
    {"name": "노트북", "discount": 15},
    {"name": "마우스", "discount": 25},
    {"name": "키보드", "discount": 30},
    {"name": "모니터", "discount": 10}
]

# 할인율 20% 이상만 추출
discounted = list(filter(lambda x: x["discount"] > 20, products))
print(discounted)

# 결과: [{'name': '마우스', 'discount': 25}, {'name': '키보드', 'discount': 30}]