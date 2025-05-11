# Python Calculator

This repository provides a simple Python `Calculator` class that supports basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division
- Square root

## Usage

```python
from calculator import Calculator

calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.subtract(10, 4))  # 6
print(calc.multiply(2, 7))   # 14
print(calc.divide(20, 5))     # 4.0
print(calc.sqrt(16))          # 4.0
```

Division by zero or square root of a negative number raises a `ValueError`.  