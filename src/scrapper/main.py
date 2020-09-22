from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import json
from .config import ENDPOINT


def main():
    print(total_schools())


def total_schools():
    def work():
        html = urlopen(ENDPOINT)
        bs = BeautifulSoup(html.read(), 'html.parser')

        number = bs.find('div', {'class': {'summary'}})
        total = number.find_all('b')

        schools = []
        for i, school in enumerate(bs.find_all('tr', {'class': 'w0'})):
            x = school.find_all('td', {'class': 'w0'})
            sc = {
                'id': i,
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
