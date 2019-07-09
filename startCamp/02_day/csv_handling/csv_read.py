# 1. split 함수
with open('dinner.csv', 'r', encoding = "utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip().split(',')) # print도 개행 문자 붙는다~  / # , 기준으로 문자열을 split한다.

# 2. csv_reader 사용
import csv
with open('dinner.csv', 'r', encoding = 'utf-8') as f:
    items = csv.reader(f)
    for item in items:
        print(item)