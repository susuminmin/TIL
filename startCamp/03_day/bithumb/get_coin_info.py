import requests
import bs4
import csv

# step1. Bithumb 페이지를 가지고 온다. 
url = 'https://www.bithumb.com/'

# selector = ' tr > td > span'

response = requests.get(url) # 요청을 보내 응답을 받는다.  # response먼저 해보고 200을 보면 맞다는 소리임 ㅎㅎ 
html = response.text # 응답 받은 객체에서 html문서를 str으로 가지고 옴. 
# print(html) # 끝이 </html>로 끝나주면 ㅇㅋ # 타입은 str


# step2. BeautifulSoup 모듈을 이용하여 str type의 html을 파싱한다. 
soup = bs4.BeautifulSoup(html, 'html.parser') # html으로 접근이 가능하도록 해 줌 ㅎㅅㅎ


# step3. 각 코인의 정보가 담겨 있는 table row 데이터를 list 의 형태로 가져온다. 
coins = soup.select('.coin_list > tr') # 프린트하면 대괄호! 리스트라는 뜻임


# step4. 각 코인을 순회하며 필요한 정보만 추출한다. 
for coin in coins:
    coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.strip()
    coin_name = coin_name.replace('NEW', '')
    coin_price = coin.select_one('td:nth-child(2) > strong').text
    data = (coin_name, coin_price)
    print(data)

# step5. csv_writer를 이용해서 정보를 저장한다. 
with open('coin_info.csv', 'w', encoding = "utf-8", newline='') as f:
    csv_writer = csv.writer(f)
    for coin in coins:
        coin_name = coin.select_one('td:nth-child(1) > p > a > strong').text.strip()
        coin_name = coin_name.replace('NEW', '')
        coin_price = coin.select_one('td:nth-child(2) > strong').text
        data = (coin_name, coin_price)
        csv_writer.writerow(data)