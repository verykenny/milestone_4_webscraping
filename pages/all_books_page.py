import logging

from bs4 import BeautifulSoup


from parsers.book import BookParser
from locators.all_books_page import AllBooksPageLocators


class AllBooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logging.info('Parsing books')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]
