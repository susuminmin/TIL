import requests
import bs4

url = 'https://finance.naver.com/sise/'

response = requests.get(url)

html = response.text

soup = bs4.BeautifulSoup(html, 'html.parser') 
kospi = soup.select_one('#KOSPI_now').text # select는 list형태 반환 (여러개 반환)
print(kospi)

# requests.get('http://naver.com ').status_code