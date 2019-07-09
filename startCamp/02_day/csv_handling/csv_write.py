dinner = {
    '양자강': '02-557-4211', 
    '김밥카페': '02-553-3181',
    '순남시래기': '02-508-0887'
}


# 1. String formatting 이용하는 법 (csv파일을 새롭게 만듦)
with open('dinner.csv', 'w', encoding = "utf-8") as f:
     # dict 가지고 list(for문도는)로 바꿔줌! ★★★
    for item in dinner.items():
        f.write(f'{item[0]},{item[1]}\n')


# 2. csv writer
import csv
with open('dinner.csv', 'w', encoding='utf-8', newline = '') as f: # option 으로 줄 때는 붙여서 하는게 convention
    csv_writer = csv.writer(f) # f라는 파일의 csv를 작성하는 객체를 생성
    for item in dinner.items():
        csv_writer.writerow(item)
