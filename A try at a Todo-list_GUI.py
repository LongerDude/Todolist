import customtkinter as ctk

tasks = []
app = ctk.CTk()
app.geometry("320x520")
app.title("My TodoList")
app._set_appearance_mode("Dark")  # You might want to use "Dark" or "Light" directly

def save_entry_in_tasks(event):
    entry_text = add_task_entry.get()
    if entry_text.strip():  # Avoid empty entries
        new_task_dict = {'Task': entry_text}
        tasks.append(new_task_dict)
        
        task_box_list.configure(state="normal")  # Enable text box temporarily
        task_box_list.insert("end", entry_text + "\n")
        task_box_list.configure(state="disabled")  # Disable again to prevent manual edits
        
        add_task_entry.delete(0, "end")  # Clear entry box after adding
        print('Task saved')

# Entry field for tasks
add_task_entry = ctk.CTkEntry(app, placeholder_text="🖌 Add a task...", corner_radius=3, width=300, border_width=2.5)
add_task_entry.pack(padx=50, pady=20)
add_task_entry.bind('<Return>', save_entry_in_tasks)

# Box to display tasks
task_box_list = ctk.CTkTextbox(app, state="disabled", corner_radius=3, border_color="#565b5e", border_width=3, width=300, height=250)
task_box_list.pack(padx=50, pady=20)

app.mainloop()