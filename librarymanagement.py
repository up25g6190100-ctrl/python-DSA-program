class Book:
    def __init__(self,book_id,title):
        self.book_id = book_id
        self.title = title
        self.available = True  
class Member:
    def __init__(self,member_id,name):
        self.member_id = member_id
        self.name = name
class Library:
    def __init__(self):
        self.books = []
        self.members = [] 
    def add_book(self,book):
        self.books.append(book)
        print(f"Book '{book.title}' added .")
    def add_member(self,member):
        self.members.append(member)
        print(f"Member '{member.name}' registered .")
    def register_member(self,member):
        self.members.append(member)
        print(f"Member '{member.name}' registered .")
    def issue_book(self,book_id,member_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print(f" '(book.title)' issued to(member.name).")
                else:
                    print("Book is not available.")
                return 
        print("Book not found.")  
    def return_book(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                print(f"Book '{book.title}' returned.")
                return
library = Library()
book1 = Book(101,"Python Programming") 
member1 = Member(1,"Arun")
library.add_book(book1)
library.register_member(member1)
library.issue_book(101, member1)
library.return_book(101)