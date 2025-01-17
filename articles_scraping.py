import requests
from bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org'


with open('lvl_paths.txt', 'r') as file:
    raw = file.readlines()


for line in raw:
    html = requests.get(URL + line.translate({ord('\n'): None})).text
    soup = BeautifulSoup(html, 'html.parser')

    lists = soup.find_all('div', attrs={'class': 'div-col'})
    
