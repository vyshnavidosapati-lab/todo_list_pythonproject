import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)  # Adds the task to the visual Listbox
        task_entry.delete(0, tk.END)       # Clears the input field
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        # Gets the index of the selected item and deletes it
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def clear_tasks():
    # Clears everything from index 0 to the very end
    task_listbox.delete(0, tk.END)

# ---- GUI Setup ----
root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("400x450")

# 1. Entry Widget (For typing tasks)
task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

# 2. Add Button
add_btn = tk.Button(root, text="Add Task", font=("Arial", 12), width=15, command=add_task, bg="#2ecc71", fg="white")
add_btn.pack(pady=5)

# 3. Listbox Widget (For displaying the list of tasks)
task_listbox = tk.Listbox(root, font=("Arial", 12), width=30, height=12)
task_listbox.pack(pady=10)

# 4. Delete Button
delete_btn = tk.Button(root, text="Delete Selected", font=("Arial", 12), width=15, command=delete_task, bg="#e74c3c", fg="white")
delete_btn.pack(pady=5)

# 5. Clear All Button
clear_btn = tk.Button(root, text="Clear All Tasks", font=("Arial", 12), width=15, command=clear_tasks, bg="#95a5a6", fg="white")
clear_btn.pack(pady=5)

# Start the application loop
root.mainloop()