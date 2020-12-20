from app import books

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


# print_best_books()
# print_cheapest_books()
print_best_by_price_books()