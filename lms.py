class Book:
    
    def __init__(self,title, author,isbn):
        self.title   = title
        self.author  = author
        self.isbn    = isbn
        self.is_borrowed = False
        self.borrowed_by = None
        

    def __str__(self):
        
         borrowed_status = f"Yes, by {self.borrowed_by}"        
         return (f"Title: {self.title}," if self.is_borrowed else "No"
                 f"Author:{self.author},"
                 f"ISBN:{self.isbn},"
                 f"Borrowed:{"yes" if self.is_borrowed else "No"}"
                 
                 )

class User:
    def __init__(self,user_id,name,email):
        self.user_id = user_id
        self.name = name
        self.email = email
        
        
    def __str__(self):
        return f"User Id: {self.user_id}, Name: {self.name}, Email: {self.email}"
                



class Library:
    
    def __init__(self):
        self.books=[]
        self.users = {}
        
    
    def add_book(self,book):
        self.books.append(book)
        print(f"Book {book.title} was added to the library")   
        
    def list_books(self):
        if not self.books:
            print("No Book in the library.")
        
        for book in self.books:
            print(book)
            
    
        
        
        
        
    def add_user(self,user):
        if user.user_id in self.users:
            print(f"User Id {user.user_id} already exist ")
            return
        self.users[user.user_id] = user
        print(f"User {user.name} added with ID {user.user_id}")
        
    
    def list_user(self):
        if not self.users:
            print("YOu are not listed")
            return
        for user_id,user in self.users.items():
            print(user)
    
    
    def update_user(self,user_id,name=None,email=None):
        if user_id not in self.users:
            print("Your user is doesn't exist")
            return
        if name: 
            self.users[user_id].name = name
        if email:
            self.users[user_id].email = email
            print(f"User {user_id} updated")
            
    
    def delete_user(self,user_id):
        if user_id not in self.users:
            print("user not found")
            return
        if user_id:
            del self.users[user_id]
            print(f"user {user_id} is deleted")  
            
    
    def borrow_book(self,isbn,user_id):
        if user_id not in self.users:
            print(f"User ID {user_id} does not exist")
            return
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                book.borrowed_by = user_id
                print(f" {self.users[user_id].name} has borrowed {book.title}")
            return
        print('Book not available')
    
    def return_book(self,isbn,user_id):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed and book.borrowed_by == user_id:
              book.is_borrowed = False
              book.borrowed_by = None
              print(f"User {self.users[user_id].name} has returned {book.title} .")
              return
        print("Book is not available, or has been borrowed , or has not beem by this user"   )
            
    
        

book1 = Book("Clean Code", "Robert C. Martin", "978-0132350884")
book2 = Book("Atomic Habits", "James Clear", "978-0735211292")
book3 = Book("Python Tricks", "Dan Bader", "978-1775093305")
book4 = Book("The Pragmatic Programmer", "Andrew Hunt & David Thomas", "978-0201616224")
book5 = Book("Introduction to Algorithms", "Thomas H. Cormen", "978-0262033848")


library = Library()












