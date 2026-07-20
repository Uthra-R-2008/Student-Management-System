class Student:
    def __init__(self, roll, name, age, dept, marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.dept = dept
        self.marks = marks


students = []


def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    dept = input("Enter Department: ")
    marks = float(input("Enter Marks: "))

    students.append(Student(roll, name, age, dept, marks))
    print("Student Added Successfully!\n")


def display_students():
    if not students:
        print("No Records Found!\n")
        return

    print("\nStudent Records")
    for s in students:
        print(f"Roll: {s.roll}")
        print(f"Name: {s.name}")
        print(f"Age: {s.age}")
        print(f"Department: {s.dept}")
        print(f"Marks: {s.marks}")
        print("------------------------")


def search_student():
    roll = int(input("Enter Roll Number to Search: "))

    for s in students:
        if s.roll == roll:
            print("Student Found")
            print(f"Name: {s.name}")
            print(f"Age: {s.age}")
            print(f"Department: {s.dept}")
            print(f"Marks: {s.marks}")
            return

    print("Student Not Found!\n")


def update_student():
    roll = int(input("Enter Roll Number to Update: "))

    for s in students:
        if s.roll == roll:
            s.name = input("Enter New Name: ")
            s.age = int(input("Enter New Age: "))
            s.dept = input("Enter New Department: ")
            s.marks = float(input("Enter New Marks: "))
            print("Record Updated Successfully!\n")
            return

    print("Student Not Found!\n")


def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))

    for s in students:
        if s.roll == roll:
            students.remove(s)
            print("Student Deleted Successfully!\n")
            return

    print("Student Not Found!\n")


def sort_students():
    students.sort(key=lambda x: x.roll)
    print("Students Sorted by Roll Number.\n")


while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Students")
    print("7. Exit")

    try:
        choice = int(input("Enter Choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            display_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            sort_students()
        elif choice == 7:
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Please enter a number between 1 and 7.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")