import json
import os

class Student:
    def __init__(self, name, roll_number):
        self.Name = name
        self.Roll_number = roll_number
        
    def marks(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print("NAME:-", self.Name)
        print("Roll No:-", self.Roll_number)
        print("Physics:-", self.phy)
        print("Chemistry:-", self.chem)
        print("Maths:-", self.maths)


class StudentManager:
    def __init__(self):
        self.students = []
        self.load_from_file()     

    def save_to_file(self):
     data = []

     for student in self.students:
        student_dict = {
            "name" : student.Name,
            "roll_number" : student.Roll_number,
            "marks" : {
                "physics" : student.phy,
                "chemistry" : student.chem,
                "maths" : student.maths
            }
        }  
        data.append(student_dict)

     with open("student.json", "w")as file:
            json.dump(data, file, indent=4) 

     print("Data saved Successfully")



    def load_from_file(self):
        if not os.path.exists("student.json"):
            self.students = []
            return
        
        with open("student.json", "r")as file:
            data = json.load(file)

        for item in data:
            name = item["name"]
            roll = item["roll_number"]

            phy = item["marks"]["physics"]
            chem = item["marks"]["chemistry"]
            maths = item["marks"]["maths"]

            student = Student(name, roll)
            student.marks(phy, chem, maths)

            self.students.append(student)

        print("Student loaded Successfully")



    def add_student(self, name, roll_number, phy, chem, maths):
        student = Student(name, roll_number)
        student.marks(phy, chem, maths)
        self.students.append(student)
        self.save_to_file()


    def view_student(self):
        if len(self.students) == 0:
            print("No Students Found")
        else:
            for student in self.students:
                student.display()
                print("--------------------------")

    def search_student(self, roll_number):
        for student in self.students:
            if student.Roll_number == roll_number:
                student.display()
                return student
        print("Student Not Found")
        return None
    

    def update_student(self, roll_number, new_phy, new_chem, new_maths):
        student = self.search_student(roll_number)
        if student is None:  
            print("Student Not Found")
            return
        student.marks(new_phy, new_chem, new_maths)
        self.save_to_file()
        print("Marks updated successfully!")


    def delete_student(self, roll_number):
        student = self.search_student(roll_number)
        if student is None:  
            print("Student Not Found")
            return
        self.students.remove(student)
        self.save_to_file()
        print("Student deleted Successfully")

manager = StudentManager()

while True:
        print("\n------ STUDENT MANAGEMENT SYSTEM ------")
        print("1. Add Student")
        print("2. View all students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print("------------------------")


        if choice == "1":
            name = input("Enter Name: ")
            roll = int(input("Enter Roll Number: "))
            phy = int(input("Enter Physics Marks: "))
            chem = int(input("Enter Chemistry Marks: "))
            maths = int(input("Enter Maths Marks: "))
            manager.add_student(name, roll, phy, chem, maths)

        elif choice == "2":
            manager.view_student()

        elif choice == "3":
            roll = int(input("Enter a Roll number to Search: "))
            print("---------------------------------------------")
            manager.search_student(roll)

        elif choice == "4":
            roll = int(input("Enter a Roll number to update: "))
            print("-----------------------------------------")
            new_phy = int(input("Enter New Physics Marks: "))
            new_chem = int(input("Enter New Chemistry Marks: "))
            new_maths = int(input("Enter New Maths Marks: "))
            print("----------------------------------------")
            manager.update_student(roll, new_phy, new_chem, new_maths)
        
        elif choice == "5":
            roll = int(input("Enter a Roll Numebr to Delete: "))
            print("-------------------------------------------")
            manager.delete_student(roll)
        
        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid Choice! Please choose a valid option.")






    








