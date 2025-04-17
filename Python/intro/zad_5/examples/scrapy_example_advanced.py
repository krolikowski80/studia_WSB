# Programowe uruchomienie spidera Scrapy z poziomu skryptu
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_example.spiders.quotes_spider import QuotesSpider

# Tworzymy obiekt procesora Scrapy z domyślnymi ustawieniami
process = CrawlerProcess(get_project_settings())

# Dodajemy naszego spidera do kolejki zadań
process.crawl(QuotesSpider)

# Uruchamiamy crawl (blokująco)
process.start()
