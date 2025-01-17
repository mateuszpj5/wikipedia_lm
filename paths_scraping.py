import requests
from bs4 import BeautifulSoup
URL = 'https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/5/'


html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')


paths = []
table = soup.find('table', attrs={'class':'wikitable sortable'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    href = []
    for item in cols:
        try:
            href.append(item.a['href'])
        except TypeError:
            pass
    for path in href:
        paths.append(path)


with open('lvl_paths.txt', 'w') as file:
    for path in paths:
        file.write(f"{path}\n")