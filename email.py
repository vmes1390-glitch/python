import re

def is_valid(email):
    return re.fullmatch(r"\w+@gmail\.com", email) is not None

email = input("Enter your email: ")
print(is_valid(email))