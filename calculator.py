import math

class Calculator:

    def __init__(self):
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, x, op, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Inputs must be numbers")

        if op not in self.operations:
            raise ValueError("Invalid operation")

        return self.operations[op](x, y)


# Advanced operations
def power(x, y):
    return math.pow(x, y)

def sqrt(x, y):
    return math.sqrt(x)

def log(x, y):
    return math.log(x, y)


# Create calculator
calc = Calculator()

# Add advanced operations
calc.add_operation("**", power)
calc.add_operation("sqrt", sqrt)
calc.add_operation("log", log)


# Main program
while True:
    try:
        op = input("\nEnter operation (+, -, *, /, **, sqrt, log) or exit: ")

        if op.lower() == "exit":
            break

        x = float(input("Enter first number: "))
        y = 0 if op == "sqrt" else float(input("Enter second number: "))

        print("Result:", calc.calculate(x, op, y))

    except (ValueError, TypeError, ZeroDivisionError) as e:
        print("Error:", e)

print("Calculator closed!")


