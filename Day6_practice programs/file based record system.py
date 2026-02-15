import json
import os

FILE = "records.json"

# Load records from file
def load_records():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save records to file
def save_records(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add record
def add_record(data):
    sid = input("Enter Student ID: ")
    if sid in data:
        print("Record already exists!")
        return
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    data[sid] = {"Name": name, "Marks": marks}
    save_records(data)
    print("Record saved successfully!")

# View records
def view_records(data):
    if not data:
        print("No records found.")
        return
    for sid, info in data.items():
        print(f"\nID: {sid}")
        print("Name:", info["Name"])
        print("Marks:", info["Marks"])

# Search record
def search_record(data):
    sid = input("Enter Student ID to search: ")
    if sid in data:
        print("Record Found:")
        print(data[sid])
    else:
        print("Record not found.")

# Delete record
def delete_record(data):
    sid = input("Enter Student ID to delete: ")
    if sid in data:
        del data[sid]
        save_records(data)
        print("Record deleted.")
    else:
        print("Record not found.")

# Main menu
def main():
    data = load_records()

    while True:
        print("\n===== FILE BASED RECORD SYSTEM =====")
        print("1. Add Record")
        print("2. View Records")
        print("3. Search Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_record(data)
        elif choice == "2":
            view_records(data)
        elif choice == "3":
            search_record(data)
        elif choice == "4":
            delete_record(data)
        elif choice == "5":
            print("Program closed.")
            break
        else:
            print("Invalid choice!")

main()
