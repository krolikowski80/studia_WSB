# Importujemy potrzebne biblioteki
import requests
from bs4 import BeautifulSoup

# Funkcja pobierająca wszystkie linki (href) ze strony
def get_all_links(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    links = []
    for a in soup.find_all('a', href=True):
        links.append(a['href'])  # dodajemy atrybut href do listy
    return links

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Web_scraping'
    links = get_all_links(url)
    print("Znalezione linki:")
    for link in links[:10]:  # wyświetlamy tylko pierwsze 10
        print("-", link)
