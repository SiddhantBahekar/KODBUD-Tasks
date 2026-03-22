# Simple Calculator (CLI)

def calculator():

    print("      Simple Calculator")
    print("Operations: +  -  *  /")
  
    try:
        num1 = float(input("Enter first number : "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number : "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if operator == "+":
        result = num1 + num2
        symbol = "+"
    elif operator == "-":
        result = num1 - num2
        symbol = "-"
    elif operator == "*":
        result = num1 * num2
        symbol = "×"
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed!")
            return
        result = num1 / num2
        symbol = "÷"
    else:
        print(f"Error: '{operator}' is not a valid operator. Use +, -, *, /")
        return

    
    result_display = int(result) if result == int(result) else round(result, 4)

    print("-" * 30)
    print(f"  {num1} {symbol} {num2} = {result_display}")
    print("=" * 30)


# Run again loop
while True:
    calculator()
    again = input("\nCalculate again? (yes/no): ").strip().lower()
    if again not in ("yes", "y"):
        print("Goodbye!")
        break
    print()
