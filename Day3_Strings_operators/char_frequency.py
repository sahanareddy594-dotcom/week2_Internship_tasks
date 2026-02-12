string = input("Enter a string: ")

for char in set(string):
    print(char, ":", string.count(char))
