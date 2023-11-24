import json
import os
import time

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the Todo list
def display_todo_list(todo_list):
    clear_console()
    if not todo_list:
        print("No items in the Todo list.")
    else:
        print("Todo List:")
        for i, item in enumerate(todo_list, start=1):
            print(f"{i}. {item['task']}")

# Function to add a new task to the Todo list
def add_task(todo_list, task):
    clear_console()
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    todo_list.append({"task": task, "timestamp": timestamp})
    print("Task added successfully.")

# Function to remove a task from the Todo list
def remove_task(todo_list, task_number):
    clear_console()
    if not todo_list:
        return
    try:
        if task_number < 1 or task_number > len(todo_list):
            print("Invalid task number.")
        else:
            todo_list.pop(task_number - 1)
            print("Task removed successfully.")
    except ValueError:
        print("Invalid task number.")

# Function to save the Todo list to a JSON file
def save_todo_list(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)

# Function to load the Todo list from a JSON file
def load_todo_list():
    if os.path.exists("todo_list.json"):
        with open("todo_list.json", "r") as file:
            todo_list = json.load(file)
        return todo_list
    else:
        return []

# Menu function
def main():
    todo_list = load_todo_list()
    while True:
        clear_console()
        print("=====================")
        print("Todo List App")
        print("1. Display Todo List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        print("=====================")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            display_todo_list(todo_list)
            input("Press Enter to continue...")
        elif choice == "2":
            task = input("Enter task: ")
            add_task(todo_list, task)
            save_todo_list(todo_list)
            input("Press Enter to continue...")
        elif choice == "3":
            display_todo_list(todo_list)
            task_number = int(input("Enter task number to remove: "))
            remove_task(todo_list, task_number)
            save_todo_list(todo_list)
            input("Press Enter to continue...")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()