# develop calculator using classes 
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        if y == 0:
            self.result = "Cannot divide by zero"
        else:
            self.result = x / y

    def get_result(self):
        return self.result

# Create an instance of the Calculator class
calculator = Calculator()

# Example calculations
calculator.add(5, 3)
print("Addition Result:", calculator.get_result())

calculator.subtract(10, 4)
print("Subtraction Result:", calculator.get_result())

calculator.multiply(6, 7)
print("Multiplication Result:", calculator.get_result())

calculator.divide(15, 3)
print("Division Result:", calculator.get_result())

calculator.divide(10, 0)
print("Division Result:", calculator.get_result())
