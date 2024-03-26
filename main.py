import requests
from bs4 import BeautifulSoup


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
        data = {
            'id': uid,
            'make': make,
            'model': model,
            'price': price,
            'mileage': mileage
        }
        listings.append(data)
    return listings
for i in range(1,21):
    result = get_page_listings(i)
    print(result)