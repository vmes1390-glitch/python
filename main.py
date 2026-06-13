name=input("Enter your name: ")

with open("E:/python/names.txt", "a", newline="\n") as file:
    file.write(name + "\n")