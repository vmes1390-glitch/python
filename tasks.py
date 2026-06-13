while True:
    try:
        num = int(input("1. Add task\n2. Show tasks\n3. exit\n"))

        if num == 1:
            task = input("Enter your task: ")
            with open("E:/python/tasks.txt", "a") as file:
                file.write(task + "\n")
                print("Added Successfully!")

        elif num == 2:
            with open("E:/python/tasks.txt", "r") as file:
                for line in file:
                    print(line, end="")

        elif num == 3:
            break

        else:
            print("Invalid input!")

    except ValueError:
        print("Invalid input!")