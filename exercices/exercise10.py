#any() is a built-in function that checks whether at least one item in an iterable is True.

def check_password():
    password = input("Enter your password: ")
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False

    print("Password is valid.")
    return True

check_password()