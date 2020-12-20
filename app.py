import requests
import logging

from pages.all_books_page import AllBooksPage

page_content = requests.get("http://books.toscrape.com").content
page = AllBooksPage(page_content)
logging.info('Content pulled from target website and added to list')
books = page.books

i = 2

while i <= 50:
    page = str(i)
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    i += 1
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)

    logging.info('Content pulled from target website and added to list')
    books.extend(page.books)