# --------------------- UNDER DEVELOPMENT --------------------------

import requests
from bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org'


with open('lvl_paths.txt', 'r') as file:
    paths = file.readlines()

hrefs = []
for line in paths:
    html = requests.get(URL + line.translate({ord('\n'): None})).text
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', attrs={'class': 'div-col'})
    for div in divs:
        lists = div.find_all('ol')
        for ol in lists:
            for child in ol.children:
                contents = child.find_all(['a', 'b'])
                for item in contents:
                    if item.has_attr('class'):
                        contents.remove(item)
                for item in contents:
                     hrefs.append(item.href)


    
