import json

tasks = []  # Global list to store to-do tasks

def load_tasks():
#   Loads tasks from the 'tasks.json' file if it exists, If the file is not found or contains invalid JSON, it starts with an empty task list
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        print("Tasks loaded successfully!")
    except FileNotFoundError:
        print("No saved tasks found. Starting with an empty list.")
        tasks = []
    except json.JSONDecodeError:
        print("Error decoding saved tasks. Starting with an empty list.")
        tasks = []

load_tasks()

def add_task():
#   Prompts the user for a task description and adds it as a new incomplete task to the global tasks list.
    new_task_desc = input("Add task description: ")
    new_task_dict = {'description': new_task_desc, 'done': False}
    tasks.append(new_task_dict)

def viewtask():
#   Displays the current to-do list to the user, showing the index, status, and description of each task.
    if not tasks:
        print('Your task list is empty!')
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks):
            status = "[X]" if task['done'] else "[ ]"
            print(f"{i + 1}. {status} {task['description']}")
        print("-----------------------\n")

def delete_task():
#    Prompts the user for the number of the task to delete and removes it from the global tasks list, Handles cases where the list is empty or the input is invalid.
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return
    try:
        index_to_delete = int(input("Which task would you like to delete (enter the number)? ")) - 1
        if 0 <= index_to_delete < len(tasks):
            deleted_task = tasks.pop(index_to_delete)
            print(f"Task '{deleted_task['description']}' deleted.")
        else:
            print("Invalid task number. Please enter a valid number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def mark_complete_task():
#   Prompts the user for the number of the task to mark as complete and updates its status in the global tasks list, Handles cases where the list is empty or the input is invalid.
    
    if not tasks:
        print("Your to-do list is empty. Nothing to mark as complete.")
        return
    try:
        index_to_complete = int(input("Which task would you like to mark as complete? (enter the number) ")) - 1
        if 0 <= index_to_complete < len(tasks):
            tasks[index_to_complete]['done'] = True
            print('Task marked as complete!')
        else:
            print("Invalid task number. Please enter a valid number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def save_tasks():
#   Saves the current global tasks list to the 'tasks.json' file using JSON format, Handles potential errors during the saving process.
    
    try:
        with open('tasks.json', 'w') as file:
            json.dump(tasks, file)
        print("Tasks saved successfully!")
    except Exception as e:
        print(f"Error saving tasks: {e}")

def main():
#   The main function that runs the to-do list application loop, presenting a menu to the user.
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Mark task as complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            viewtask()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_complete_task()
        elif choice == '5':
            save_tasks()
            print("Exiting to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()