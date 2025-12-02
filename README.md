# Library-Management-System-Python-OOP-Project
This project is a console-based Library Management System built using Object-Oriented Programming (OOP) in Python. It simulates a real library where users can register, borrow books, return books, and view available resources.


✔ Add Books to the library
✔ Register Users with unique user IDs
✔ List all Books with borrowing status
✔ List all Registered Users
✔ Update / Delete User Details
✔ Borrow a Book (only if available)
✔ Return a Borrowed Book
✔ Fully designed with OOP concepts (Classes, Objects, Methods, Encapsulation)

| Concept              | Implemented in                           |
| -------------------- | ---------------------------------------- |
| Classes & Objects    | `Book`, `User`, `Library`                |
| Encapsulation        | Object attributes and controlled methods |
| `__str__` Overriding | Readable object outputs                  |
| Lists & Dictionaries | Storing books and users                  |
| Conditionals & Loops | Searching and validating records         |

| Class       | Responsibility                                                 |
| ----------- | -------------------------------------------------------------- |
| **Book**    | Stores book details and borrowing status                       |
| **User**    | Stores user information (ID, name, email)                      |
| **Library** | Core system — manages books, users, borrow & return operations |


library = Library()

# Add books
library.add_book(Book("Clean Code", "Robert C. Martin", "978-0132350884"))

# Add user
library.add_user(User(1, "Basavaraj", "example@mail.com"))

# Borrow & return
library.borrow_book("978-0132350884", 1)
library.return_book("978-0132350884", 1)

# List books and users
library.list_books()
library.list_users()


Future Enhancements (Optional Ideas)

🔹 Save data to a JSON / CSV file
🔹 Build a menu-based CLI interface
🔹 Convert into a Flask / Django Web App
🔹 Integrate SQLite / PostgreSQL database
🔹 Add admin login and authentication



This project is a great practice piece for beginners to understand:

Object-Oriented Programming (OOP)

Python data structures

Real-world software design thinking


Feel free to fork & improve — contributions are welcome!

If you want, I can also generate:
🔹 GIF demo for the README
🔹 Project title logo
🔹 Fully formatted README.md file with icons and badges
Just tell me anytime 🚀
