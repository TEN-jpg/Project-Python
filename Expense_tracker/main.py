import json
import os
from datetime import datetime

class Expense():
    def __init__(self,amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description
        self.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display(self):
        print(f"{self.date_time} | {self.category:<10} | ${self.amount:<7} | {self.description}")


    def to_dict(self):
        return{
            "amount" : self.amount,
            "category" : self.category,
            "description" : self.description,
            "date_time" : self.date_time
        }
    

class ExpenseTracker():
    def __init__(self):
        self.expenses = []
        self.load_from_file()

    def save_to_file(self):
        data = []

        for exp in self.expenses:
            data.append(exp.to_dict())
        
        with open("expense.json", "w") as file:
            json.dump(data, file, indent=4)
        
        print("Data Saved")


    def load_from_file(self):

        if not os.path.exists("expense.json"):
         return
        
        with open("expense.json", "r")as file:
         data = json.load(file)

        for item in data:
            exp = Expense(item["amount"], item["category"], item["description"])
            exp.date_time = item["date_time"]
            self.expenses.append(exp)

        print("Data Loaded")


    def add_expense(self,amount, category, description):
        
        if amount <= 0:
            print("---------------------")
            print("Enter a valid amount")
            print("---------------------")
            return
        
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        self.save_to_file()

    def view_expenses(self):

        if not self.expenses:
            print("No Expenses yet")
            return
        
        for i in self.expenses:
            i.display()

    def total_expenses(self):

        if not self.expenses:
            print("No Expense to calculate")
            return

        total = 0
        for exp in self.expenses:
            total += exp.amount
        print(f"Total Expense = ${total}")

    def category_report(self, category):
    
        total = 0

        for cat in self.expenses:
            if cat.category == category:
                total += cat.amount

        if total == 0:
            print("----------------------------")
            print("NO Expenses in this category")
            print("----------------------------")
        else:
            print("---------------------------------------")
            print(f"Total Expenses of {category}: ${total}")
            print("---------------------------------------")

expenses = ExpenseTracker()

while True:
    print("====EXPENSE TRACKER====")
    print("1.Add Expenses")
    print("2.View All Expenses")
    print("3.Total Expenses")
    print("4.Category Wise Expenses")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = int(input("Enter Expense Amount: $"))
        category = input("Enter the Category of Expense: ")
        
        description_permission = input("Do you want to write a Description? (Y/N): ")
        if description_permission.lower() == "y":
            description = input("Enter Description: ")
        else:
            description = ""

        expenses.add_expense(amount, category, description)

    elif choice == "2":
        print("----> ALL EXPENSE")
        expenses.view_expenses()
        print("---------------------")

    elif choice == "3":
        print("---------------------")
        expenses.total_expenses()
        print("---------------------")

    elif choice == "4":
        category = input("Enter a Category Name: ")
        expenses.category_report(category)

    elif choice == "5":
        print("------------------------------------")
        print("Thank you for using Expense Tracker")
        print("Exiting...")
        break
    
    else:
        print("-------------------------------------------")
        print("Invalid choice! Please enter a valid option")
        print("-------------------------------------------")



    
        

