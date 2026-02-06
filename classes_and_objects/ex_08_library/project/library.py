from project.user import User

class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {}
        self.rented_books: dict[str, dict[str, int]] = {}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        # book_available = next((True for author, books in self.books_available.items() if book_name in books ), None)
        # self.books_available[author].remove(book_name) for author, books in self.books_available

        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books.keys():
                self.rented_books[user.username] = {book_name: 0}
            self.rented_books[user.username][book_name] = days_to_return
            user.books.append(book_name)
        else:
            days = self.rented_books[user.username][book_name]
            return f'The book "{book_name}" is already rented and will be available in {days} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str|None:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        else:
            return f"{user.username} doesn't have this book in his/her records!"


