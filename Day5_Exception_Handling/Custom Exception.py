class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeError("You must be 18 or older")
    print("Access granted")

except InvalidAgeError as e:
    print("Error:", e)
except ValueError:
    print("Enter a valid age")
