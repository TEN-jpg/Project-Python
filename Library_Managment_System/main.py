import json
import os


class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True     #initially book is not issued


class Member():
    def __init__(self,name,member_ID):
        self.name = name
        self.member_ID = member_ID
        self.borrowed_books = []


class Library():
    def __init__(self):
        self.books = []
        self.members = []
        self.load_from_file()


    def save_to_file(self):
        data = {"books" : [], "members" : []}
        for book in self.books:
            data["books"].append({
                "title" : book.title,
                "author" : book.author,
                "available" : book.available
            })
        for member in self.members:
            data["members"].append({
                "name" : member.name,
                "member_ID" : member.member_ID,
                "borrowed_books": member.borrowed_books
            })
        
        with open("library.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully")


    def load_from_file(self):
        if not os.path.exists("library.json"):
            self.books = []
            self.members = []
            return
        
        with open("library.json", "r")as file:
            data = json.load(file)
        
        for b in data["books"]:
            book = Book(b["title"],b["author"])
            book.available = b["available"]
            self.books.append(book)

        for m in data["members"]:
            member = Member(m["name"], m["member_ID"])
            member.borrowed_books = m["borrowed_books"]
            self.members.append(member)

        print("Data loaded successfully")

                

    
    def add_book(self,title,author):
        book = Book(title,author)
        self.books.append(book)
        self.save_to_file()
    
    def add_member(self,name,member_ID):
        member = Member(name,member_ID)
        self.members.append(member)
        self.save_to_file()
    
    def borrow_book(self,member_ID,title):

        member = None
        for m in self.members:
            if m.member_ID == member_ID:
                member = m
                break
        if member is None:
            print("Member Not Found!")
            return
         
        book = None
        for b in self.books:
            if b.title == title:
                book = b
                break

        if book is None:    
            print("Book Not Found!")
            return

        if not book.available:
            print("Book already Borrowed!")
            return
        
        book.available = False
        member.borrowed_books.append(book.title)
        print(f"{book.title} borrowed by Member ID: {member.member_ID} successfully!")
        self.save_to_file()

    def return_book(self,member_ID,title):

        member = None
        for m in self.members:
            if m.member_ID == member_ID:
                member = m
                break
        if member is None:
            print("Member Not Found!")
            return 
        
        if title not in member.borrowed_books:
            print(f"Member ID: {member.member_ID} didn't borrowed '{title}'")
            return
        
        book = None
        for b in self.books:
            if b.title == title:
                book = b
                break
        
        book.available = True
        member.borrowed_books.remove(book.title)
        print(f"{book.title} borrowed by Member ID: {member.member_ID} is returned successfully!")
        self.save_to_file()

    def view_all_books(self):

        if not self.books:
            print("No books available in Library Currently!")
            return
        
        print("---------------------------BOOK LIST------------------------------")
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(f"'{book.title}' by '{book.author}' | {status}")

library = Library()

while True:
    print("=========LIBRARY=========")
    print("1. Add Book")
    print("2. Be Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter a book title: ")
        author = input("Enter the Author name: ")
        library.add_book(title,author)
    
    elif choice == "2":
        name = input("Enter your name: ")
        member_ID = input("Enter Member ID: ")
        library.add_member(name, member_ID)

    elif choice == "3":
        member_ID = input("Enter Member ID: ")
        title = input("Enter a book title: ")
        library.borrow_book(member_ID,title)
    
    elif choice == "4":
        member_ID = input("Enter Member ID: ")
        title = input("Enter a book title: ")
        library.return_book(member_ID,title)
    
    elif choice == "5":
        library.view_all_books()

    elif choice == "6":
        print("Thanks for using Library System")
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please enter a valid option")
    