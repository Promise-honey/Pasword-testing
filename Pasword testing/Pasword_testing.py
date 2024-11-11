import re

def test_password_strength(password):
    # check password length
    if len(password) < 8:
        return "password is too short. it should be at least 8 characters long."

    # Any Upper case letters?
    if not re.search(r'[A-Z]', password):
        return "password should contain at least one uppercase letter."

    # Any lower case letters?
    if not re.search(r'[a-z]', password):
        return "password should contain at least one lowercase letter."

    # look for numbers
    if not re.search(r'[0-9]', password):
        return "password should contain at least one number."

    # look for special characters
    if not re.search(r'[@$!%*?&]', password):
        return "password should contain at least one special character like @$!%*?&."

    # If everything is correct
    return "password is strong!"

def validate_password():
    while True:
        password = input("enter a password to test: ")
        result = test_password_strength(password)
        print(result)
        
        if result == "password is strong!":
            break  # Exit if password is strong
        else:
            print("please try again.")

# run validation
validate_password()


