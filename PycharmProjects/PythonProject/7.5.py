# # [실습 7.1-1] 텍스트 파일 통계\
# def read_textfile(filename):
#     with open(filename,'r',encoding='utf-8') as f:
#         lines = f.readlines()
#
#     line_count = len(lines)
#     word_count = sum(len(line.strip()) for line in lines)
#     char_count = sum(len(line) for line in lines)
#     long_line = max(len(line) for line in lines) if lines else 0
#
#     print(f"전체 줄 수 : {line_count}")
#     print(f"전체 단어 수 : {word_count}")
#     print(f"전체 문자 수 : {char_count}")
#     print(f"가장 긴 줄의 길이 : {long_line}")\
# # [실습 7.1-2] 간단한 일기장
# from datetime import datetime
# import os
#
#
# class DiaryManager:
#     def __init__(self, folder='diary'):
#         self.folder = folder
#         os.makedirs(folder, exist_ok=True)
#
#     def write_diary(self, content, date=None):
#         if date is None:
#             date = [datetime.now](http: // datetime.now)().strftime('%Y-%m-%d')
#
#         filename = f"{self.folder}/diary_{date}.txt"
#         with open(filename, 'w', encoding='utf-8') as f:
#             f.write(content)
#         print(f"일기가 저장되었습니다: {filename}")
#
#     def read_diary(self, date):
#         filename = f"{self.folder}/diary_{date}.txt"
#         try:
#             with open(filename, 'r', encoding='utf-8') as f:
#                 return [f.read](http: // f.read)()
#         except FileNotFoundError:
#             return f"{date} 날짜의 일기가 없습니다."
#
#     def list_diaries(self):
#         files = [f for f in os.listdir(self.folder) if f.startswith('diary_')]
#         files.sort()
#         return files
#
# diary = DiaryManager()
# diary.write_diary("오늘 파일 입출력을 배웠다!")
# print([diary.read](http: // diary.read)_diary([datetime.now](http: // datetime.now)().strftime('%Y-%m-%d')))
# print("일기 목록:", diary.list_diaries())
#
# #