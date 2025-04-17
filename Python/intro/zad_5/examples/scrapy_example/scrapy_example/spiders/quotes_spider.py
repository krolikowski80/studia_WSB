import scrapy

# Definicja klasy spidera dziedzicząca po scrapy.Spider
class QuotesSpider(scrapy.Spider):
    # Nazwa spidera – używana do uruchamiania
    name = "quotes"

    # Lista początkowych adresów URL
    start_urls = ['http://quotes.toscrape.com/page/1/']

    # Główna metoda przetwarzająca odpowiedź HTTP
    def parse(self, response):
        # Iterujemy po każdym cytacie na stronie
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        # Szukamy linku do kolejnej strony
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            # Rekurencyjnie wykonujemy crawl na kolejnej stronie
            yield response.follow(next_page, self.parse)
