# Importujemy biblioteki
import requests
from bs4 import BeautifulSoup

# Funkcja pobierająca wszystkie nagłówki <h2> ze strony
def get_headings(url: str):
    # Pobranie treści HTML ze strony
    r = requests.get(url)
    # Parsowanie HTML za pomocą BeautifulSoup
    soup = BeautifulSoup(r.text, 'lxml')
    # Zwracamy listę tekstów z tagów <h2>
    return [h2.get_text(strip=True) for h2 in soup.find_all('h2')]

# Uruchamiamy funkcję, jeśli plik uruchamiany bezpośrednio
if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Web_scraping'
    headings = get_headings(url)
    print('Nagłówki H2 na stronie:')
    for h in headings:
        print('–', h)
