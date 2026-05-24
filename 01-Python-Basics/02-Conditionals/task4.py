ch = input("Enter a character: ")
if ch.isalpha():
    print("The character is an alphabet.")
elif ch.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")