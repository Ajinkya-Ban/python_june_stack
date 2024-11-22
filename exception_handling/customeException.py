class InvalidAgeException(Exception):
    "Raised when the input number is less then 18"
    pass

try:
    num = int(input("Enter the number = "))
    if num < 18:
        raise InvalidAgeException
    else:
        print("Eligible for voting")
except InvalidAgeException:
    print("Exception occured: Invalid Age")

