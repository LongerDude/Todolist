import tkinter as tk
from tkinter import messagebox, simpledialog
import json

tasks = []

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

def save_tasks():
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
    except Exception as e:
        messagebox.showerror("Error", f"Error saving tasks: {e}")

def refresh_task_list():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✔" if task['done'] else "✘"
        listbox.insert(tk.END, f"{i + 1}. [{status}] {task['description']} ({task['priority']})")

def add_task():
    desc = entry.get()
    if not desc.strip():
        messagebox.showwarning("Invalid input", "Task description cannot be empty.")
        return

    priority = priority_var.get()
    if priority not in ["Low", "Medium", "High"]:
        messagebox.showwarning("Invalid priority", "Please choose a valid priority.")
        return

    task = {'description': desc, 'done': False, 'priority': priority}
    tasks.append(task)
    refresh_task_list()
    entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("No selection", "Please select a task to delete.")
        return

    index = selected[0]
    del tasks[index]
    refresh_task_list()

def mark_complete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("No selection", "Please select a task to mark complete.")
        return

    index = selected[0]
    tasks[index]['done'] = True
    refresh_task_list()

def view_done_tasks():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        if task['done']:
            listbox.insert(tk.END, f"{i + 1}. [✔] {task['description']} ({task['priority']})")

def view_pending_tasks():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        if not task['done']:
            listbox.insert(tk.END, f"{i + 1}. [✘] {task['description']} ({task['priority']})")

def exit_app():
    save_tasks()
    root.destroy()

# GUI SETUP
load_tasks()

root = tk.Tk()
root.title("To-Do List GUI")

frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=0, padx=5)

priority_var = tk.StringVar(value="Select Priority")
priority_menu = tk.OptionMenu(frame, priority_var, "Low", "Medium", "High")
priority_menu.grid(row=0, column=1)

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Delete Task", command=delete_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Mark Complete", command=mark_complete_task).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="View Done", command=view_done_tasks).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="View Pending", command=view_pending_tasks).grid(row=0, column=3, padx=5)
tk.Button(button_frame, text="Save & Exit", command=exit_app).grid(row=0, column=4, padx=5)

refresh_task_list()
root.mainloop()
