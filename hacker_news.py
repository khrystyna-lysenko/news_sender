from cgitb import html
from bs4 import BeautifulSoup
import requests


html_doc = requests.get('https://news.ycombinator.com/')


soup = BeautifulSoup(html_doc.content, 'html.parser')


article_list = soup.find_all('tr.athing')

for a in article_list:

    print(a.text)
# print(soup.prettify())

# news_list = []

# for n in range(1, 50):
#     news_list.append(soup.div['article_header'].get_text())

# print(news_list)

# print(soup.find_all("div.article_header").text())