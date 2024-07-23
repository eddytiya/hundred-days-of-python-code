#day67 library management system
'''
Write a Library class with no_of_books and books as two instance variables. 
Write a program to create a library from this Library class and show how you 
can print all books, add a book and get the number of books using different methods.
 Show that your program doesnt persist the books after the program is stopped!
'''
class library:
    def __init__(self):
        self.no_of_books=0
        self.books=[]

    def addBook(self,book):
        self.books.append(book)
        self.no_of_books=len(self.books)

    def showInfo(self):
        print(f"the library has {self.no_of_books} books.the books are")
        for book in self.books:
            print(book)
    


l1=library()
l1.addBook("harry potter")
l1.addBook("germinico stilton")
l1.addBook("the diary of a wimpy kid")
l1.showInfo()


