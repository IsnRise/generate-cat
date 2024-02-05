import random
import requests
from bs4 import BeautifulSoup
from PIL import Image
from urllib.request import urlopen


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
url = 'https://ru.freepik.com/photos/милые-котики'
result = requests.get(url, headers=headers)


def main():
    if result.status_code == 200:
        soup = BeautifulSoup(result.text, 'html.parser')
        links = []
        all_images = soup.find_all('figure', class_="showcase__item js-detail-data caption showcase__item--with-tags showcase__item--buttons")

        for item in all_images:
            link = item.find('div', class_='showcase__content tags-links active-tags-tablet-mobile').find('a', class_='showcase__link js-detail-data-link').find('img').find('img')
            if link:
                links.append(link.get('src'))

        image = Image.open(urlopen(random.choice(links)))
        image.show()


def menu():
    print('\n 1. Создать котика \n 2. Выйти=нельзя')
    answer = input('\nЧто хочешь сделать?\n')
    match answer:
        case '1':
            main()
        case '2':
            exit()


if __name__ == '__main__':
    while True:
        menu()
