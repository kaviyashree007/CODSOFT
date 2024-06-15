def simplecalculator():
    print("Welcome to the Simple Calculator!")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        number1 = float(input("Enter the first number for calculation: "))
        number2 = float(input("Enter the second number for calculation: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    
    operation = input("Choose an operation from the given choices (1, 2, 3, 4): ")

    
    if operation == '1':
        answer = number1 + number2
        print(f"The result of {number1} + {number2} is: {answer}")
    elif operation == '2':
        answer = number1 - number2
        print(f"The result of {number1} - {number2} is: {answer}")
    elif operation == '3':
        answer = number1 * number2
        print(f"The result of {number1} * {number2} is: {answer}")
    elif operation == '4':
        if number2 != 0:
            answer = number1 / number2
            print(f"The result of {number1} / {number2} is: {answer}")
        else:
            print("Error: Invalid input, Division by zero is not defined.")
    else:
        print("Invalid operation choice. Please choose from the choice given.")


simplecalculator()
