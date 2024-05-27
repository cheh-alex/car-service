import requests
from bs4 import BeautifulSoup
from car import Car


def get_page_listings(page):
    URL = f'https://www.autoscout24.fr/lst?atype=C&cy=F&damaged_listing=exclude&desc=1&page={page}&powertype=kw&search_id=zdjw1fw7no&sort=age&source=listpage_pagination&ustate=N%2CU'

    responce = requests.get(URL)
    page = BeautifulSoup(responce.text, 'html.parser')
    articles = page.find_all('article', {'class': 'cldt-summary-full-item'})
    listings = []
    for article in articles:
        uid = article.get('id')
        make = article.get('data-make')
        model = article.get('data-model')
        price = article.get('data-price')
        mileage = article.get('data-mileage')
        # photo = article.find('source').get('srcset')
        photo = None
        link = 'https://www.autoscout24.fr' + article.find('a', {'class': 'ListItem_title__ndA4s'}).get('href')

        car = Car(uid, make, model, price, mileage, link, photo)
        listings.append(car)
    return listings
