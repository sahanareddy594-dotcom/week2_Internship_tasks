file = open("students.txt", "a")   

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i+1)
    name = input("Name: ")
    usn = input("USN: ")
    branch = input("Branch: ")
    marks = input("Marks: ")

    file.write(f"Name: {name}, USN: {usn}, Branch: {branch}, Marks: {marks}\n")

file.close()

print("\nStudent records saved successfully.")
