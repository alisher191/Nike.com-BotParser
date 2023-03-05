import requests
from bs4 import BeautifulSoup
import lxml

import config


HOST = 'https://https://www.nike.com/'
URL = 'https://www.nike.com/w/jordan-1-aj85g'

HEADERS = config.HEADERS

def get_html(URL, HEADERS, params=''):
    response = requests.get(url=URL, headers=HEADERS, params=params)
    return response


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='product-card product-grid__card css-c2ovjx')
    
    jordans = []
    
    for item in items:
        jordans.append(
            {
                'title': item.find('div', class_='product-card__body').find('a').get_text(),
                'link': item.find('div', class_='product-card__body').find('a').get('href'),
                'category': item.find('div', class_='product-card__body').find('div', class_='product-card__subtitle').get_text(),
                'price': item.find('div', class_='product-card__body').find('div', class_='product-price us__styling is--current-price css-11s12ax').get_text(),
                # 'img': item.find('div', class_='product-card__body').find('div', class_='wall-image-loader').find('img').get('src')
            }
        )
    return jordans


html = get_html(URL=URL, HEADERS=HEADERS)
content = get_content(html=html.text)


# with open('content.txt', 'w') as file:
#     file.write(str(content))

def prs(content):
    items = []
    for ind, item in enumerate(content):
        items.append(f'''Товар № {ind + 1}\nНазвание: {item['title']}\nСсылка на товар: {item['link']}\nКатегория: {item['category']}\nЦена: {item['price']}\n----------------\n''')
    return items


shoes = prs(content)
