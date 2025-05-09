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
    
    if  new_task_desc == "":
        print("invalid input")
        return add_task()
    
    task_append_confirmation = input("Are you sure you want to add this(yes or no)?: ")
    
    match task_append_confirmation.lower():
        case "yes":
            print("\n--- Priority List ---")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            choice = input("Whats the priority of this task(Enter a number from the list)?: ")
            match choice:
                case  "1":
                    priority = "Low"
                    new_task_dict = {'description': new_task_desc, 'done': False, 'priority': priority }
                    print("Task added.")
                    tasks.append(new_task_dict)
                    
                case  "2":
                    priority = "Medium"
                    new_task_dict = {'description': new_task_desc, 'done': False, 'priority': priority }
                    print("Task added.")
                    tasks.append(new_task_dict)
                    
                case  "3":
                    priority = "High"
                    new_task_dict = {'description': new_task_desc, 'done': False, 'priority': priority }
                    print("Task added.")
                    tasks.append(new_task_dict)
                case _:
                    print("Invalid input, enter a number.")

                    
            
        case "no":
            print("Task not added.")
            return
        case _:
            print("Invalid answer, please answer with yes or no.")
            return    

def viewtask():
#   Displays the current to-do list to the user, showing the index, status, and description of each task.
    if not tasks:
        print('Your task list is empty!')
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks):
            status = "[X]" if task['done'] else "[ ]"
            print(f"{i + 1}. {status} {task['description']} - Priority : {task['priority']}")
        print("-----------------------\n")

def delete_task():
#    Prompts the user for the number of the task to delete and removes it from the global tasks list, Handles cases where the list is empty or the input is invalid.
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return
    try:
        index_to_delete = int(input("Which task would you like to delete (enter the number)? ")) - 1
        if 0 <= index_to_delete < len(tasks):
            confirmation = input("Are you sure you want to delete this task?(yes or no)")
            match confirmation.lower():
                case 'yes':
                    deleted_task = tasks.pop(index_to_delete)
                    print(f"Task '{deleted_task['description']}' deleted.")
                case 'no':
                    print("Deletion canceled!")
                    return
                case _:
                    print("Invalid answer, please answer with yes or no.")
                    return
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
            confirmation = input("Are you sure you want to confirm this task?(yes or no)")
            match confirmation:
                case 'yes':
                    tasks[index_to_complete]['done'] = True
                    print('Task marked as complete!')
                case 'no':
                    print("Validation canceled")
                    return
                case _:
                    print("Invalid answer, please answer with yes or no.")
                    return
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

def view_done_task():
    if not tasks:
        print('Your task list is empty!')
    else : 
        print("\n--- Done tasks ---")
        for i, task in enumerate(tasks):
            status = "[X]" if task['done'] else "[ ]"
            if status == "[X]":
                print(f"{i + 1}. {status} {task['description']} - Priority : {task['priority']}")
        print("-----------------------\n")
    

def view_notdone_task():
        if not tasks:
            print('Your task list is empty!')
        else : 
            print("\n--- Pending tasks ---")
            for i, task in enumerate(tasks):
                status = "[X]" if task['done'] else "[ ]"
                if status == "[]":
                    print(f"{i + 1}. {status} {task['description']} - Priority : {task['priority']}")
            print("-----------------------\n")


def main():
#   The main function that runs the to-do list application loop, presenting a menu to the user.
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Mark task as complete")
        print("5. View done tasks")
        print("6. View pending tasks")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")
        match choice:
            case '1':
                add_task()
            case '2':
                viewtask()
            case '3':
                delete_task()
            case '4':
                mark_complete_task()
            case '5':
                view_done_task()
            case '6':
                view_notdone_task()
            case '7':
                save_tasks()
                print("Exiting to-do list application. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

main()