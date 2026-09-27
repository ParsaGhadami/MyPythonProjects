tasks = []
def add_new_task():
    new_task = input("Add Your New Task: ")
    tasks.append(new_task)
    print("Done!")
def Show_Tasks():
    print("Your Tasks: ") 
    if len(tasks) == 0:
        print("it does not exist")
    else:
        a = 1
        for item in tasks:
            print(f"{a}.{item}")
            a += 1
# def Complete_Tasks():
while True:
    print("\n===== TO-DO LIST =====\n")
    print("1. Add New task")
    print("2. Show tasks")
    print("3. Complete task")
    print("4. Exit\n")
    choice = input("Choose: ")
    
    if choice == "1":
        add_new_task()
    elif choice == "2":
        Show_Tasks()
    # elif choice == "3":
    #     Complete_Tasks()
    elif choice == "4":
        print("Goodbye.")
        break