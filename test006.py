class Book:
    def __init__(self, name, age, pages):
        self.name = name
        self.age = age
        self.pages = pages

book = Book("My book", 23, 234)
print(book.name)
print(book.age)
print(book.pages)
