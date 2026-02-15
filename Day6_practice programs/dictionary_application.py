dictionary = {}

while True:
    print("\n===== DICTIONARY MENU =====")
    print("1. Add Word")
    print("2. Search Meaning")
    print("3. Update Meaning")
    print("4. Delete Word")
    print("5. View Dictionary")
    print("6. Exit")

    choice = input("Enter your choice: ")

    
    if choice == "1":
        word = input("Enter word: ")
        meaning = input("Enter meaning: ")
        dictionary[word] = meaning
        print("Word added successfully.")


    elif choice == "2":
        word = input("Enter word to search: ")
        if word in dictionary:
            print("Meaning:", dictionary[word])
        else:
            print("Word not found.")

    
    elif choice == "3":
        word = input("Enter word to update: ")
        if word in dictionary:
            dictionary[word] = input("Enter new meaning: ")
            print("Meaning updated.")
        else:
            print("Word not found.")

  
    elif choice == "4":
        word = input("Enter word to delete: ")
        if word in dictionary:
            del dictionary[word]
            print("Word deleted.")
        else:
            print("Word not found.")

    
    elif choice == "5":
        if dictionary:
            for w, m in dictionary.items():
                print(f"{w} : {m}")
        else:
            print("Dictionary is empty.")

  
    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice! Try again.")
