books_shelf = input().split("&")

command = input().split(" | ")

while command[0] != "Done":
    action = command[0]
    if action =="Add Book":
        book = command[1]
        if book not in books_shelf:
            books_shelf.insert(0, book)
    elif action == "Take Book":
        book = command[1]
        if book in books_shelf:
            book_index = books_shelf.index(book)
            books_shelf.pop(book_index)
    elif action == "Swap Books":
        book01 = command[1]
        book02 = command[2]
        if book01 in books_shelf and book02 in books_shelf:
            book01_index = books_shelf.index(book01)
            book02_index = books_shelf.index(book02)
            books_shelf[book01_index], books_shelf[book02_index] = books_shelf[book02_index], books_shelf[book01_index]
    elif action == "Insert Book":
        book = command[1]
        if book not in books_shelf:
            books_shelf.append(book)
    elif action == "Check Book":
        index = int(command[1])
        if index in range(len(books_shelf)):
            print(books_shelf[index])

    command =input().split(" | ")

print(", ".join(books_shelf))