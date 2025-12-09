import json
import os

class Password():
    def __init__(self, website, username, password, date_saved, id):
        self.website = website
        self.username = username
        self.password = password
        self.date_saved = date_saved
        self.id = id
    
    def validate(self):
        if not self.website or self.website.strip() == "":
            raise ValueError("Website cannot be empty")
        
        if not self.username or self.username.strip() == "":
            raise ValueError("Username cannot be empty")

        if not self.password or self.password.strip() == "":
            raise ValueError("Password cannot be empty")
        
        if len(self.password) < 6:
            raise ValueError("Password too short")
        
        return True

    def to_dict(self):
        return{
            "website" : self.website,
            "username" : self.username,
            "password" : self.password,
            "date_saved" : self.date_saved,
            "id" : self.id
        }
    
class PasswordManager():
    def __init__(self):
        self.passwords = []
        self.load_from_file()

    def save_to_file(self):
        try:
            data = [p.to_dict() for p in self.passwords]
    
            
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
            
            print("Data Saved Successfully!")

        except Exception as e:
            print("Error Saving file:",e)
    
    def load_from_file(self):
        try:
            if not os.path.exists("passwords.json"):
                self.passwords = []
                return
            
            with open("passwords.json", "r")as file:
                data = json.load(file)
    
            self.passwords = [
                Password(
                    item["website"],
                    item["username"],
                    item["password"],
                    item["date_saved"],
                    item["id"]
                )
                for item in data
            ]

            print("DATA LOADED SUCCESSFULLY!")

        except json.JSONDecodeError:
            print("Error: JSON file is corrupted")
            self.passwords = []
        
        except Exception as e:
            print("Error loading file:", e)
            self.passwords = []

    def add_password(self, website, username, password):

        new_id = len(self.passwords) + 1

        from datetime import datetime
        date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        passwrd = Password(website, username, password, date_now, new_id)
        passwrd.validate()

        self.passwords.append(passwrd)
        self.save_to_file()
        print("Password Saved Successfully")

    def view_all(self):

        if not self.passwords:
            print("NO PASSWORD SAVED YET")
            return
        
        print("\nSaved Passwords:")
        print("------------------------------")
        
        for p in self.passwords:
            masked = "*" * (len(p.password) - 3) + p.password[-3:] #if password <= 3 becomes zero or negative this causes weird masking.
        
            print(f"ID: {p.id}")      
            print(f"Website: {p.website}")
            print(f"Username: {p.username}")
            print(f"Password: {masked}")
            print(f"Date Saved: {p.date_saved}")
            print("-------------------------------")

    def search_by_website(self, website):

        search = website.lower()

        matches = [p for p in self.passwords if p.website.lower() == search]

        if not matches:
            print("NO PASSWORD FOUND FOR THIS WEBSITE")
            return
        
        print("\nResult for '{website}':")
        print("-----------------------------")
        for p in matches:
            masked = "*" * (len(p.password) - 3) + p.password[-3:] #if password <= 3 becomes zero or negative this causes weird masking.
            
            print(f"ID: {p.id}")      
            print(f"Website: {p.website}")
            print(f"Username: {p.username}")
            print(f"Password: {masked}")
            print(f"Date Saved: {p.date_saved}")
            print("-------------------------------")

    def delete_password(self):

        try:
            delete_id = int(input("Enter ID to Delete: "))
        except ValueError:
            print("Invalid ID. Must contain only numbers")
            return
        
        matches = [p for p in self.passwords if p.id == delete_id]

        if not matches:
            print("NO SUCH ID EXISTS")
            return

        passwrd_to_delete = matches[0]
        self.passwords.remove(passwrd_to_delete)
        self.save_to_file()
        print("ID DELETE SUCCESSFULLY")

def main():

    manager = PasswordManager()

    while True:
        print("\n----- PASSWORD MANAGER -----")
        print("1. Add Password")
        print("2. View All Passwords")
        print("3. Search by Website")
        print("4. Delete Password")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            website = input("Enter Website: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            try:
                manager.add_password(website, username, password)
            except Exception as e:
                print("Error:", e)
        
        elif choice == "2":
            manager.view_all()

        elif choice == "3":
            website = input("Enter Website to search: ")
            manager.search_by_website(website)
        
        elif choice == "4":
            manager.delete_password()

        elif choice == "5":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__": #If you run this file - run main()
    main()                 #If you import this file → don’t run main() Because main() is your entire MENU system.
                           #and it takes input from user so there is no need to reuse menu instead reuse 
                           #classes and methods they contain the logic

        

    

     
    


        
         