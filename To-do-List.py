import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", font=("Helvetica", 12), command=self.add_task)
        self.add_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(root, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", font=("Helvetica", 12), command=self.remove_task)
        self.remove_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()

    def remove_task(self):
        selected_index = self.tasks_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_listbox()

    def update_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
