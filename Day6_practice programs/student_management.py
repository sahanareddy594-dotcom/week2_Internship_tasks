import json
import os

FILE_NAME = "students.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def add_student(data):
    sid = input("Enter Student ID: ")
    if sid in data:
        print("Student already exists!")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    data[sid] = {"Name": name, "Age": age, "Course": course}
    save_data(data)
    print("Student added successfully!")

# View all students
def view_students(data):
    if not data:
        print("No records found.")
        return
    for sid, info in data.items():
        print(f"\nID: {sid}")
        for key, value in info.items():
            print(f"{key}: {value}")


def search_student(data):
    sid = input("Enter Student ID to search: ")
    if sid in data:
        print("Student Found:")
        for key, value in data[sid].items():
            print(f"{key}: {value}")
    else:
        print("Student not found!")


def delete_student(data):
    sid = input("Enter Student ID to delete: ")
    if sid in data:
        del data[sid]
        save_data(data)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def main():
    data = load_data()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

main()

