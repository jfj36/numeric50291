import numpy as np

###
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface
## function that will prompt the user for input and
## call the appropriate function based on the user's
## input. The interface function should continue to
## prompt the user for input until the user enters
## 'exit'. 
##
## 2) The interface function should also handle
## any exceptions that might be thrown by the basic
## operations functions. If an exception is thrown,
## the interface function should print an error message
## and continue to prompt the user for input.
##
## 3) Add other "operations" to the calculator, that
## involve complicated operations (e.g., trigonometric
## functions, logarithms, etc.).



def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

def logarithm(a):
    """Calculate the logarithm of a number using numpy."""
    return np.log(a)

def exponential(a):
    """Calculate the Euler's exponential of a number using numpy."""
    return np.exp(a)

def sin(a):
    """Calculate the sine of an angle in radians using numpy."""
    return np.sin(a)

def cos(a):
    """Calculate the cosine of an angle in radians using numpy."""
    return np.cos(a)

def tan(a):
    """Calculate the tangent of an angle in radians using numpy."""
    return np.tan(a)

def square(a):
    """Calculate the square of a number using numpy."""
    return np.square(a)

def square_root(a):
    """Calculate the square root of a number using numpy."""
    return np.sqrt(a)

def logit(a):
    """Calculate the logit function of a number using numpy."""
    return np.log(a / (1 - a))



def interface():
    """Interface function for the calculator."""
    while True:
        try:
            operation = input("Enter an operation (add, subtract, multiply, divide, logarithm, exponential, sin, cos, tan, square, square_root, logit) or 'exit' to quit: ")
            
            if operation == 'exit':
                break
            
            if operation not in ['add', 'subtract', 'multiply', 'divide', 'logarithm', 'exponential', 'sin', 'cos', 'tan', 'square', 'square_root', 'logit']:
                print("Invalid operation. Please try again.")
                continue
            
            if operation in ['add', 'subtract', 'multiply', 'divide']:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                
                if operation == 'add':
                    result = add(a, b)
                elif operation == 'subtract':
                    result = subtract(a, b)
                elif operation == 'multiply':
                    result = multiply(a, b)
                elif operation == 'divide':
                    if b == 0:
                        print("Cannot divide by zero. Please try again.")
                        continue
                    result = divide(a, b)
            
            elif operation in ['logarithm', 'exponential', 'sin', 'cos', 'tan', 'square', 'square_root', 'logit']:
                a = float(input("Enter the number: "))
                
                if operation == 'logarithm':
                    if a <= 0:
                        print("Cannot compute logarithm of a non-positive number. Please try again.")
                        continue
                    result = logarithm(a)
                elif operation == 'exponential':
                    result = exponential(a)
                elif operation == 'sin':
                    result = sin(a)
                elif operation == 'cos':
                    result = cos(a)
                elif operation == 'tan':
                    result = tan(a)
                elif operation == 'square':
                    result = square(a)
                elif operation == 'square_root':
                    if a < 0:
                        print("Cannot compute square root of a negative number. Please try again.")
                        continue
                    result = square_root(a)
                elif operation == 'logit':
                    if a <= 0 or a >= 1:
                        print("Cannot compute logit function for a number outside the range (0, 1). Please try again.")
                        continue
                    result = logit(a)
            
            print("Result:", result)
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
        except Exception as e:
            print("An error occurred:", str(e))



