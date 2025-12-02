class BankAccount():
    def __init__(self, name, account_number, pin):
       self.name = name
       self.account_number = account_number
       self.pin = pin
       self.balance = 0

    def verify_pin(self, enter_pin):
       return self.pin == enter_pin
    
    def deposit_money(self, amount, enter_pin):
        if not self.verify_pin(enter_pin):
           print("Incorrect Pin")
           return
    
        if amount <= 0:
            print("Invalid Deposit Amount")
        else:
           self.balance += amount
           print("Balance: $",self.balance)


    def withdraw_money(self, amount, enter_pin):
       if not self.verify_pin(enter_pin):
        print("Incorrect Pin")
        return
       
       if amount <= 0:
          print("Invalid Withdraw Amount")
       elif self.balance < amount:
          print("Insufficinet Money")
       else:
        self.balance -= amount
        print("Balance: $",self.balance)


    def check_balance(self, enter_pin):
        if not self.verify_pin(enter_pin):
           print("Incorrect Pin")
           return
        else:
           print("Your Balance: $",self.balance)
      
    def to_dict(self):
       return {
          "name": self.name,
          "account_number": self.account_number,
          "pin": self.pin,
          "balance": self.balance 
       }
    


class Banksystem():
   def __init__ (self):
      self.accounts = {}
      self.load_data()

   def save_to_file(self):
      import json 
      data = []

      for acc in self.accounts.values():
         data.append(acc.to_dict())

      with open("accounts.json", "w") as file:
         json.dump(data, file, indent=4)  
   
   def load_data(self):
      import json
      import os
      if not os.path.exists("accounts.json"):
         return
      
      with open("accounts.json", "r")as file:
         data = json.load(file)

      for item in data:
         acc = BankAccount(item["name"], item["account_number"], item["pin"])
         acc.balance = item["balance"]
         self.accounts[acc.account_number] = acc
      

   def create_acc(self,name,account_number,pin):
      user = BankAccount(name, account_number, pin)
      self.accounts[account_number] = user
      self.save_to_file()
      print("Account created Successfully")

   def search_acc(self,account_number,pin):
      acc = self.accounts.get(account_number)
      if acc and acc.verify_pin(pin):
            return acc
      return None
   


bank = Banksystem()

bank.create_acc("Ten", 1234, 3635)
bank.create_acc("Son", 2345, 1234)


while True:
   print("===============BANK LOGIN==================")
   acc_num = int(input("Enter your Account number: "))
   pin = int(input("Enter PIN: "))

   user = bank.search_acc(acc_num,pin)

   if user:
      print(f"----------Welcome {user.name}-------------")


      while True:
         print("--------------ATM---------------")
         print("1.Check Balance")
         print("2.Deposit Amount")
         print("3.Withdraw Amount")
         print("4.Exit")
      
         choice = input("Enter your choice: ")
      
         if choice == "1":
              pin = int(input("Enter PIN: "))
              user.check_balance(pin)
      
         elif choice == "2":
              pin = int(input("Enter PIN: "))
              amount = int(input("Enter Depsit Amount: $"))
              user.deposit_money(amount, pin)
              bank.save_to_file()
              
           
         elif choice == "3":
              pin = int(input("Enter PIN: "))
              amount = int(input("Enter Withdraw Amount: $"))
              user.withdraw_money(amount, pin)
              bank.save_to_file()
           
         elif choice == "4":
              print("Exiting...")
              break
         else:
            print("Invalid option")

   else:
      print("WRONG Account Number or PIN")

   
         
               
       

      




    



