import os
TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [task.strip() for task in file.readlines()]
    
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter task: ")
    priority = input("Enter priority (High/Medium/Low): ")

    tasks = load_tasks()
    tasks.append(f"[Pending] [{priority}] {task}")

    save_tasks(tasks)
    print("Task added successfully")

def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No tasks found")
    else:
        print("\n========= YOUR TO-DO LIST =========")

        for i, task in enumerate(tasks, 1):
            print(i, ".", task)

        print("\nTotal Tasks:", len(tasks))

def update_task():
    view_tasks()
    tasks = load_tasks()

    try:
        index = int(input("Enter task number to update: ")) - 1

        if 0 <= index < len(tasks):
            new_task = input("Enter new task: ")
            priority = input("Enter priority: ")

            tasks[index] = f"[Pending] [{priority}] {new_task}"

            save_tasks(tasks)
            print("Task updated successfully")
        else:
            print("Enter valid task number")

    except ValueError:
        print("Enter numbers only")


def delete_task():
    view_tasks()
    tasks = load_tasks()

    try:
        index = int(input("Enter task number to delete: ")) - 1

        if 0 <= index < len(tasks):
            removed = tasks.pop(index)

            save_tasks(tasks)
            print("Deleted:", removed)
        else:
            print("Invalid task number")

    except ValueError:
        print("Enter numbers only")


def complete_task():
    view_tasks()
    tasks = load_tasks()

    try:
        index = int(input("Enter completed task number: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index] = tasks[index].replace("[Pending]", "[Completed]")

            save_tasks(tasks)
            print("Task marked as completed")
        else:
            print("Invalid task number")

    except ValueError:
        print("Enter numbers only")


def search_task():
    tasks = load_tasks()

    keyword = input("Enter keyword to search: ").lower()
    found = False

    for task in tasks:
        if keyword in task.lower():
            print(task)
            found = True

    if not found:
        print("No matching tasks found")


def clear_tasks():
    confirm = input("Are you sure? (yes/no): ")

    if confirm.lower() == "yes":
        save_tasks([])
        print("All tasks cleared")
    else:
        print("Operation cancelled")


while True:
    print("\n========== SMART TO-DO LIST ==========")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Complete Task")
    print("6. Search Task")
    print("7. Clear All Tasks")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        complete_task()

    elif choice == "6":
        search_task()

    elif choice == "7":
        clear_tasks()

    elif choice == "8":
        print("Thank you for using Smart To-Do List")
        break

    else:
        print("Invalid choice")