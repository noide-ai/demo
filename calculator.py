import math

class Calculator:
    """Simple calculator class for basic arithmetic operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference between a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a divided by b.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def sqrt(self, a):
        """Return the square root of a.

        Raises:
            ValueError: If a is negative.
        """
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        return math.sqrt(a)


if __name__ == "__main__":
    # Example usage
    calc = Calculator()
    print("Addition:", calc.add(5, 3))
    print("Subtraction:", calc.subtract(10, 4))
    print("Multiplication:", calc.multiply(2, 7))
    print("Division:", calc.divide(20, 5))
    print("Square root:", calc.sqrt(16))  # 4.0
