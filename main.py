class Book:

    def __init__(self, title: str, author: str, price: float, quantity: int) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def apply_discount(self, discount_percentage: float) -> float or str:
        if discount_percentage > 100 or discount_percentage < 0:
            return "There is a wrong value of percentage"
        self.price = self.price * (1 - (discount_percentage / 100))
        return round(self.price, 2)

    def sell(self, amount: int) -> str or None:
        if amount < self.quantity:
            return "There are no such amount of books in the storage"
        else:
            self.quantity -= amount

    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Price: ${round(self.price, 2)}, Quantity: {self.quantity}"

class BookStore:

    def __init__(self, books: list[Book]) -> None:
        self.books = books

    def add_book(self, book: Book):
        self.books.append(book)

    def search(self, query: str) -> Book or str:
        for book in self.books:
            if book.title == query:
                return book
            else:
                return "There are no such books in the storage"

    def calculate_total_value(self) -> float:
        total_value = 0
        for book in self.books:
            total_value += book.price * book.quantity
        return total_value
