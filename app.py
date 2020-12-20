import requests
import logging

from pages.all_books_page import AllBooksPage

page_content = requests.get("http://books.toscrape.com/").content
logging.info('Content pulled from target website')
page = AllBooksPage(page_content)

books = page.books

# for book in books:
#     print(book)
