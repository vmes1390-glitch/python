def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a/b

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))

print("addition: ", add(x, y))
print("subtraction: ", subtract(x, y))
print("multiplication: ", multiply(x, y))
print("division: ", divide(x, y))