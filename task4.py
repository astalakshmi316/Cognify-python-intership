def basic_calculator():
    try:
        # User kitta irundhu inputs vangarom
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /, %): ").strip()

        # Oru oru operator-kum calculation check panrom
        if operator == '+':
            print(f"Result: {num1 + num2}")
        elif operator == '-':
            print(f"Result: {num1 - num2}")
        elif operator == '*':
            print(f"Result: {num1 * num2}")
        elif operator == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed!")
        elif operator == '%':
            print(f"Result: {num1 % num2}")
        else:
            print("Invalid operator selected!")
    except ValueError:
        print("Please enter valid numeric values.")

# Function-ah call panrom
basic_calculator()