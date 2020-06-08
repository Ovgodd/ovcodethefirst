#class > library
#layers of abstractions > display available books, to lend a book, to ad a book

#class > customer
#layers of abstractions > request for a book, return a book
class Library:

    def __init__(self,listOfBooks):
        self.availableBooks = listOfBooks


    def displayAvailableBooks(self):
        print()
        print("Available Books : ")
        for book in self.availableBooks:
            print(book)

    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry the book is not available in our list.")

    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("You have return the book. Thank You")

class Customer:
    def requestedBook(self):
        print("Enter the bame of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnedBook(self):
        print("enter the name of the book which you are returning ")
        self.book = input()
        return self.book

library = Library(['Think and Grow Rich','Who will Cry When You Die','For One More Day'])
customer = Customer()

while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestBook = customer.requestedBook()
        library.lendBook(requestBook)
    elif userChoice is 3:
        returnBook = customer.returnedBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()