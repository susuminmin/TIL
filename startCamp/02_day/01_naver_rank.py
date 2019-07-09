# # 네이버 페이지에 요청 보내기

import requests
import bs4

url = 'http://www.naver.com/'

selector = '.ah_k'

html = requests.get(url).text
soup = bs4.BeautifulSoup(html, 'html.parser')

ranks = soup.select(selector)
print(ranks)

for rank in ranks:
    print(rank.text)
# # 원하는 정보는 급상승 검색어... 우클릭 요소검사 탭 

# # selector 만들기 / 코스피 나우 부분
# # '.ah_l .ah_item .ah_a .ah_k ' 
