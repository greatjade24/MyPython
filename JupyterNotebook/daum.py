import requests
from bs4 import BeautifulSoup

resp = requests.get('http://www.daum.net')

html = resp.text

soup = BeautifulSoup(html, 'html.parser')

result = soup.select('.list_favorsch a')

for item in result:
    print(item.text)

