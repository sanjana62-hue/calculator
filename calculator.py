def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Example usage:
if __name__ == '__main__':
    print("Addition: ", add(5, 3))
    print("Subtraction: ", subtract(5, 3))
    print("Multiplication: ", multiply(5, 3))
    print("Division: ", divide(5, 3))