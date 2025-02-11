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
    divs = soup.find_all('div', attrs={'class': 'div-col', 'style': 'column-width: 15em;'})
    for div in divs:
        lists = div.find_all('ol')
        for ol in lists:
            for child in ol.find_all('li'):
                if not child.find_all('b') and not child.find_all('i'):
                    contents = child.find_all('a')
                    for item in contents:
                        if not item.has_attr('class'):
                            # if item['href'] not in hrefs:
                            #     hrefs.append(item['href'])
                            hrefs.append(item['href'])
                elif not child.find_all('i'):
                    contents = child.find_all('b')
                    for item in contents:
                        # if not item.has_attr('class'):
                        #     hrefs.append(item.a['href'])
                        # if item.a['href'] not in hrefs:
                        #     hrefs.append(item.a['href'])
                        hrefs.append(item.a['href'])
                else:
                    contents = child.find_all('i')
                    for item in contents:
                        # if not item.has_attr('class'):
                        #     hrefs.append(item['href'])
                        for b in item.find_all('b'):
                            hrefs.append(item.a['href'])

hrefs = list(dict.fromkeys(hrefs))  # removing duplicates from the hrefs
print(len(hrefs))

with open('articles_paths.txt', 'w') as file:
    for item in hrefs:
        file.write(f"{item}\n")
