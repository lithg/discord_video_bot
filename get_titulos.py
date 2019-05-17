from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


req = Request('https://www.youtube.com/results?search_query=python', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page, 'html.parser')
soup.prettify()

lista = []

for link in soup.find_all('a'):
    if link.get('title') != None:
        lista.append(link.get('title'))
del lista[:41]


for i in range(10):
    print(lista[i])
