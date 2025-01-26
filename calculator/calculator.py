def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b

def get_input():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        return a, b
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        return None, None

def display_result(operation, a, b, result):
    print(f"{a} {operation} {b} = {result}\n")

while True:
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter the number for the operation: ")

    if choice == "1":
        print("Addition")
        a, b = get_input()
        if a is not None and b is not None:
            result = add(a, b)
            display_result("+", a, b, result)

    elif choice == "2":
        print("Subtraction")
        a, b = get_input()
        if a is not None and b is not None:
            result = sub(a, b)
            display_result("-", a, b, result)

    elif choice == "3":
        print("Multiplication")
        a, b = get_input()
        if a is not None and b is not None:
            result = mul(a, b)
            display_result("*", a, b, result)

    elif choice == "4":
        print("Division")
        a, b = get_input()
        if a is not None and b is not None:
            result = div(a, b)
            display_result("/", a, b, result)

    elif choice == "5":
        print("Program ended")
        break

    else:
        print("Invalid choice! Please select a valid option from the list above.")
