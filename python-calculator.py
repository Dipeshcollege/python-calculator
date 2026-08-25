import math


def menu():
    print("\n\nWelcome to the Calculator")
    print("Please select an operation:\n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Exit\n")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        add()
    elif choice == '2':
        subtract()
    elif choice == '3':
        multiply()
    elif choice == '4':
        divide()
    elif choice == '5':
        power()
    elif choice == '6':
        sqrt_op()
    elif choice == '7':
        percentage()
    elif choice == '8':
        print("Exiting the calculator.")
        exit()
    else:
        print("Invalid choice. Please try again.")
        menu()


def add():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The result of addition is: {result}")
    menu()


def subtract():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
    menu()


def multiply():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
    menu()


def divide():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The result of division is: {result}")
    menu()

def power():
    base = float(input("Enter the base number: "))
    exponent = float(input("Enter the exponent: "))
    result = base ** exponent
    print(f"The result of {base} raised to the power {exponent} is: {result}")
    menu()

def sqrt_op():
    num = float(input("Enter the number to find square root of: "))
    if num < 0:
        print("Error: Cannot take square root of a negative number.")
    else:
        result = math.sqrt(num)
        print(f"The square root of {num} is: {result}")
    menu()

def percentage():
    print("Percentage options:")
    print("1. Calculate X% of Y")
    print("2. Calculate what percentage X is of Y")
    opt = input("Enter your choice (1-2): ")
    if opt == '1':
        x = float(input("Enter X (percent): "))
        y = float(input("Enter Y (number): "))
        result = (x / 100) * y
        print(f"{x}% of {y} is: {result}")
    elif opt == '2':
        x = float(input("Enter X (part): "))
        y = float(input("Enter Y (whole): "))
        if y == 0:
            print("Error: Division by zero.")
        else:
            result = (x / y) * 100
            print(f"{x} is {result}% of {y}")
    else:
        print("Invalid option.")
    menu()

if __name__ == "__main__":
    menu()
    