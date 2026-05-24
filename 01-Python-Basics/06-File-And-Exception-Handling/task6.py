class PasswordError(Exception):
    pass
password = input("Enter password: ")
try:
    if len(password) < 6:
        raise PasswordError("Password must contain at least 6 characters")
    else:
        print("Password accepted")
except PasswordError as e:
    print(e)