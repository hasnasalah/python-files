def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")


try:
    age = int(input("Please enter your age: "))
    validate_age(age)
    print("Your age was accepted!")

except ValueError as error:
    print("Error:", error)