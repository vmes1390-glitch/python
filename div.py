try:
    n = int(input("Enter first number: "))
    m = int(input("Enter second number: "))
    num = n / m

except ZeroDivisionError, ValueError:
    print("can not divide!")



else:
    print(num)