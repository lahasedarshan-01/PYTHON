class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))
        print("Book added")

    def lend_book(self, title):
        for b in self.books:
            if b.title == title and b.available:
                b.available = False
                print("Book issued")
                return
        print("Book not available")

    def return_book(self, title):
        for b in self.books:
            if b.title == title:
                b.available = True
                print("Book returned")
                return

    def display_books(self):
        for b in self.books:
            status = "Available" if b.available else "Issued"
            print(b.title, "-", status)


lib = Library()

while True:
    print("\n1. Add Book")
    print("2. Lend Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        title = input("Enter book name: ")
        lib.add_book(title)

    elif choice == 2:
        title = input("Enter book name: ")
        lib.lend_book(title)

    elif choice == 3:
        title = input("Enter book name: ")
        lib.return_book(title)

    elif choice == 4:
        lib.display_books()

    elif choice == 5:
        break

    else:
        print("Invalid choice")