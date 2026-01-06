# 실습 10.1-1] 위험한 코드 찾기
# f-스트링을 사용해서
# f-스트링을 사용하면 인증우회나 테이블 삭제 다른 테이블 탈취 같은 유형에 공격을 당할 수 있기 때문이다.
# [실습 10.1-2] 안전한 코드로 수정하기
name = input("이름: ")
age = input("나이: ")

sql = "INSERT INTO students VALUES (%s,%s)"
cursor.execute(sql, (name, age))
# 이름 기반 %(key)s)


name = input("이름: ")
age = input("나이: ")

sql = "INSERT INTO students VALUES (%(name)s, %(age)s)"
cursor.execute(sql, {"name" : name, "age" : age})

# [실습 10.1-3] 공격 시나리오 분석
# ' OR '1'='1