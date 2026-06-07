borrowed_books = []
class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print("Books present in this library are:")
        for book in self.books:
            print(f" - {book}")

class Student(Library):
    def BorrowBook(self, BookName):
        if BookName in self.books:
            print(f"You have borrowed \"{BookName}\" ")
            self.books.remove(BookName)
            self.borrowed_books = borrowed_books
            self.borrowed_books.append(BookName)
        else:
            print("This book is not present in the library.")
    
    def returnBook(self, BookName):
        if BookName in borrowed_books:
            self.books.append(BookName)
            print(f"You have returned \"{BookName}\" to the library")
        else:
            print("You have not borrowed this book.")
    
    def AddBook(self, BookName):
        self.books.append(BookName)
        print(f"You have added \"{BookName}\" to the library.")
    
    def RemoveBook(self, BookName):
        if BookName in self.books:
            self.books.remove(BookName)
            print(f"You have removed \"{BookName}\" from the library.")
        else:
            print("That book is not present in the library.")

if __name__ == "__main__":
    a = Student(["Python for Beginners", "To Kill a Mockingbird", "The Art of War","The Great Gatsby",
                 "Rework", "The Alchemist", "The Fault in Our Stars", "Introduction to Algorithms",
                 "Freakonomics"])
    while(True):
        print(f'''\t=======CENTRAL LIBRARY SYSTEM=======\t
              Please choose an option:
              1. List all availible books
              2. Borrow a book  
              3. Return a book
              4. Add a book
              5. Remove a book
              6. Exit the library''')
        try:
            choice = int(input("Enter a choice: "))
            if choice == 1:
                print("\n")
                a.displayAvailableBooks()
                input("")
            elif choice == 2:
                print("\n")
                a.displayAvailableBooks()
                BorrowChoice = input("Which book would you like to borrow: ")
                a.BorrowBook(BorrowChoice)
            elif choice == 3:
                print("\n")
                ReturnChoice = input("Which book would you like to return: ")
                a.returnBook(ReturnChoice)
            elif choice == 4:
                print("\n")
                AddChoice = input("Enter the name of the book which you would like to add: ")
                a.AddBook(AddChoice)
            elif choice == 5:
                print("\n")
                RemoveChoice = input("Enter the name of the book you would like to remove: ")
                a.RemoveBook(RemoveChoice)
            elif choice == 6:
                print("\n")
                print("Thank you for using the Central Library System!")
                input("Press Enter to exit...")
                break
            else:
                print("\n")
                print("Invalid choice!")
        except Exception as e:
            print("Invalid choice!")
