class Book:
    def __init__(self,book_id,title,author):
        self.book_id = book_id
        self.title = title
        self.aurthor=author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter book ID: ")
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(book_id, title, author)
        self.books.append(book)

        print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\n--- Library Books ---")

        for book in self.books:
            status = "Available" if book.available else "Borrowed"

            print(f"ID: {book.book_id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Status: {status}")
            print("--------------------")

    def search_book(self):
        keyword = input("Enter book title or author: ").lower()
     
    


        


