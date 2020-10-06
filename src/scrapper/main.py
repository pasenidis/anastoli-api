from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json
from .config import ENDPOINT, ROUNDS


def main():
    print(total_schools())


def total_schools():
    def work():
        schools = []
        c = 0
        
        for i in range(ROUNDS):
            html = urlopen(f'{ENDPOINT}/index.php?page={i + 1}&per-page=100')
            bs = BeautifulSoup(html.read(), 'html.parser')

            number = bs.find('div', {'class': {'summary'}})
            total = number.find_all('b')

            for i, school in enumerate(bs.find_all('tr', {'class': 'w0'})):
                x = school.find_all('td', {'class': 'w0'})
                c += 1
                sc = {
                    'id': c,
                    'name': x[0].text,
                    'region': x[1].text,
                    'address': x[2].text,
                    'closed_until': x[3].text,
                    'comments': x[4].text
                }
                schools.append(sc)

        return (int(total[1].text), schools)

    return work()


if __name__ == "__main__":
    main()
