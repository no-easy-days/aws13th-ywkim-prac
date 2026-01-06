# 문제 1: CSV 읽기 (기본)
import csv

with open('users.csv', 'r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['이름']} - {row['직업']}")
# 문제 2: CSV 필터링
import csv

with open('users.csv', 'r',encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        age = int(row['나이'])
        if age >= 30:
            print(f"{row['이름']} ({age}세)")

# 문제 3: CSV 쓰기
import csv

students = [
    {'학번': 'S001', '이름': '김민수', '학과': '컴퓨터공학'},
    {'학번': 'S002', '이름': '이수진', '학과': '전자공학'},
    {'학번': 'S003', '이름': '박영호', '학과': '기계공학'},
]

with open('students.csv', 'w', encoding='utf-8', newline='') as f:
    filenames_2 = ['학번', '이름', '학과']
    writer = csv.DictWriter(f, fieldnames=filenames_2)

    writer.writeheader()
    writer.writerows(students)

# 문제 4: JSON 읽기 (기본)
import json

with open('config.json', 'r',encoding='utf-8') as f:
    config = json.load(f)

    print(f"앱 이름 : {config['app_name']}")
    print(f"버전 : {config['version']}")
    print(f"DB 호스트 : {config['database']['host']}")
# 문제 5: JSON 수정 및 저장
import json

with open('config.json', 'r',encoding='utf-8') as f:
    config = json.load(f)

config['debug'] = True
config['features'].append('notifications')

with open('config_updated.json', 'w',encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
# # 문제 6: CSV → JSON 변환
import csv
import json

def csv_to_dict(csv_file, json_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        data = list(csv.DictReader(f))

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 문제 7: 실무 시나리오 - 로그 분석
import json

with open('logs.json', 'r', encoding='utf-8') as f:
    logs = json.load(f)

errors = [log for log in logs if log['level'] == 'ERROR']

with open('errors.json', 'w', encoding='utf-8') as f:
    json.dump(errors, f, ensure_ascii=False, indent=2)

print(f"에러 {len(errors)}건을 errors.json에 저장했습니다.")