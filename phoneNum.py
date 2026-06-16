import re

phone_num = input("Enter your phone number: ")

result = re.fullmatch(r"09\d{9}", phone_num)

print(result is not None)