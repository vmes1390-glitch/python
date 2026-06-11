from datetime import date

bYear=int(input("Enter your born year: "))

age=date.today().year-bYear

print(age)