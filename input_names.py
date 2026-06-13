name=input("Enter your name: ")

with open("E:/python/names.txt", "a") as file:
    file.write(name + "\n")