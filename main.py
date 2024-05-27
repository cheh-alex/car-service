from car import Car
import requests
from bs4 import BeautifulSoup
import database
import time
from parsers.autoscout import get_page_listings
from logger import logger


def update_listings():
    logger.info('start updating listings')
    listings = []
    for i in range(1, 5):
        logger.info(f'processing page {i}')
        try:
            result = get_page_listings(i)
            for car in result:
                if not database.check_car_exists(car):
                    database.insert_car(car)

                    logger.info(f'{car.uid}, {car.make}, {car.link}')

                    listings.append(car)

        except Exception as ex:
            logger.error(ex)

    logger.info('finish updating listings')


while True:
    update_listings()
    time.sleep(10)
