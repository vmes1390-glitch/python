try:
    age=int(input("Enter your age: "))

except ValueError:
    print("Enter your age!")

else:
    print(age)