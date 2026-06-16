import re

answer = input("How old are you? ")

age = re.search(r"\d+", answer)

print(f"your age: {age.group()}")