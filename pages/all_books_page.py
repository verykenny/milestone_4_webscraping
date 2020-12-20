import logging
import re

from bs4 import BeautifulSoup


from parsers.book import BookParser
from locators.all_books_page import AllBooksPageLocators

logger = logging.getLogger('scraping.all_books.page')

class AllBooksPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.info('Parsing books')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        content = self.soup.select_one(AllBooksPageLocators.PAGE_COUNT).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        return int(matcher.group(1))
