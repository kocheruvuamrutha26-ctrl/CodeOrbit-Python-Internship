"""
CodeOrbit Tech - Python Programming Internship
Task 1: Simple Calculator

A beginner-friendly calculator for addition, subtraction,
multiplication, and division.
"""

def calculate():
    """Run the calculator program."""
    print("\n===== SIMPLE CALCULATOR =====")

    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        print("\nChoose an operation:")
        print("+  Addition")
        print("-  Subtraction")
        print("*  Multiplication")
        print("/  Division")

        operation = input("Enter operation: ").strip()

        if operation == "+":
            result = first + second
        elif operation == "-":
            result = first - second
        elif operation == "*":
            result = first * second
        elif operation == "/":
            if second == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = first / second
        else:
            print("Error: Invalid operation. Please choose +, -, *, or /.")
            return

        print(f"Result: {first:g} {operation} {second:g} = {result:g}")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculate()
