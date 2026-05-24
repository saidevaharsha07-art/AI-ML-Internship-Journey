try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Division =", num1 / num2)
    lst = [10, 20, 30]
    index = int(input("Enter list index: "))
    print("Element =", lst[index])
except ValueError:
    print("Please enter valid integer values")
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Index out of range")