import string

def check_password(password, min_length, numbers=True, special_characters=True):
    meets_criteria = len(password) >= min_length

    if numbers:
        meets_criteria = meets_criteria and any(char in string.digits for char in password)

    if special_characters:
        meets_criteria = meets_criteria and any(
            char in string.punctuation for char in password
        )

    return meets_criteria


min_length = int(input("Enter the minimum length: "))
has_numbers = input("Should your password contain numbers? (y/n): ").lower() == "y"
has_special_characters = (
    input("Should your password contain special characters? (y/n): ").lower() == "y"
)

password = input("Create your password: ")

if check_password(password, min_length, has_numbers, has_special_characters):
    print("Your password meets the requirements.")
else:
    print("Your password does not meet the requirements.")