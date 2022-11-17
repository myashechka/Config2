import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    file = open('f.txt')
    for i in file.readlines():
        page = requests.get(i)
        soup = BeautifulSoup(page.text, "html.parser")
        result = (soup.findAll('div', {'class': 'design'}))
        print(result)


