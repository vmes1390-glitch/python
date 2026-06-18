class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip() != "":
                self._name = name

        else:
            raise ValueError("Name shoud be string!")

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if 10 <= age <=100:
            self._age = age

        else:
            raise ValueError("Unvalid age!")
        
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"
    

while True:
    print("1. Add student")
    print("2. See results")
    print("3. Exit")


    num = input("Enter number: ")

    if num == "1":
        try:
            name = input("Enter name: ").strip()
            age = int(input("Enter age: "))
            s = Student(name, age)
            with open("E:/python/studentsInfo.txt", "a") as file:
                file.write(str(s) + "\n")
        except ValueError as e:
            print(e)

    elif num == "2":
        with open("E:/python/studentsInfo.txt", "r") as file:
            for line in file:
                print(line, end="")

    elif num == "3":
        break

    else:
        print("Invalid input!")


