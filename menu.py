from app import books
import logging


logging.basicConfig(filename='menu.log', level=logging.DEBUG)

USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the catalogue
- 'q' to exit

Enter your choice: '''

def menu():
    user_input = input(USER_CHOICE).lower()
    while user_input != 'q':
        try:
            logging.info('User input: ' + user_input)
            menu_options[user_input]()
        except:
            logging.error('User entered invalid command: ' + user_input)
            print("Please choose a valid command.")

        user_input = input(USER_CHOICE).lower()


'''
sort by one thing
'''


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


'''
sort by multiple things by doing a tuple
if it finds more than one thing with the same value, it will begin to sort by the next item in the tuple
'''


def print_best_by_price_books():
    best_by_price = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_by_price:
        print(book)


# def next_book_gen():
#     global i
#     while i < 100:
#         yield i
#         i += 1


# def next_book():
#     print(books[next(g)])

books_gen = (x for x in books)


def next_book():
    print(next(books_gen))


menu_options = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': next_book,
}

# g = next_book_gen()

menu()
