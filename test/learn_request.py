import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
res = requests.get("https://www.baidu.com", stream=True)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())
doc = pq(soup.prettify())
x= doc.find('.mnav').items()
for i in x:
    print(i.attr('href'), i.text())
    file = open('restful.test.txt', 'a', encoding='utf-8')
    file.write('\n'+i.attr('href') + i.text())
    file.close()

