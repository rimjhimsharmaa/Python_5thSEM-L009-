""" 
wap that allows a librarian to add several books to a library.for each book ask the user to enter its title and no of copies.store each book and its 
avail copy in a dict.after each books have been added,display a menu that lets user issue a book,return a book,display all books or exit the program

conditions : -  books title should be compared w/o distinguish uppercase and lowercase letters.
   - a book can be issued only if exits in the library abd atleast 1 copy is avail.
   - issuing a book decreases its available copy count by 1.
   - a book can be returned only if it exits in the library and atleast 1 copy has been issued,
   - returning a book increases avail copy count by 1.
   - display an appropriate msg for an unavail book,an invalid choice,or an invalid no of copies.

"""

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, copies):
        key = title.lower()
        self.books[key] = [title, copies, copies]

    def issue_book(self, title):
        key = title.lower()

        if key not in self.books:
            print("Book not found.")
        elif self.books[key][1] == 0:
            print("No copies are available.")
        else:
            self.books[key][1] -= 1
            print("Book issued successfully.")

    def return_book(self, title):
        key = title.lower()

        if key not in self.books:
            print("Book not found.")
        elif self.books[key][1] == self.books[key][2]:
            print("No copy of this book is currently issued.")
        else:
            self.books[key][1] += 1
            print("Book returned successfully.")

    def display_books(self):
        print("\nLibrary Books:")

        for details in self.books.values():
            title = details[0]
            available_copies = details[1]
            print(title, "- Available copies:", available_copies)


library = Library()

number_of_books = int(input("How many different books do you want to add? "))

for i in range(number_of_books):
    title = input("Enter book title: ").strip()
    copies = int(input("Enter number of copies: "))
 