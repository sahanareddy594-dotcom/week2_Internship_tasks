try:
    f = open("sample.txt", "r")
    data = f.read()
    print(data)
    f.close()
except FileNotFoundError:
    print("Error: File does not exist")
