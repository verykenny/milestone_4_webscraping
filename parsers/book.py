import re
import logging

from locators.book_locators import BookLocators


class BookParser:
    """
    A class to take in an HTML page or content, and find properties of an item
    in it.
    """

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Book: {self.name}, £{self.price} ({self.rating} stars)>'


    @property
    def name(self):
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs['title']
        logging.info('Book name has been pulled for ' + item_name)
        return item_name

    @property
    def link(self):
        locator = BookLocators.LINK_LOCATOR
        item_url = self.parent.select_one(locator).attrs['href']
        logging.info('Retrieving URL')
        return item_url

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        price = float(matcher.group(1))
        logging.info('Retrieving book price')
        return price

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_element = self.parent.select_one(locator)
        classes = star_rating_element.attrs['class']
        rating_classes = filter(lambda x: x != 'star-rating', classes)
        logging.info('Retrieving Rating')
        return self.RATINGS[next(rating_classes)]

