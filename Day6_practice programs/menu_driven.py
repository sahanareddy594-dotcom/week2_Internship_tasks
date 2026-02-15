marks = []

while True:
    print("\n===== STUDENT MARKS MENU =====")
    print("1. Add Marks")
    print("2. View All Marks")
    print("3. Average Marks")
    print("4. Highest Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        m = float(input("Enter marks: "))
        marks.append(m)
        print("Marks added.")

    elif choice == "2":
        print("Marks List:", marks)

    elif choice == "3":
        if marks:
            print("Average =", sum(marks)/len(marks))
        else:
            print("No marks available.")

    elif choice == "4":
        if marks:
            print("Highest =", max(marks))
        else:
            print("No marks available.")

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Try again.")
