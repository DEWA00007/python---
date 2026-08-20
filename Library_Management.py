class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
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

        found = False

        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                status = "Available" if book.available else "Borrowed"

                print(f"\nID: {book.book_id}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Status: {status}")

                found = True

        if not found:
            print("Book not found.")

    def borrow_book(self):
        book_id = input("Enter book ID to borrow: ")

        for book in self.books:
            if book.book_id == book_id:

                if book.available:
                    book.available = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed.")

                return

        print("Book not found.")

    def return_book(self):
        book_id = input("Enter book ID to return: ")

        for book in self.books:
            if book.book_id == book_id:

                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book was not borrowed.")

                return

        print("Book not found.")


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.display_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.borrow_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
