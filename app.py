import requests
import logging

from pages.all_books_page import AllBooksPage


logging.basicConfig(format='%(asctime)s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='example.log',
                    level=logging.DEBUG)

logger = logging.getLogger('scraping')

page_content = requests.get("http://books.toscrape.com").content
logger.info('Content pulled from target website.')
page = AllBooksPage(page_content)

books = page.books
logger.info('Content added to Books list')

i = 2

# while i <= 50:
# page = str(i)
# url = f"http://books.toscrape.com/catalogue/page-{page}.html"
# i += 1
# page_content = requests.get(url).content
# page = AllBooksPage(page_content)
#
# logging.info('Content pulled from target website and added to list')
# books.extend(page.books)


for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html'
    page_content = requests.get(url).content
    logger.info('Additional page of content pulled from target website.')
    page = AllBooksPage(page_content)
    books.extend(page.books)
    logger.info('Content added to books list.')
